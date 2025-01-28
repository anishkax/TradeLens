# FinReport: Explainable Stock Earnings Forecasting via News Factor Analyzing Model
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/finreport-explainable-stock-earnings/stock-market-prediction-on-astock)](https://paperswithcode.com/sota/stock-market-prediction-on-astock?p=finreport-explainable-stock-earnings)

TradeLens
TradeLens is a stock market analysis tool that combines data processing, technical indicators, and sentiment analysis to predict market trends. This project is designed to process large datasets, analyze stock performance, and assist in making informed investment decisions.

# TradeLens: Stock Market Analysis and Prediction System

## Overview

TradeLens is a robust stock market analysis and prediction tool designed to analyze financial data, including historical stock prices, news sentiment, and technical indicators. It integrates with news articles and stock data, processing them to generate insights for better decision-making in trading.

## Features

- **Stock Data Processing**: Ingests stock price data and processes it with technical indicators like moving averages, RSI, MACD, and more.
- **News Sentiment Analysis**: Analyzes and integrates news sentiment to correlate with stock market movements.
- **Prediction Models**: Uses machine learning algorithms for stock price prediction based on historical data and sentiment analysis.
- **CSV Data Input/Output**: Easily processes and outputs stock data in CSV format for further analysis or usage in other systems.

## Key Components

1. **Data Ingestion**: 
   - The system accepts CSV files containing stock data with columns like `open`, `high`, `low`, `close`, and `volume`.
   - Technical indicators and other transformations are added to the raw data.

2. **News Integration**:
   - The tool uses news articles to extract relevant stock-related information.
   - Sentiment analysis helps in understanding the market's emotional response to news.

3. **Prediction Model**:
   - Machine learning models are applied to predict future stock prices or trends based on historical data.

4. **CSV Export**:
   - Processed data and predictions are exported back into CSV files for further use.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Required Python Libraries:
  - `pandas`
  - `stockstats`
  - `tqdm`
  - `sklearn` (for model building)
