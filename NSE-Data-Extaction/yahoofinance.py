import yfinance as yf
import plotly.graph_objects as go
import datetime

# Define the stock symbol and date range
stock_symbol = 'RELIANCE.NS'  # Add .NS for NSE stocks
start_date = '2023-01-01'
end_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Get historical data
historical_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Check if data is fetched
if historical_data.empty:
    print("No data fetched. Please check the stock symbol or date range.")
else:
    # Create a candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=historical_data.index,
                                          open=historical_data['Open'],
                                          high=historical_data['High'],
                                          low=historical_data['Low'],
                                          close=historical_data['Close'])])

    # Update layout
    fig.update_layout(title=f'Candlestick Chart for {stock_symbol}',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      xaxis_rangeslider_visible=False)

    # Show the chart
    fig.show()
