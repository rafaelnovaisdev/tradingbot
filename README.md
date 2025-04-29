# Trading Bot

This repository contains the source code for a trading bot platform. The platform supports data ingestion, model training, signal generation, and trade execution.

## Directory Structure

```
trading-bot/
├── data-ingestion/
│   ├── stocks/
│   │   ├── download_daily_prices.py
│   ├── news/
│   │   ├── scrape_news.py
│   ├── macro/
│   │   ├── fetch_fred_data.py
│   └── __init__.py
├── models/
│   ├── mean_reversion/
│   │   ├── train_model.py
│   │   ├── backtest_strategy.py
│   ├── momentum/
│   │   ├── detect_momentum.py
│   └── __init__.py
├── signal-generation/
│   ├── generate_signals.py
├── execution/
│   ├── execute_trades.py
├── utils/
│   ├── db_connection.py
│   ├── logger.py
│   ├── config.yaml
│   └── __init__.py
├── requirements.txt
├── Jenkinsfile
├── README.md
└── LICENSE
```

## Features

- **Data Ingestion**: Fetches stock prices, news, and macroeconomic data.
- **Models**: Implements trading strategies, including mean reversion and momentum detection.
- **Signal Generation**: Converts model outputs into actionable trading signals.
- **Execution**: Executes trades based on generated signals.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/rafaelnovaisdev/trading-bot.git
   cd trading-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the environment:
   - Edit `utils/config.yaml` to set up database and API keys.

4. Run scripts:
   - Example: To download daily prices:
     ```bash
     python data-ingestion/stocks/download_daily_prices.py
     ```

## License

This project is licensed under the [MIT License](LICENSE).