import requests
import threading
import time
import logging

class DataFetcher:
    def __init__(self, config):
        self.config = config
        self.running = False
        self.processor = None
        
    def set_processor(self, processor):
        self.processor = processor
        
    def start(self):
        self.running = True
        self.fetch_thread = threading.Thread(target=self._fetch_loop)
        self.fetch_thread.daemon = True  # Thread will stop when main program stops
        self.fetch_thread.start()
        
    def _fetch_loop(self):
        while self.running:
            try:
                response = requests.get(self.config['data']['source_url'])
                data = response.json()
                logging.info(f"Current prices: {data}")
                
                if self.processor:
                    self.processor.process_data(data)
                    
            except Exception as e:
                logging.error(f"Error fetching data: {e}")
            
            time.sleep(self.config['data']['refresh_rate'])

    def stop(self):
        self.running = False
        logging.info("Data fetcher stopping...")