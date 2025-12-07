# Stock Analysis Dashboard

A comprehensive data analysis and visualization system for Nifty 50 stocks. The system processes historical stock data from YAML files, performs data cleaning and transformation, stores data in a SQL database, and provides interactive visualizations through a Streamlit dashboard.

## Features

- Extract and transform stock data from YAML files
- Data cleaning and validation
- MySQL database storage
- Performance analysis (top/worst performers)
- Volatility analysis
- Cumulative returns tracking
- Sector-wise performance analysis
- Correlation analysis
- Monthly trend analysis
- Interactive Streamlit dashboard

## Project Structure

```
stock-analysis-dashboard/
├── .env.example          # Environment configuration template
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── app.py              # Main Streamlit application
├── config/             # Configuration files
├── src/                # Source code
│   ├── data_extraction.py
│   ├── data_cleaning.py
│   ├── database.py
│   ├── analysis.py
│   ├── visualization.py
│   └── utils.py
├── tests/              # Test files
├── scripts/            # Utility scripts
├── raw_data/           # Raw YAML data files
└── refined_data/       # Processed CSV files
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd stock-analysis-dashboard
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment

Copy `.env.example` to `.env` and update with your configuration:

```bash
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac
```

Edit `.env` file with your database credentials and paths.

### 6. Set up MySQL database

```sql
CREATE DATABASE stock_data;
```

### 7. Run the application

```bash
streamlit run app.py
```

## Testing

Run all tests:

```bash
pytest tests/ -v
```

Run tests with coverage:

```bash
pytest tests/ -v --cov=src
```

Run property-based tests:

```bash
pytest tests/test_properties.py -v
```

## Usage

1. **Data Processing**: Extract and clean data from YAML files
2. **Database Loading**: Load processed data into MySQL database
3. **Dashboard**: Launch Streamlit dashboard to explore visualizations
4. **Analysis**: View performance, volatility, sector analysis, and more

## Requirements

- Python 3.8+
- MySQL/MariaDB 8.0+
- 50 Nifty stocks data in YAML format
- Sector mapping CSV file

## License

This project is for educational and analysis purposes.

## Contributing

Contributions are welcome! Please follow the existing code structure and add tests for new features.
