import yfinance as yf


def fetch_sp500_data():
    sp500 = yf.download("^GSPC", period="1y", interval="1d")
    sorted_sp500 = sp500.sort_index(ascending=False)
    filtered_sp500 = sorted_sp500["Close"]

    return filtered_sp500


def fetch_nasdaq_data():
    nasdaq = yf.download("^IXIC", period="1y", interval="1d")
    sorted_nasdaq = nasdaq.sort_index(ascending=False)
    filtered_nasdaq = sorted_nasdaq["Close"]

    return filtered_nasdaq


def fetch_ticker_data(ticker):
    try:
        stock = yf.Ticker(ticker.strip().upper())
        info = stock.info
        quote_type = info.get("quoteType")

        analysis_packet = {
            "symbol": ticker.strip().upper(),
            "valuation": {
                "currentPrice": info.get("currentPrice"),
                "forwardPE": info.get("forwardPE"),
                "trailingPE": info.get("trailingPE"),
                # "pegRatio": info.get("pegRatio"),
            },
            "growth_profitability": {
                "revGrowth": info.get("revenueGrowth"),
                "earningsGrowth": info.get("earningsGrowth"),
                "profitMargin": info.get("profitMargins"),
                "returnOnEquity": info.get("returnOnEquity"),
            },
            "risk_sentiment": {
                "debtToEquity": info.get("debtToEquity"),
                "beta": info.get("beta"),
                "analystTarget": info.get("targetMeanPrice"),
                "recommendation": info.get("recommendationKey"),
            },
        }
        return analysis_packet
    except Exception as e:
        return {"error": str(e)}


def fetch_ticker_news(ticker):
    news = yf.Ticker(f"{ticker.strip().upper()}").news

    if news:
        print(news[0])
