import yfinance as yf

# Fetch the data of the S&P 500 and NASDAQ indices
indices = yf.download("^GSPC ^IXIC", period="1y", interval="1d")
sorted_indices = indices.sort_index(ascending=False)
filtered_indices = sorted_indices["Close"]

selected_data = filtered_indices.iloc[0, [0, 1]]


def fetch_ticker_data(ticker):
    data = yf.Ticker(f"{ticker.strip().upper()}")
    info = data.info
    revenue_growth = info.get("revenueGrowth")  # Look for consistent top-line growth
    earnings_growth = info.get(
        "earningsGrowth"
    )  # Look for consistent bottom-line growth
    balance_sheet = (
        data.balance_sheet
    )  # Shows assets, liabilities, shareholders' equity
    profit_margins = info.get("profitMargins")  # Look for high profit margins
    cash_flow = data.cashflow  # Look for consistent cash flow
    # Competitive advantage (moat)
    operating_margins = info.get("operatingMargins")  # Look for high operating margins
    return_on_invested_capital = info.get(
        "returnOnInvestedCapital"
    )  # Look for high ROIC
    debt_to_equity = info.get("debtToEquity")  # Look for low debt to equity


def fetch_ticker_news(ticker):
    news = yf.Ticker(f"{ticker.strip().upper()}").news

    if news:
        print(news[0])
