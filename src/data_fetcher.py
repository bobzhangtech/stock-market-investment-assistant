import yfinance as yf
import logging

logging.getLogger("yfinance").setLevel(logging.CRITICAL)


def fetch_ticker_data(ticker):
    try:
        asset = yf.Ticker(ticker.upper())
        info = asset.info
        quote_type = info.get("quoteType")

        if quote_type == "EQUITY":
            analysis_data = {
                "longName": info.get("longName"),
                "symbol": info.get("symbol"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "longBusinessSummary": info.get("longBusinessSummary"),
                "currentPrice": info.get("currentPrice"),
                "previousClose": info.get("previousClose"),
                "marketCap": info.get("marketCap"),
                "beta": info.get("beta"),
                "trailingPE": info.get("trailingPE"),
                "forwardPE": info.get("forwardPE"),
                "trailingPegRatio": info.get("trailingPegRatio"),
                "priceToBook": info.get("priceToBook"),
                "priceToSalesTrailing12Months": info.get(
                    "priceToSalesTrailing12Months"
                ),
                "enterpriseToRevenue": info.get("enterpriseToRevenue"),
                "enterpriseToEbitda": info.get("enterpriseToEbitda"),
                "trailingEps": info.get("trailingEps"),
                "forwardEps": info.get("forwardEps"),
                "earningsGrowth": info.get("earningsGrowth"),
                "earningsQuarterlyGrowth": info.get("earningsQuarterlyGrowth"),
                "revenueGrowth": info.get("revenueGrowth"),
                "totalRevenue": info.get("totalRevenue"),
                "grossMargins": info.get("grossMargins"),
                "operatingMargins": info.get("operatingMargins"),
                "profitMargins": info.get("profitMargins"),
                "returnOnAssets": info.get("returnOnAssets"),
                "returnOnEquity": info.get("returnOnEquity"),
                "ebitda": info.get("ebitda"),
                "revenuePerShare": info.get("revenuePerShare"),
                "bookValue": info.get("bookValue"),
                "totalCashPerShare": info.get("totalCashPerShare"),
                "freeCashflow": info.get("freeCashflow"),
                "operatingCashflow": info.get("operatingCashflow"),
                "totalCash": info.get("totalCash"),
                "totalDebt": info.get("totalDebt"),
                "debtToEquity": info.get("debtToEquity"),
                "currentRatio": info.get("currentRatio"),
                "dividendYield": info.get("dividendYield"),
                "dividendRate": info.get("dividendRate"),
                "payoutRatio": info.get("payoutRatio"),
                "volume": info.get("volume"),
                "averageVolume": info.get("averageVolume"),
                "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
                "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
                "fiftyDayAverage": info.get("fiftyDayAverage"),
                "twoHundredDayAverage": info.get("twoHundredDayAverage"),
                "shortPercentOfFloat": info.get("shortPercentOfFloat"),
                "heldPercentInsiders": info.get("heldPercentInsiders"),
                "heldPercentInstitutions": info.get("heldPercentInstitutions"),
                "recommendationKey": info.get("recommendationKey"),
                "targetMedianPrice": info.get("targetMedianPrice"),
                "numberOfAnalystOpinions": info.get("numberOfAnalystOpinions"),
                "historical_price": asset.history(period="1y", interval="1mo")[
                    "Close"
                ].to_markdown(),
            }
            return analysis_data

        if quote_type == "ETF":
            analysis_data = {
                "longName": info.get("longName"),
                "symbol": info.get("symbol"),
                "category": info.get("category"),
                "fundFamily": info.get("fundFamily"),
                "longBusinessSummary": info.get("longBusinessSummary"),
                "previousClose": info.get("previousClose"),
                "navPrice": info.get("navPrice"),
                "totalAssets": info.get("totalAssets"),
                "trailingPE": info.get("trailingPE"),
                "yield": info.get("yield"),
                "netExpenseRatio": info.get("netExpenseRatio"),
                "beta3Year": info.get("beta3Year"),
                "ytdReturn": info.get("ytdReturn"),
                "threeYearAverageReturn": info.get("threeYearAverageReturn"),
                "fiveYearAverageReturn": info.get("fiveYearAverageReturn"),
                "volume": info.get("volume"),
                "averageVolume": info.get("averageVolume"),
                "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
                "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
                "fiftyDayAverage": info.get("fiftyDayAverage"),
                "twoHundredDayAverage": info.get("twoHundredDayAverage"),
                "historical_price": asset.history(period="1y", interval="1mo")[
                    "Close"
                ].to_markdown(),
            }
            return analysis_data

        if quote_type == "CRYPTOCURRENCY":
            analysis_data = {
                "longName": info.get("longName"),
                "symbol": info.get("symbol"),
                "description": info.get("description"),
                "regularMarketPrice": info.get("regularMarketPrice"),
                "previousClose": info.get("previousClose"),
                "marketCap": info.get("marketCap"),
                "volume24Hr": info.get("volume24Hr"),
                "volume": info.get("volume"),
                "averageVolume": info.get("averageVolume"),
                "circulatingSupply": info.get("circulatingSupply"),
                "maxSupply": info.get("maxSupply"),
                "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
                "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
                "fiftyDayAverage": info.get("fiftyDayAverage"),
                "twoHundredDayAverage": info.get("twoHundredDayAverage"),
                "historical_price": asset.history(period="1y", interval="1mo")[
                    "Close"
                ].to_markdown(),
            }
            return analysis_data

    except Exception as e:
        return f"Error: {e}"
