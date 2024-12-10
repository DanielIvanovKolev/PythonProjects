# data_collection.py

# First, we import the necessary library
import yfinance as yf
from datetime import date


# We define a function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data for a given ticker and date range.

    Args:
    ticker (str): Stock ticker symbol
    start_date (str): Start date in 'YYYY-MM-DD' format
    end_date (str): End date in 'YYYY-MM-DD' format

    Returns:
    pandas.DataFrame: Historical stock data
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data


# This block allows us to run the script as a standalone program
if __name__ == "__main__":
    # Example usage
    ticker = 'NIO'
    start_date = '2020-01-01'
    end_date = date.today()

    data = fetch_stock_data(ticker, start_date, end_date)

    #data = fetch_stock_data(ticker, start_date, end_date)
    #print(data.head())

# The head() function, by default, displays only the first 5 rows of a pandas DataFrame.
# This is a common practice when working with large datasets
# to get a quick preview of the data without overwhelming the output.

    print(f"Data shape: {data.shape}")
    print("\nFirst 5 rows:")
    print(data.head())
    print("\nLast 5 rows:")
    print(data.tail())
    print("\nData info:")
    data.info()
    print("\nData description:")
    print(data.describe())

# Adding the data to a file, so we can manipulate it
    data.to_csv('nio_stock_data.csv')
