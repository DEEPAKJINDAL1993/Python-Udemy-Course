import requests


class NSEDataFetcher:
    def __init__(self):
        # URL for NSE API
        self.base_url = 'https://www.nseindia.com/api/quote-equity'
        # Headers to simulate browser behavior
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Host': 'www.nseindia.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
            'Referer': 'https://www.nseindia.com',
            'X-Requested-With': 'XMLHttpRequest'
        }
        # Create a session to manage cookies and persistent connections
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        # Fetch initial cookies by visiting NSE home page
        self._initialize_session()

    def _initialize_session(self):
        """
        This private method initializes the session by visiting the NSE home page
        to set up necessary cookies.
        """
        home_url = 'https://www.nseindia.com'
        try:
            response = self.session.get(home_url)
            if response.status_code == 200:
                print("Session initialized successfully.")
            else:
                print(f"Failed to initialize session. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while initializing session: {e}")

    def get_stock_data(self, symbol):
        """
        Fetch stock data for a given symbol from the NSE website.

        Parameters:
        - symbol (str): The stock symbol (e.g., 'INFY' for Infosys)

        Returns:
        - dict: JSON response from the NSE API containing stock data
        """
        stock_url = f"{self.base_url}?symbol={symbol}"
        try:
            response = self.session.get(stock_url)
            if response.status_code == 200:
                # Attempt to parse the JSON response
                try:
                    data = response.json()
                    return data
                except ValueError:
                    print("Error: Unable to parse the response as JSON.")
                    print(response.text)  # Show the response text for debugging
            else:
                print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching stock data for {symbol}: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Instantiate the NSEDataFetcher class
    nse_fetcher = NSEDataFetcher()

    # Fetch stock data for INFY (Infosys)
    stock_data = nse_fetcher.get_stock_data('INFY')

    # Print the fetched data
    if stock_data:
        print(stock_data)
