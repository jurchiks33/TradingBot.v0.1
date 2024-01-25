
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

    window = GUI.create_main_window(btc_data)
    window.mainloop()

if __name__ == "__main__":
    main()

                        

