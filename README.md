# Crypto Price Monitor

A real-time cryptocurrency price monitoring system built with Python. This project demonstrates real-time data fetching, multithreading, and logging capabilities while tracking Bitcoin and Ethereum prices.

## Features

- Real-time price updates every 5 seconds
- Price change percentage calculation
- Multithreaded data fetching and processing
- Console and file logging
- Graceful shutdown handling
- YAML-based configuration

## Project Structure

```
project/
├── config/
│   └── config.yaml       # Configuration settings
├── logs/
│   └── app.log          # Application logs
├── src/
│   ├── __init__.py
│   ├── main.py          # Main entry point
│   ├── config.py        # Configuration management
│   ├── data.py          # Data fetching
│   └── processor.py     # Data processing
└── README.md
```

## Requirements

- Python 3.7+
- Required packages:
  - requests
  - pyyaml

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd crypto-price-monitor
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install requests pyyaml
```

4. Create required directories:
```bash
mkdir -p logs
```

## Usage

1. Start the monitor:
```bash
python src/main.py
```

2. Stop the monitor:
   - Press `CTRL+C` to shutdown the application

## Configuration

You can modify the `config/config.yaml` file to adjust:
- Log file location
- Data refresh rate
- API endpoint URL

```yaml
app:
  name: "Crypto Price Monitor"
  log_file: "logs/app.log"
  
data:
  refresh_rate: 5  # Refresh rate in seconds
  source_url: "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
```

## Output Example

```
Starting Crypto Price Monitor...
[14:23:45] BITCOIN: $42,123.45 (+0.35%)
[14:23:45] ETHEREUM: $2,845.67 (-0.12%)
```

## Project Components

- **DataFetcher**: Handles the retrieval of cryptocurrency prices from the CoinGecko API
- **DataProcessor**: Processes the price data and calculates price changes
- **ConfigManager**: Manages the application configuration
- **Main**: Orchestrates the application components and handles shutdown

## Error Handling

The application includes comprehensive error handling:
- API connection errors
- Data processing errors
- Shutdown on keyboard interrupt

## Logging

Logs are written to both:
- Console (stdout)
- File (`logs/app.log`)

## Contributing

Feel free to submit issues and enhancement requests!