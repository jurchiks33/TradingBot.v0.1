
import GUI
from data_scraper import fetch_crypto_data

def main():
    #List of crypto pairs.
    crypto_pairs = [
        'BTC-USD',    # Bitcoin
        'ETH-USD',    # Ethereum
        'XRP-USD',    # Ripple
        'LTC-USD',    # Litecoin
        'BCH-USD',    # Bitcoin Cash
        'ADA-USD',    # Cardano
        'DOT-USD',    # Polkadot
        'LINK-USD',   # Chainlink
        'BNB-USD',    # Binance Coin
        'XLM-USD',    # Stellar
        'USDT-USD',   # Tether
        'DOGE-USD',   # Dogecoin
        'UNI-USD',    # Uniswap
        'SOL-USD',    # Solana
        'USDC-USD',   # USD Coin
        'MATIC-USD',  # Polygon
        'ALGO-USD',   # Algorand
        'VET-USD',    # VeChain
        'ICP-USD',    # Internet Computer
        'TRX-USD'     # TRON
    ]

    #Fetching data for the first pair.
    initial_pair = crypto_pairs[0]
    initial_data = fetch_crypto_data(initial_pair, period='5d',
                                     interval='1h')

    window = GUI.create_main_window(initial_data, crypto_pairs)
    window.mainloop()

if __name__ == "__main__":
    main()

                        

