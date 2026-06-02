import requests
import time
import json
import pandas as pd


class NSEDataFetcher:
    def __init__(self):
        # URLs for fetching current stock data and historical data
        self.nse_home_url = 'https://www.nseindia.com'
        self.nse_chart_home_url = 'https://charting.nseindia.com'
        self.stock_data_url = 'https://www.nseindia.com/api/quote-equity'
        self.historical_data_url = 'https://charting.nseindia.com/Charts/symbolhistoricaldata/'
        self.nse_historical_data_url = 'https://www.nseindia.com/api/historical/securityArchives'

        # Initialize separate sessions for stock data and historical data
        self.stock_session = self._initialize_stock_session()
        self.historical_session = self._initialize_historical_session()

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

    def _initialize_historical_session(self):
        """
        Initialize a session for historical data API with appropriate headers.
        """
        session = requests.Session()
        historical_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'charting.nseindia.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': self.nse_chart_home_url,
            'Content-Type': 'application/json'
        }
        session.headers.update(historical_headers)

        """
                        This private method initializes the session by visiting the NSE home page
                        to set up necessary cookies.
                        """
        home_url = self.nse_chart_home_url
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

    def get_historical_data(self, symbol, scrip_code, start_date, end_date, interval="D", period="W"):
        """
        Fetch historical data for a given stock symbol within a date range from NSE Charting.

        Parameters:
        - symbol (str): The stock symbol (e.g., 'INFY' for Infosys)
        - scrip_code (int): Scrip code representing the stock symbol (e.g., 1594 for INFY)
        - start_date (str): Start date in 'yyyy-mm-dd' format
        - end_date (str): End date in 'yyyy-mm-dd' format
        - interval (str): Time interval for the data ('1' for daily data, default is 'D' for daily)
        - period (str): Chart period ('W' for weekly, 'D' for daily)

        Returns:
        - dict: JSON response containing historical stock data
        """
        # Convert dates to epoch time
        from_date_epoch = self._convert_to_epoch(start_date)
        to_date_epoch = self._convert_to_epoch(end_date)

        # Create the payload for the POST request
        payload = {
            "exch": "N",  # 'N' for NSE
            "instrType": "C",  # 'C' for equity (you may change this for different types)
            "scripCode": scrip_code,  # The scrip code for the symbol
            "ulToken": scrip_code,  # Seems to be the same as scripCode
            "fromDate": from_date_epoch,  # From date in epoch
            "toDate": to_date_epoch,  # To date in epoch
            "timeInterval": interval,  # Time interval (1 for daily, etc.)
            "chartPeriod": period,  # Chart period ('W' for weekly, 'D' for daily)
            "chartStart": 0  # Pagination or starting point for the chart
        }

        try:
            # Make a POST request with the payload using the persistent historical session
            response = self.historical_session.post(self.historical_data_url, data=json.dumps(payload))

            if response.status_code == 200:
                try:
                    data = response.json()
                    return data
                except ValueError:
                    print("Error: Unable to parse the response as JSON.")
                    print(response.text)
            else:
                print(f"Failed to fetch historical data for {symbol}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching historical data for {symbol}: {e}")
        return None


    def get_stock_history(self, symbol, start_date, end_date, dataType = "priceVolumeDeliverable" , series = "ALL"):
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

        # Create the payload for the POST request
        payload = {
            "symbol": symbol,
            "from": start_date,
            "to": end_date,
            "dataType": dataType,
            "series": series
            }

        # Make a request for stock data using the persistent stock session
        stock_url = f"{self.nse_historical_data_url}?symbol={symbol}&from={start_date}&to={end_date}&dataType={dataType}&series={series}"

        try:
            # Make a get request with the payload using the persistent historical session
            # response = self.stock_session.post(self.nse_historical_data_url, data=json.dumps(payload))
            response = self.stock_session.get(stock_url)

            if response.status_code == 200:
                try:
                    data = response.json()
                    return data
                except ValueError:
                    print("Error: Unable to parse the response as JSON.")
                    print(response.text)
            else:
                print(f"Failed to fetch historical data for {symbol}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching historical data for {symbol}: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Instantiate the NSEDataFetcher class
    nse_fetcher = NSEDataFetcher()

    # Fetch stock data for RELIANCE (RELIANCE)
    stock_data = nse_fetcher.get_stock_data('RELIANCE')
    #stock_data_df = pd.json_normalize(stock_data)
    if stock_data:
        print("Current Stock Data:")
        print(json.dumps(stock_data, indent=4))

    # Fetch historical data for RELIANCE from 1st Jan 2023 to 1st Oct 2023
    historical_stock_data = nse_fetcher.get_historical_data('RELIANCE', 2885, '2019-01-01', '2024-10-06', interval=1, period="D")
    historical_df = pd.DataFrame({
        'Date': pd.to_datetime(historical_stock_data['t'], unit='s'),
        'Open': historical_stock_data['o'],
        'High': historical_stock_data['h'],
        'Low': historical_stock_data['l'],
        'Close': historical_stock_data['c'],
        'Volume': historical_stock_data['v']
    })
    if historical_stock_data:
        print("\nHistorical Stock Data:")
        print(historical_df)

    # Fetch historical data for RELIANCE from 1st Jan 2023 to 1st Oct 2023
    historical_data = nse_fetcher.get_stock_history('RELIANCE', '31-01-2023', '05-10-2024')
    # Convert to DataFrame
    # data = json.loads(historical_data)
    historical_stock_df = pd.DataFrame(historical_data['data'])

    # Simplify column names
    historical_stock_df.columns = [
        "ID",
        "Symbol",
        "Series",
        "Market_Type",
        "Trade_High_Price",
        "Trade_Low_Price",
        "Opening_Price",
        "Closing_Price",
        "Last_Trade_Price",
        "Previous_Close_Price",
        "Total_Trade_Quantity",
        "Total_Trade_Value",
        "52_Week_High",
        "52_Week_Low",
        "Total_Trades",
        "ISIN",
        "Timestamp",
        "Full_Timestamp",
        "Created_At",
        "Updated_At",
        "Version",
        "Delivery_Quantity",
        "Delivery_Percentage",
        "VWAP",
        "Market_Date"
    ]

    if historical_data:
        print("\nHistorical Data:")
        print(historical_stock_df)
        #print(json.dumps(historical_data, indent=4))


