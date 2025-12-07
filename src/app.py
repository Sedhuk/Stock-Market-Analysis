import streamlit as st
import pandas as pd
import mysql.connector as mc
import plotly.express as px

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Data-Driven Stock Analysis",
    layout="wide"
)

st.title("📊 Nifty 50 — Data-Driven Stock Analysis Dashboard")
st.markdown("Visualizing stock performance over the past year with charts and filters.")

# -------------------------
# Database Connection
# -------------------------
def get_db_connection():
    try:
        conn = mc.connect(
            host="localhost",
            user="root",
            password="Sedhu.k001@",
            database="stock_data"
        )
        return conn
    except mc.Error as e:
        st.error(f"Database connection error: {e}")
        return None

@st.cache_data
def load_data():
    conn = get_db_connection()
    if conn is None:
        return pd.DataFrame()
    query = "SELECT * FROM stocks"
    df = pd.read_sql(query, conn)
    conn.close()
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()
if df.empty:
    st.error("No data loaded.")
else:
    st.success("Stock data loaded successfully!")

# -------------------------
# Compute Returns for all tabs
# -------------------------
df['daily_return'] = df.groupby('Ticker')['close'].pct_change()
df['yearly_return'] = df.groupby('Ticker')['close'].transform(lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0])

# -------------------------
# Tabs
# -------------------------
tabs = st.tabs([
    "Filtered Data",
    "Top Gainers & Losers",
    "Volatility",
    "Cumulative Return",
    "Sector Performance",
    "Correlation Heatmap",
    "Monthly Top 5"
])

# -------------------------
# Tab 1: Filtered Data with internal filters
# -------------------------
with tabs[0]:
    st.subheader("Filtered Stock Data")

    # Filters inside this tab
    tickers = st.multiselect(
        "Select Stock Symbol",
        options=df['Ticker'].unique(),
        default=df['Ticker'].unique()[:5]
    )
    month = st.selectbox(
        "Select Month",
        options=df['month'].unique(),
        key="filtered_data_month"
    )

    df_filtered = df[(df['Ticker'].isin(tickers)) & (df['month'] == month)]
    st.dataframe(df_filtered)

    st.download_button(
        label="Download Filtered CSV",
        data=df_filtered.to_csv(index=False),
        file_name="filtered_stocks.csv",
        mime="text/csv"
    )

# -------------------------
# Tab 2: Top 10 Gainers & Losers (Full dataset)
# -------------------------
with tabs[1]:
    st.header("📈 Top 10 Gainers & Losers (Yearly)")
    top_gainers = df[['Ticker', 'yearly_return']].drop_duplicates().sort_values('yearly_return', ascending=False).head(10)
    top_losers = df[['Ticker', 'yearly_return']].drop_duplicates().sort_values('yearly_return', ascending=True).head(10)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 10 Gainers")
        fig1 = px.bar(top_gainers, x='Ticker', y='yearly_return', title="Top 10 Best Performing Stocks")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.subheader("Top 10 Losers")
        fig2 = px.bar(top_losers, x='Ticker', y='yearly_return', title="Top 10 Worst Performing Stocks")
        st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Tab 3: Volatility
# -------------------------
with tabs[2]:
    st.header("📉 Volatility — Top 10 Most Volatile Stocks")
    volatility = df.groupby("Ticker")['daily_return'].std().sort_values(ascending=False).head(10)
    fig3 = px.bar(volatility, x=volatility.index, y=volatility.values, title="Top 10 Volatile Stocks")
    st.plotly_chart(fig3, use_container_width=True)

# -------------------------
# Tab 4: Cumulative Return
# -------------------------
with tabs[3]:
    st.header("📈 Cumulative Return Over Time")
    cum_df = df.copy()
    cum_df['daily_return'] = cum_df.groupby("Ticker")['close'].pct_change()
    cum_df['cumulative_return'] = cum_df.groupby("Ticker")['daily_return'].cumsum()
    top5 = df.groupby("Ticker")['yearly_return'].mean().sort_values(ascending=False).head(5).index
    fig4 = px.line(
        cum_df[cum_df['Ticker'].isin(top5)],
        x="date",
        y="cumulative_return",
        color="Ticker",
        title="Top 5 Stocks — Cumulative Return Over Time"
    )
    st.plotly_chart(fig4, use_container_width=True)

# -------------------------
# Tab 5: Sector Performance
# -------------------------
with tabs[4]:
    st.header("🏢 Sector-wise Average Yearly Return")
    try:
        conn = get_db_connection()
        if conn:
            sector_df = pd.read_sql("SELECT * FROM sector", conn)
            conn.close()
            sector_df['Ticker_clean'] = sector_df['symbol'].str.split(':').str[-1].str.strip()
            df_sector = df.merge(sector_df, left_on='Ticker', right_on='Ticker_clean', how='left')
            sector_perf = df_sector.groupby("sector")['yearly_return'].mean().sort_values(ascending=False)
            fig5 = px.bar(sector_perf, x=sector_perf.index, y=sector_perf.values, title="Average Yearly Return by Sector")
            st.plotly_chart(fig5, use_container_width=True)
        else:
            st.warning("Sector data not available from DB.")
    except Exception as e:
        st.warning(f"Sector-wise performance skipped: {e}")

# -------------------------
# Tab 6: Correlation Heatmap
# -------------------------
with tabs[5]:
    st.header("📊 Stock Price Correlation Heatmap")
    close_df = df.pivot(index='date', columns='Ticker', values='close')
    corr_matrix = close_df.corr()
    fig6 = px.imshow(corr_matrix,
                     labels=dict(x="Stock", y="Stock", color="Correlation"),
                     x=corr_matrix.columns,
                     y=corr_matrix.columns,
                     title="Stock Closing Price Correlation Heatmap")
    st.plotly_chart(fig6, use_container_width=True)

# -------------------------
# Tab 7: Monthly Top 5 Gainers & Losers
# -------------------------
with tabs[6]:
    st.header("📅 Monthly Top 5 Gainers & Losers")
    selected_month = st.selectbox("Select Month", options=df['month'].unique() , key="monthly_top5_month")
    df_month = df[df['month'] == selected_month].copy()
    df_month['monthly_return'] = df_month.groupby('Ticker')['close'].pct_change().fillna(0)
    monthly_return = df_month.groupby('Ticker')['monthly_return'].sum().sort_values(ascending=False)
    top5_gain = monthly_return.head(5)
    top5_loss = monthly_return.tail(5)
    col1, col2 = st.columns(2)
    with col1:
        st.write("Top 5 Gainers")
        fig_g = px.bar(top5_gain, x=top5_gain.index, y=top5_gain.values)
        st.plotly_chart(fig_g, use_container_width=True)
    with col2:
        st.write("Top 5 Losers")
        fig_l = px.bar(top5_loss, x=top5_loss.index, y=top5_loss.values)
        st.plotly_chart(fig_l, use_container_width=True)
