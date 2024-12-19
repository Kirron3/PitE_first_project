import threading
import logging
from datetime import datetime

class DataProcessor:
    def __init__(self):
        self.threads = []
        self.previous_prices = {}
        
    def process_data(self, data):
        thread = threading.Thread(target=self._process, args=(data,))
        thread.daemon = True  # Thread will stop when main program stops
        self.threads.append(thread)
        thread.start()
        
    def _process(self, data):
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            
            for crypto, prices in data.items():
                current_price = prices['usd']
                
                if crypto in self.previous_prices:
                    prev_price = self.previous_prices[crypto]
                    change = ((current_price - prev_price) / prev_price) * 100
                    
                    logging.info(f"[{current_time}] {crypto.upper()}: ${current_price:,.2f} "
                               f"({'+'if change>0 else ''}{change:.2f}%)")
                else:
                    logging.info(f"[{current_time}] {crypto.upper()}: ${current_price:,.2f}")
                
                self.previous_prices[crypto] = current_price
                
        except Exception as e:
            logging.error(f"Error processing data: {e}")