from nse_data import NSEData
from Database import DatabaseHandler

nse = NSEData()
db_handler = DatabaseHandler()

historical_stock_df = nse.get_all_history('RELIANCE', '01-01-2015', '31-10-2024')
print(historical_stock_df.head())

if not historical_stock_df.empty:
    db_handler.save_historical_data('RELIANCE', historical_stock_df)

print("Job Finished")

