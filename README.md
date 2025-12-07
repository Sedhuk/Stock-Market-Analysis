🚀 Features
1. Filtered Stock Data Viewer

Select stocks by ticker

Filter by month

View full OHLCV data in an interactive table

2. Top 10 Yearly Gainers & Losers

Automatically calculates yearly returns from closing prices

Dynamic bar charts for best and worst-performing stocks

3. Top 10 Most Volatile Stocks

Volatility calculated using standard deviation of daily returns

Bar chart highlighting the riskiest stocks

4. Cumulative Return Trend

Line chart showing cumulative returns over time

Supports comparison of multiple stocks

5. Sector-wise Performance

Merges stock tickers with sector data

Shows sector-level average yearly performance

6. Monthly Gainers & Losers

Select a month and instantly view:

Top 5 gainers

Top 5 losers

7. Correlation Heatmap

Displays a heatmap of correlations between closing prices

Helpful for portfolio diversification analysis

📁 Project Structure
📦 streamlit-stock-dashboard
│
├── app.py                # Main Streamlit application
├── data/
│   ├── stock_data.csv    # Daily stock OHLCV data
│   └── sector_data.csv   # Ticker-to-sector mapping
│
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation

🛠️ Installation & Setup
1. Clone the Repository
git clone <repo-url>
cd streamlit-stock-dashboard

2. Install Dependencies
pip install -r requirements.txt

3. Run the Streamlit App
streamlit run app.py

📦 Required Python Libraries

Your requirements.txt should contain:

streamlit
pandas
numpy
plotly
yfinance


(Add/remove based on your project)

📊 How the Data Is Processed
Daily Returns

Calculated using:

daily_return = (Close_today - Close_yesterday) / Close_yesterday

Yearly Return
yearly_return = (Last_Close_of_Year - First_Close_of_Year) / First_Close_of_Year

Volatility
volatility = standard deviation of all daily returns

Cumulative Return
cumulative_return = cumulative sum of daily returns

🌐 Available Dashboards
Dashboard Section	Description
Filter Stock Data	Shows full dataset for selected filters
Yearly Gainers	Top 10 best performers
Yearly Losers	Top 10 worst performers
Volatility	Most volatile stocks
Cumulative Return	Multi-stock performance trend
Sector Analysis	Avg yearly return by sector
Monthly Gainers/Losers	Monthly performers
⭐ Future Enhancements

Multi-year sector comparison

Portfolio comparison module

Forecasting with ARIMA/Prophet

Real-time live stock updates