
import GUI
from data_scraper import fetch_crypto_data

def main():
    #fetch data for Bitcoin
    btc_data = fetch_crypto_data('BTC-USD', period='5d', interval='1h')

    window = GUI.create_main_window(btc_data)
    window.mainloop()

if __name__ == "__main__":
    main()

                        

