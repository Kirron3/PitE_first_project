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
│   └── app.log            # Log file
├── src/
│   ├── main.py          # Main entry point
│   ├── config.py        # Configuration management
│   ├── data.py          # Data fetching
│   └── processor.py     # Data processing
```

## Requirements

- Python 3.7+
- Required packages:
  - requests
  - pyyaml

## Installation

1. Create the project structure:
```bash
mkdir -p project/src project/config
```

2. Install dependencies:
```bash
pip install requests pyyaml
```

## Usage

1. Start the monitor:
```bash
python src/main.py
```

2. Stop the monitor:
   - Press `CTRL+C` to shutdown gracefully

## Configuration

The `config/config.yaml` file contains:
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

- **main.py**: Entry point and application orchestration
- **data.py**: Handles cryptocurrency price fetching
- **processor.py**: Processes prices and calculates changes
- **config.py**: Manages configuration loading

## Error Handling

The application includes error handling for:
- API connection issues
- Data processing errors
- Graceful shutdown on CTRL+C

## Logging

Logs are written to both console and file, which are automatically created in the project directory.

## Contributing

Feel free to submit issues and enhancement requests!