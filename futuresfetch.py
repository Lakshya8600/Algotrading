from datetime import date
from jugaad_data.nse import derivatives_df
import pandas as pd
import yfinance as yf
from jugaad_data.nse import NSELive

def fetch_futures_data(symbol,from_date: date, to_date: date, expiry_date: date) -> pd.DataFrame:
    """
    Fetches futures data for RELIANCE using jugaad-data library.

    Args:
        from_date (date): The start date for fetching data.
        to_date (date): The end date for fetching data.
        expiry_date (date): The expiry date of the futures contract.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the futures data.
                      Returns an empty DataFrame if no data is found or an error occurs.
    """
    try:
        # Define the symbol for Reliance
        # symbol = "RELIANCE"
        # Define the instrument type for stock futures
        instrument_type = "FUTSTK" # FUTSTK for Stock Futures, FUTIDX for Index Futures

        print(f"Fetching futures data for {symbol} from {from_date} to {to_date} with expiry {expiry_date}...")

        # Fetch the derivatives data
        df = derivatives_df(
            symbol=symbol,
            from_date=from_date,
            to_date=to_date,
            expiry_date=expiry_date,
            instrument_type=instrument_type
        )

        if df.empty:
            print("No data found for the specified criteria.")
        else:
            print("Data fetched successfully!")

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame() # Return an empty DataFrame in case of an error

if __name__ == "__main__":
    start_date = date(2025, 5, 1)
    end_date = date(2025, 6, 11) # Example end date
    futures_expiry_date = date(2025, 6, 26)
    reliance_futures_data = fetch_futures_data("RELIANCE",start_date, end_date, futures_expiry_date)

    # Display the first few rows of the fetched data
    if not reliance_futures_data.empty:
        print("RELIANCE")
        print("\nFirst 5 rows of RELIANCE futures data:")
        print(reliance_futures_data.head())
        print(reliance_futures_data.iloc[0,6])  # Display first 5 columns

    print("Reliance Futures Data Fetching Complete. Program is Working")
    df = pd.read_csv("stocksname.csv")
    print(df.head())  # Display the first few rows of the stocks data
      # Display the first few rows of the stocks data
    df["cmp"] = None
    df["fmp"] = None

    n = NSELive()
    for i in range(len(df)):
        stockname = df.iloc[i,1]
        try:
            futures_data = fetch_futures_data(stockname,start_date, end_date, futures_expiry_date)
            futures_price = futures_data.iloc[0,6]
            quote = n.stock_quote(stockname)  # Replace with your stock symbol
            print("Current Market Price (CMP):", quote['priceInfo']['lastPrice'])
            print("Futures Price (CMP):", futures_price)
            df.iloc[i, 2] = quote['priceInfo']['lastPrice']
            df.iloc[i, 3] = futures_price

        except Exception as e:
            # print(f"An error occurred while fetching data for {stockname}: {e}")
            continue    
        
    df.to_csv("stocksnamewithfutpr.csv", index=False)  # Save the updated DataFrame to CSV