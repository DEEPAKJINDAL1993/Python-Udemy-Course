from EDA import SnowflakeEDA


eda = SnowflakeEDA(database='SHARED_DB_XACTLY_GIC',schema='INCENT2')
eda.connect()
#top_n_values = eda.get_top_n_values_per_column('XC_POSITION_V', 10)
stats = eda.get_column_stats('XC_POSITION_V','IS_MASTER')
# top_n_values.to_csv("top_n_values.csv")
print(stats)
#print(top_n_values)
# eda.disconnect()