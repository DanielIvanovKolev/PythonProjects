import yfinance as yf
import pandas as pd
from datetime import date


def fetch_stock_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date)


if __name__ == "__main__":
    ticker = 'NIO'
    start_date = '2020-01-01'
    end_date = date.today()

    data = fetch_stock_data(ticker, start_date, end_date)

    # 1. Basic info
    print(data.info())

    # 2. Calculate daily returns
    data['Daily_Return'] = data['Close'].pct_change()

    # 3. Resample to monthly data
    monthly_data = data.resample('M').last()

    # 4. Create a 20-day moving average
    data['MA20'] = data['Close'].rolling(window=20).mean()

    # 5. Filter for days when the closing price was above $150
    high_close_days = data[data['Close'] > 150]

    # 6. Get the highest and lowest closing prices
    highest_close = data['Close'].max()
    lowest_close = data['Close'].min()

    # 7. Calculate the correlation between volume and daily returns
    correlation = data['Volume'].corr(data['Daily_Return'])

    print("\nFirst 5 rows with new columns:")
    print(data.head())

    print(f"\nNumber of days with closing price above $150: {len(high_close_days)}")
    print(f"Highest closing price: ${highest_close:.2f}")
    print(f"Lowest closing price: ${lowest_close:.2f}")
    print(f"Correlation between volume and daily returns: {correlation:.4f}")

    print("\nMonthly closing prices:")
    print(monthly_data['Close'])
