
# src/logger.py
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

class LoggerSetup:
    @staticmethod
    def setup_logger(name: str, config: dict[str, any]) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(config['logging']['level'])
        
        # File handler
        file_handler = RotatingFileHandler(
            config['logging']['file'],
            maxBytes=1024 * 1024,
            backupCount=5
        )
        file_handler.setFormatter(logging.Formatter(config['logging']['format']))
        logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(config['logging']['format']))
        logger.addHandler(console_handler)
        
        return logger
