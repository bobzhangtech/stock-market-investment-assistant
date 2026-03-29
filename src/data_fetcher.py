import yfinance as yf


def fetch_ticker_data(ticker):
    try:
        asset = yf.Ticker(ticker.strip().upper())

        analysis_data = {
            "info": asset.info,
            "historical_price": asset.history(period="1y", interval="1mo")["Close"],
        }

        return analysis_data

    except Exception as e:
        return f"Error: {e}"
