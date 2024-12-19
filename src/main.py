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
    # Load configuration
    config = load_config()
    
    # Setup logging
    setup_logging(config)
    logging.info("Starting Crypto Price Monitor...")
    
    # Setup graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        # Initialize components
        data_fetcher = DataFetcher(config)
        processor = DataProcessor()
        
        # Connect processor to fetcher
        data_fetcher.set_processor(processor)
        
        # Start data collection
        data_fetcher.start()
        
        # Keep the main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        logging.info("Shutting down gracefully...")
        data_fetcher.stop()
        sys.exit(0)
        
    except Exception as e:
        logging.error(f"Fatal error in main: {e}")
        data_fetcher.stop()
        sys.exit(1)

if __name__ == "__main__":
    main()