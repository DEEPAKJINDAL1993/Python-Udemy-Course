import requests
import time
import json
import io
import pandas as pd
from datetime import datetime,timedelta


class NSEData:
    def __init__(self):
        # URLs for fetching current stock data and historical data
        self.nse_home_url = 'https://www.nseindia.com'
        self.nse_chart_home_url = 'https://charting.nseindia.com'
        self.stock_data_url = 'https://www.nseindia.com/api/quote-equity'
        self.historical_data_url = 'https://charting.nseindia.com/Charts/symbolhistoricaldata/'
        self.nse_historical_data_url = 'https://www.nseindia.com/api/historical/securityArchives'

        # Initialize separate sessions for stock data and historical data
        self.stock_session = self._initialize_stock_session()
        # self.historical_session = self._initialize_historical_session()

    def _initialize_stock_session(self):
        """
        Initialize a session for stock data API with appropriate headers.
        """
        session = requests.Session()
        stock_headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Host': 'www.nseindia.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': self.nse_home_url,
        }

        session.headers.update(stock_headers)

        """
                This private method initializes the session by visiting the NSE home page
                to set up necessary cookies.
                """
        home_url = self.nse_home_url
        try:
            response = session.get(home_url)
            if response.status_code == 200:
                print("Session initialized successfully.")
            else:
                print(f"Failed to initialize session. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while initializing session: {e}")

        return session

    def _convert_to_epoch(self, date_str):
        """
        Convert date from 'yyyy-mm-dd' format to epoch time.
        """
        pattern = '%Y-%m-%d'
        epoch_time = int(time.mktime(time.strptime(date_str, pattern)))
        return epoch_time

    def get_stock_data(self, symbol):
        """
        Fetch stock data for a given symbol from the NSE website.

        Parameters:
        - symbol (str): The stock symbol (e.g., 'INFY' for Infosys)

        Returns:
        - dict: JSON response from the NSE API containing stock data
        """
        # Make a request for stock data using the persistent stock session
        stock_url = f"{self.stock_data_url}?symbol={symbol}"
        print(stock_url)
        try:
            response = self.stock_session.get(stock_url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    return data
                except ValueError:
                    print("Error: Unable to parse the response as JSON.")
                    print(response.text)
            else:
                print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching stock data for {symbol}: {e}")
        return None

    def get_12_month_history(self, symbol, start_date, end_date, dataType="priceVolumeDeliverable" , series = "ALL"):
        """
                Fetch historical data for a given stock symbol within a date range from NSE Website.

                Parameters:
                - symbol (str): The stock symbol (e.g., 'INFY' for Infosys)
                - start_date (str): Start date in 'dd-mm-yyyy' format
                - end_date (str): End date in 'dd-mm-yyyy' format
                - datatype (str): Type of data ('priceVolumeDeliverable' for Price-Volume data, default is 'priceVolumeDeliverable' for Price-Volume data)
                - series (str): Default is 'ALL'

                Returns:
                - dict: JSON response containing historical stock data
                """

        # Make a request for stock data using the persistent stock session
        stock_url = f"{self.nse_historical_data_url}?symbol={symbol}&from={start_date}&to={end_date}&dataType={dataType}&series={series}&csv=true"
        print(stock_url)


        try:
            # Make a get request with the payload using the persistent historical session
            # response = self.stock_session.post(self.nse_historical_data_url, data=json.dumps(payload))
            response = self.stock_session.get(stock_url)

            if response.status_code == 200:
                try:
                    csv_content = io.StringIO(response.content.decode('utf-8'))
                    df = pd.read_csv(csv_content)
                    return df
                except ValueError:
                    print("Error: Unable to parse the response as JSON.")
                    print(response.text)
            else:
                print(f"Failed to fetch historical data for {symbol}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching historical data for {symbol}: {e}")
        return None

    def get_all_history(self, symbol, start_date, end_date, dataType="priceVolumeDeliverable", series="ALL"):
        """
        Fetch historical stock data iteratively over multiple years (to handle API constraints).

        Parameters:
        - symbol (str): Stock symbol
        - start_date (str): Start date in 'dd-mm-yyyy' format
        - end_date (str): End date in 'dd-mm-yyyy' format
        - dataType (str): Type of data ('priceVolumeDeliverable', default is 'priceVolumeDeliverable')
        - series (str): Series type (default is 'ALL')

        Returns:
        - DataFrame: Combined historical data for the given symbol over multiple years
        """

        def date_range_chunks(start, end, delta=364):
            """
            Helper function to split the date range into chunks of `delta` days.
            """
            current_start = datetime.strptime(start, "%d-%m-%Y")
            current_end = datetime.strptime(end, "%d-%m-%Y")

            while current_start < current_end:
                chunk_end = min(current_start + timedelta(days=delta), current_end)
                yield current_start.strftime("%d-%m-%Y"), chunk_end.strftime("%d-%m-%Y")
                current_start = chunk_end + timedelta(days=1)

        # Initialize an empty DataFrame to store results
        full_data_df = pd.DataFrame()

        # Fetch data in chunks of 12 months (or a given delta)
        for start_chunk, end_chunk in date_range_chunks(start_date, end_date, 364):
            print(f"Fetching data from {start_chunk} to {end_chunk}...")
            data_chunk = self.get_12_month_history(symbol, start_chunk, end_chunk, dataType, series)

            if isinstance(data_chunk, pd.DataFrame) and not data_chunk.empty:
                # chunk_df = pd.DataFrame(data_chunk['data'])
                chunk_df = pd.DataFrame(data_chunk)
                full_data_df = pd.concat([full_data_df, chunk_df], ignore_index=True)
            else:
                print(f"No data fetched for period {start_chunk} to {end_chunk}")

        full_data_df.columns = [
            "Symbol",
            "Series",
            "Date",
            "Prev_Close",
            "Open_Price",
            "High_Price",
            "Low_Price",
            "Last_Price",
            "Close_Price",
            "Average_Price",
            "Total_Traded_Quantity",
            "Turnover",
            "No_Of_Trades",
            "Deliverable_Quantity",
            "Percent_Deliverable_Qty"
        ]

        return full_data_df


# Example usage:
if __name__ == "__main__":
    # Instantiate the NSEData class
    nse = NSEData()

    # Fetch stock data for RELIANCE (RELIANCE)
    stock_data = nse.get_stock_data('RELIANCE')

    # stock_data_df = pd.json_normalize(stock_data)
    if stock_data:
        print("Current Stock Data:")
        print(json.dumps(stock_data, indent=4))

    # Fetch historical data for RELIANCE from 1st Jan 2023 to 1st Oct 2023
    historical_stock_df = nse.get_all_history('RELIANCE', '01-01-2015', '31-10-2024')

    # Convert to DataFrame
    # data = json.loads(historical_data)
    #historical_stock_df = pd.DataFrame(historical_data['data'])


    # if historical_stock_df:
    print("\nHistorical Data:")
    print(historical_stock_df)


