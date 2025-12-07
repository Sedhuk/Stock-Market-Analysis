# Streamlit Stock Dashboard

A Streamlit app for exploring stock OHLCV data, analyzing performance, volatility, sector trends, and more.

## Features
1. Filtered Stock Data Viewer
   - Select stocks by ticker
   - Filter by month
   - View full OHLCV data in an interactive table

2. Top 10 Yearly Gainers & Losers
   - Calculates yearly returns from closing prices
   - Dynamic bar charts for best and worst performers

3. Top 10 Most Volatile Stocks
   - Volatility calculated as the standard deviation of daily returns
   - Bar chart highlighting the riskiest stocks

4. Cumulative Return Trend
   - Line chart showing cumulative returns over time
   - Compare multiple stocks

5. Sector-wise Performance
   - Merge tickers with sector data
   - Show sector-level average yearly performance

6. Monthly Gainers & Losers
   - Select a month to view top 5 gainers and top 5 losers

7. Correlation Heatmap
   - Heatmap of correlations between closing prices
   - Useful for portfolio diversification analysis

## Project Structure
```
streamlit-stock-dashboard/
├── app.py                # Main Streamlit application
├── data/
│   ├── stock_data.csv    # Daily stock OHLCV data
│   └── sector_data.csv   # Ticker → sector mapping
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation
```

## Installation & Setup (Windows)
1. Clone the repository
```bash
git clone <repo-url>
cd streamlit-stock-dashboard
```

2. Create and activate a virtual environment (Windows)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell
# or
.venv\Scripts\activate.bat   # cmd
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app
```bash
streamlit run app.py
```

## Required Python Libraries
Add at least the following to requirements.txt:
```
streamlit
pandas
numpy
plotly
yfinance
```
(Adjust as needed for your project.)

## Data Processing (formulas)
- Daily return:
  - daily_return = (Close_today - Close_yesterday) / Close_yesterday
- Yearly return:
  - yearly_return = (Last_Close_of_Year - First_Close_of_Year) / First_Close_of_Year
- Volatility:
  - volatility = standard deviation of daily returns
- Cumulative return (preferred multiplicative approach):
  - cumulative_return = (1 + daily_return).cumprod() - 1

## Available Dashboards
- Filter Stock Data — Shows dataset for selected filters  
- Yearly Gainers — Top 10 best performers  
- Yearly Losers — Top 10 worst performers  
- Volatility — Most volatile stocks by daily-return stddev  
- Cumulative Return — Multi-stock performance trend  
- Sector Analysis — Average yearly return by sector  
- Monthly Gainers/Losers — Top monthly performers

## Data Files
- data/stock_data.csv — daily OHLCV with Date and Ticker columns  
- data/sector_data.csv — mapping of Ticker → Sector for sector-level analysis

## Notes & Best Practices
- Parse date columns as datetime and sort by date before calculating returns.  
- Use the multiplicative cumulative return formula to account for compounding.  
- Handle missing trading days (weekends/holidays) when computing returns.

## Future Enhancements
- Multi-year sector comparison  
- Portfolio comparison (allocation-based metrics)  
- Forecasting with ARIMA / Prophet  
- Real-time stock updates (websockets/streaming)