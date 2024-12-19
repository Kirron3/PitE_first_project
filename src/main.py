import logging
import time
import signal
import sys
from config import load_config
from data import DataFetcher
from processor import DataProcessor

def setup_logging(config):
    logging.basicConfig(
        filename=config['app']['log_file'],
        level=logging.INFO,
        format='%(message)s'
    )
    
    # Also log to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(console_handler)

def signal_handler(signum, frame):
    print("\nShutdown requested...")
    sys.exit(0)

def main():
    config = load_config()
    setup_logging(config)
    logging.info("Starting Crypto Price Monitor...")
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        data_fetcher = DataFetcher(config)
        processor = DataProcessor()
        data_fetcher.set_processor(processor)
        data_fetcher.start()
        
        # Keep the main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        logging.info("Shutting down...")
        data_fetcher.stop()
        sys.exit(0)
        
    except Exception as e:
        logging.error(f"Fatal error in main: {e}")
        data_fetcher.stop()
        sys.exit(1)

if __name__ == "__main__":
    main()