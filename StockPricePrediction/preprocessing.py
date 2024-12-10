import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def load_data(file_path):
    """
    Load the stock data from a CSV file.
    """
    return pd.read_csv(file_path, index_col='Date', parse_dates=True)


def add_simple_features(df):
    """
    Add some simple features to our dataset.
    """
    # Calculate daily returns
    df['Returns'] = df['Close'].pct_change()

    # Add a 5-day moving average
    df['MA5'] = df['Close'].rolling(window=5).mean()

    return df


def normalize_data(df):
    """
    Normalize the data using Min-Max scaling.
    """
    scaler = MinMaxScaler()
    columns_to_normalize = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Returns', 'MA5']
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
    return df, scaler


def preprocess_data(file_path):
    """
    Main function to preprocess the data.
    """
    df = load_data(file_path)
    df = add_simple_features(df)
    df = df.dropna()  # Remove any rows with missing data
    df_normalized, scaler = normalize_data(df)
    return df_normalized


if __name__ == "__main__":
    file_path = 'nio_stock_data.csv'  # Make sure this matches your file name
    processed_data = preprocess_data(file_path)

    print("Processed Data:")
    print(processed_data.tail())
    print("\nData Info:")
    print(processed_data.info())

    # Verify the presence of 'Returns' and 'MA5' columns
    print("\nColumns in processed data:")
    print(processed_data.columns)

    if 'Returns' in processed_data.columns and 'MA5' in processed_data.columns:
        print("\n'Returns' and 'MA5' columns are present in the processed data.")
    else:
        print("\nWARNING: 'Returns' or 'MA5' columns are missing from the processed data.")

    # Show a few rows of 'Returns' and 'MA5' columns
    print("\nSample of 'Returns' and 'MA5' columns:")
    print(processed_data[['Returns', 'MA5']].head())