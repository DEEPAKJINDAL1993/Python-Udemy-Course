import sqlite3
import pandas as pd
from datetime import datetime


class DatabaseHandler:
    def __init__(self, db_name="nse_data.db"):
        # Initialize database connection
        self.connection = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self):
        """
        Create tables for stock and historical data.
        """
        cursor = self.connection.cursor()

        # Create historical data table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historical_data (
                Symbol TEXT,
                Series TEXT,
                Date DATE,
                Prev_Close REAL,
                Open_Price REAL,
                High_Price REAL,
                Low_Price REAL,
                Last_Price REAL,
                Close_Price REAL,
                Average_Price REAL,
                Total_Traded_Quantity INTEGER,
                Turnover REAL,
                No_Of_Trades INTEGER,
                Deliverable_Quantity INTEGER,
                Percent_Deliverable_Qty REAL,
                PRIMARY KEY (symbol, date)
            )
        ''')

        # Create index on symbol and date fields
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_symbol_date
            ON historical_data (symbol, date);
        ''')

        self.connection.commit()

    def save_historical_data(self, symbol, df):
        """
        Save historical stock data to the historical_data table.
        """
        cursor = self.connection.cursor()

        try:
            # Iterate through each row in the DataFrame and insert it into the database
            for _, row in df.iterrows():
                # Convert date from 'dd-MMM-yyyy' to 'YYYY-MM-DD'
                date_str = row['Date']
                parsed_date = datetime.strptime(date_str, "%d-%b-%Y").date()

                cursor.execute('''
                    INSERT OR REPLACE INTO historical_data (Symbol, Series, Date, Prev_Close, Open_Price, High_Price, Low_Price,
                             Last_Price, Close_Price, Average_Price, Total_Traded_Quantity, Turnover, No_Of_Trades,
                              Deliverable_Quantity, Percent_Deliverable_Qty)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    symbol,
                    row['Series'],
                    parsed_date,
                    row['Prev_Close'],
                    row['Open_Price'],
                    row['High_Price'],
                    row['Low_Price'],
                    row['Last_Price'],
                    row['Close_Price'],
                    row['Average_Price'],
                    row['Total_Traded_Quantity'],
                    row['Turnover'],
                    row['No_Of_Trades'],
                    row['Deliverable_Quantity'],
                    row['Percent_Deliverable_Qty']
                ))
            self.connection.commit()
            print("Historical data saved successfully.")

        except Exception as e:
            print(f"An error occurred while saving historical data: {e}")

        finally:
            cursor.close()

    def delete_data_by_symbol(self, symbol):
        """
        Delete all historical data for the given stock symbol.

        Parameters:
        - symbol (str): The stock symbol for which to delete data
        """
        cursor = self.connection.cursor()
        try:
            # Execute the DELETE statement
            cursor.execute('''
                DELETE FROM historical_data
                WHERE symbol = ?
            ''', (symbol,))

            # Commit the changes
            self.connection.commit()
            print(f"Data for symbol '{symbol}' deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting data for symbol '{symbol}': {e}")
        finally:
            cursor.close()

    def fetch_data_by_symbol(self, symbol):
        """
        Fetch all historical data for a given stock symbol.

        Parameters:
        - symbol (str): The stock symbol to filter the data by.

        Returns:
        - DataFrame: A pandas DataFrame containing the historical data for the given symbol,
                     or an empty DataFrame if no data is found.
        """
        cursor = self.connection.cursor()
        try:
            # Execute the SELECT statement
            cursor.execute('''
                SELECT * FROM historical_data
                WHERE symbol = ?
            ''', (symbol,))

            # Fetch all rows and convert them to a pandas DataFrame
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]  # Get column names
            data_df = pd.DataFrame(rows, columns=columns)

            if not data_df.empty:
                print(f"Data for symbol '{symbol}' fetched successfully.")
            else:
                print(f"No data found for symbol '{symbol}'.")

            return data_df
        except Exception as e:
            print(f"An error occurred while fetching data for symbol '{symbol}': {e}")
            return pd.DataFrame()  # Return an empty DataFrame in case of error
        finally:
            cursor.close()

    def close_connection(self):
        self.connection.close()

