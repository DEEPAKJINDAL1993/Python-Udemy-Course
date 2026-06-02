import snowflake.connector
import pandas as pd
import configparser
import ast


class SnowflakeEDA:

    def __init__(self, config_file='config.ini',database=None, schema=None, role=None, user=None, password=None, account=None, warehouse=None):
        self.config = self.load_config(config_file)
        self.database = database or self.config['database']
        self.schema = schema or self.config['schema']
        self.role = role or self.config['role']
        self.user = user or self.config['user']
        self.password = password or self.config['password']
        self.account = account or self.config['account']
        self.warehouse = warehouse or self.config['warehouse']
        self.conn = None

    def load_config(self, config_file):
        """Load configuration from an INI file."""
        config = configparser.ConfigParser()
        config.read(config_file)
        return config['snowflake']

    def connect(self):
        """Establish connection to Snowflake using loaded config."""

        self.conn = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema,
            role=self.role
        )
        print(f"Connection established to {self.database}")

    def disconnect(self):
        """Close the Snowflake connection"""
        if self.conn:
            self.conn.close()
            print("Connection closed.")

    def get_columns_info(self, table_name):
        """List all columns with their data types for a given table"""
        query = f"""
        SELECT COLUMN_NAME, DATA_TYPE
        FROM {self.database}.INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = '{self.schema}' AND TABLE_NAME = '{table_name.upper()}';
        """
        return pd.read_sql(query, self.conn)

    def get_record_count(self, table_name):
        """Return the number of records in the table"""
        query = f"SELECT COUNT(*) as count FROM {self.database}.{self.schema}.{table_name};"
        return pd.read_sql(query, self.conn)['COUNT'][0]

    def get_top_n_values_per_column(self, table_name, n=10):
        """Get top N values for each column in the table using APPROX_TOP_K"""
        columns_info = self.get_columns_info(table_name)
        column_names = columns_info['COLUMN_NAME'].tolist()

        query_parts = []
        for column in column_names:
            query_parts.append(f"""
                (SELECT '{column}' AS column_name, APPROX_TOP_K({column},{n}) as top_n_values
                FROM {self.database}.{self.schema}.{table_name})
            """)

        full_query = " UNION ALL ".join(query_parts)
        print(full_query)

        df = pd.read_sql(full_query, self.conn)

        # Parsing the `TOP_N_VALUES` column
        def clean_top_n_values(column):
            # Parse the JSON-like string into a Python list
            return [dict(zip(["Value", "Frequency"], pair)) for pair in ast.literal_eval(column)]

        # Apply the cleaning function to `TOP_N_VALUES` column
        df["TOP_N_VALUES"] = df["TOP_N_VALUES"].apply(clean_top_n_values)

        return df

    def get_column_stats(self, table_name, column_name):
        """Calculate basic stats for a specific numeric column using Snowflake SQL"""
        query = f"""
        SELECT 
            MIN({column_name}) AS min_value,
            MAX({column_name}) AS max_value,
            AVG({column_name}) AS avg_value,
            MEDIAN({column_name}) AS median_value
        FROM {self.database}.{self.schema}.{table_name};
        """
        return pd.read_sql(query, self.conn)

    def aggregate_columns(self, table_name, agg_column, group_by_columns, agg_func="sum"):
        """Aggregate certain columns with specified functions (sum, avg, etc.)"""
        group_by_str = ", ".join(group_by_columns)
        query = f"""
        SELECT {group_by_str}, {agg_func}({agg_column}) as {agg_func}_{agg_column}
        FROM {self.database}.{self.schema}.{table_name}
        GROUP BY {group_by_str};
        """
        return pd.read_sql(query, self.conn)


# Example usage:
if __name__ == "__main__":
    eda = SnowflakeEDA()
    eda.connect()
    top_n_values = eda.get_top_n_values_per_column('V_HISTORICAL_AD_HOC_ALF_USD', 10)
    # column_stats = eda.get_column_stats('V_HISTORICAL_AD_HOC_ALF_USD', 'PAYMENT_AMOUNT_USD')
    print(top_n_values)
    eda.disconnect()
