import yfinance as yf

def fetch_crypto_data(ticker_symbol, period="id", interval="1m"):
    """
    Fetches historical market data for the given cryptocurrency ticker symbol from Yahoo Finance.
    
    :param ticker_symbol: Cryptocurrency symbol, e.g., 'BTC-USD' for Bitcoin.
    :param period: The data period to download (default is '1d').
    :param interval: Data interval (default is '1m').
    :return: DataFrame with historical market data.
    """
    data = yf.download(ticker_symbol, period=period, interval=interval)
    return data