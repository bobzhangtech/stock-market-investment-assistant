import yfinance as yf


def fetch_ticker_data(ticker):
    try:
        asset = yf.Ticker(ticker.strip().upper())
        info = asset.info
        quote_type = info.get("quoteType")

        if quote_type == "EQUITY":
            analysis_data = {
                "industry": info.get("industry"),
                "sector": info.get("sector"),
                "longBusinessSummary": info.get("longBusinessSummary"),
                "overallRisk": info.get("overallRisk"),
                "previousClose": info.get("previousClose"),
                "open": info.get("open"),
                "dayLow": info.get("dayLow"),
                "dayHigh": info.get("dayHigh"),
                "beta": info.get("beta"),
                "trailingPE": info.get("trailingPE"),
                "forwardPE": info.get("forwardPE"),
                "volume": info.get("volume"),
                "averageVolume": info.get("averageVolume"),
                "averageVolume10days": info.get("averageVolume10days"),
                "bid": info.get("bid"),
                "ask": info.get("ask"),
                "marketCap": info.get("marketCap"),
                "nonDilutedMarketCap": info.get("nonDilutedMarketCap"),
                "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
                "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
                "allTimeHigh": info.get("allTimeHigh"),
                "allTimeLow": info.get("allTimeLow"),
                "priceToSalesTrailing12Months": info.get(
                    "priceToSalesTrailing12Months"
                ),
                "fiftyDayAverage": info.get("fiftyDayAverage"),
                "twoHundredDayAverage": info.get("twoHundredDayAverage"),
                "enterpriseValue": info.get("enterpriseValue"),
                "profitMargins": info.get("profitMargins"),
                "floatShares": info.get("floatShares"),
                "sharesOutstanding": info.get("sharesOutstanding"),
                "sharesShort": info.get("sharesShort"),
                "sharesShortPriorMonth": info.get("sharesShortPriorMonth"),
                "sharesPercentSharesOut": info.get("sharesPercentSharesOut"),
                "heldPercentInsiders": info.get("heldPercentInsiders"),
                "heldPercentInstitutions": info.get("heldPercentInstitutions"),
                "shortRatio": info.get("shortRatio"),
                "shortPercentOfFloat": info.get("shortPercentOfFloat"),
                "impliedSharesOutstanding": info.get("impliedSharesOutstanding"),
                "bookValue": info.get("bookValue"),
                "priceToBook": info.get("priceToBook"),
                "earningsQuarterlyGrowth": info.get("earningsQuarterlyGrowth"),
                "netIncomeToCommon": info.get("netIncomeToCommon"),
                "trailingEps": info.get("trailingEps"),
                "forwardEps": info.get("forwardEps"),
                "lastSplitFactor": info.get("lastSplitFactor"),
                "lastSplitDate": info.get("lastSplitDate"),
                "enterpriseToRevenue": info.get("enterpriseToRevenue"),
                "enterpriseToEbitda": info.get("enterpriseToEbitda"),
                "52WeekChange": info.get("52WeekChange"),
                "SandP52WeekChange": info.get("SandP52WeekChange"),
                "currentPrice": info.get("currentPrice"),
                "targetHighPrice": info.get("targetHighPrice"),
                "targetLowPrice": info.get("targetLowPrice"),
                "targetMeanPrice": info.get("targetMeanPrice"),
                "targetMedianPrice": info.get("targetMedianPrice"),
                "recommendationMean": info.get("recommendationMean"),
                "recommendationKey": info.get("recommendationKey"),
                "numberOfAnalystOpinions": info.get("numberOfAnalystOpinions"),
                "totalCash": info.get("totalCash"),
                "totalCashPerShare": info.get("totalCashPerShare"),
                "ebitda": info.get("ebitda"),
                "totalDebt": info.get("totalDebt"),
                "quickRatio": info.get("quickRatio"),
                "currentRatio": info.get("currentRatio"),
                "totalRevenue": info.get("totalRevenue"),
                "debtToEquity": info.get("debtToEquity"),
                "revenuePerShare": info.get("revenuePerShare"),
                "returnOnAssets": info.get("returnOnAssets"),
                "returnOnEquity": info.get("returnOnEquity"),
                "grossProfits": info.get("grossProfits"),
                "freeCashflow": info.get("freeCashflow"),
                "operatingCashflow": info.get("operatingCashflow"),
                "earningsGrowth": info.get("earningsGrowth"),
                "revenueGrowth": info.get("revenueGrowth"),
                "grossMargins": info.get("grossMargins"),
                "ebitdaMargins": info.get("ebitdaMargins"),
                "operatingMargins": info.get("operatingMargins"),
                "symbol": info.get("symbol"),
                "regularMarketChangePercent": info.get("regularMarketChangePercent"),
                "regularMarketPrice": info.get("regularMarketPrice"),
                "averageAnalystRating": info.get("averageAnalystRating"),
                "longName": info.get("longName"),
                "postMarketChangePercent": info.get("postMarketChangePercent"),
                "postMarketPrice": info.get("postMarketPrice"),
                "postMarketChange": info.get("postMarketChange"),
                "regularMarketChange": info.get("regularMarketChange"),
                "regularMarketDayRange": info.get("regularMarketDayRange"),
                "averageDailyVolume3Month": info.get("averageDailyVolume3Month"),
                "fiftyTwoWeekLowChange": info.get("fiftyTwoWeekLowChange"),
                "fiftyTwoWeekLowChangePercent": info.get(
                    "fiftyTwoWeekLowChangePercent"
                ),
                "fiftyTwoWeekRange": info.get("fiftyTwoWeekRange"),
                "fiftyTwoWeekHighChange": info.get("fiftyTwoWeekHighChange"),
                "fiftyTwoWeekHighChangePercent": info.get(
                    "fiftyTwoWeekHighChangePercent"
                ),
                "fiftyTwoWeekChangePercent": info.get("fiftyTwoWeekChangePercent"),
                "epsTrailingTwelveMonths": info.get("epsTrailingTwelveMonths"),
                "epsForward": info.get("epsForward"),
                "epsCurrentYear": info.get("epsCurrentYear"),
                "priceEpsCurrentYear": info.get("priceEpsCurrentYear"),
                "fiftyDayAverageChange": info.get("fiftyDayAverageChange"),
                "fiftyDayAverageChangePercent": info.get(
                    "fiftyDayAverageChangePercent"
                ),
                "twoHundredDayAverageChange": info.get("twoHundredDayAverageChange"),
                "twoHundredDayAverageChangePercent": info.get(
                    "twoHundredDayAverageChangePercent"
                ),
                "trailingPegRatio": info.get("trailingPegRatio"),
                "historical_price": asset.history(period="1y", interval="1mo")[
                    "Close"
                ].to_markdown(),
            }
            return analysis_data

        if quote_type == "ETF":
            analysis_data = {
                "longBusinessSummary": info.get("longBusinessSummary"),
                "previousClose": info.get("previousClose"),
                "open": info.get("open"),
                "dayLow": info.get("dayLow"),
                "dayHigh": info.get("dayHigh"),
                "trailingPE": info.get("trailingPE"),
                "volume": info.get("volume"),
                "regularMarketVolume": info.get("regularMarketVolume"),
                "averageVolume": info.get("averageVolume"),
                "averageVolume10days": info.get("averageVolume10days"),
                "averageDailyVolume10Day": info.get("averageDailyVolume10Day"),
                "bid": info.get("bid"),
                "ask": info.get("ask"),
                "bidSize": info.get("bidSize"),
                "askSize": info.get("askSize"),
                "yield": info.get("yield"),
                "totalAssets": info.get("totalAssets"),
                "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
                "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
                "allTimeHigh": info.get("allTimeHigh"),
                "allTimeLow": info.get("allTimeLow"),
                "fiftyDayAverage": info.get("fiftyDayAverage"),
                "twoHundredDayAverage": info.get("twoHundredDayAverage"),
                "navPrice": info.get("navPrice"),
                "ytdReturn": info.get("ytdReturn"),
                "beta3Year": info.get("beta3Year"),
                "threeYearAverageReturn": info.get("threeYearAverageReturn"),
                "fiveYearAverageReturn": info.get("fiveYearAverageReturn"),
                "symbol": info.get("symbol"),
                "postMarketChangePercent": info.get("postMarketChangePercent"),
                "postMarketPrice": info.get("postMarketPrice"),
                "postMarketChange": info.get("postMarketChange"),
                "regularMarketChange": info.get("regularMarketChange"),
                "regularMarketDayRange": info.get("regularMarketDayRange"),
                "averageDailyVolume3Month": info.get("averageDailyVolume3Month"),
                "fiftyTwoWeekLowChange": info.get("fiftyTwoWeekLowChange"),
                "fiftyTwoWeekLowChangePercent": info.get(
                    "fiftyTwoWeekLowChangePercent"
                ),
                "fiftyTwoWeekRange": info.get("fiftyTwoWeekRange"),
                "fiftyTwoWeekHighChange": info.get("fiftyTwoWeekHighChange"),
                "fiftyTwoWeekHighChangePercent": info.get(
                    "fiftyTwoWeekHighChangePercent"
                ),
                "fiftyTwoWeekChangePercent": info.get("fiftyTwoWeekChangePercent"),
                "trailingThreeMonthReturns": info.get("trailingThreeMonthReturns"),
                "trailingThreeMonthNavReturns": info.get(
                    "trailingThreeMonthNavReturns"
                ),
                "netAssets": info.get("netAssets"),
                "epsTrailingTwelveMonths": info.get("epsTrailingTwelveMonths"),
                "bookValue": info.get("bookValue"),
                "fiftyDayAverageChange": info.get("fiftyDayAverageChange"),
                "fiftyDayAverageChangePercent": info.get(
                    "fiftyDayAverageChangePercent"
                ),
                "twoHundredDayAverageChange": info.get("twoHundredDayAverageChange"),
                "twoHundredDayAverageChangePercent": info.get(
                    "twoHundredDayAverageChangePercent"
                ),
                "netExpenseRatio": info.get("netExpenseRatio"),
                "priceToBook": info.get("priceToBook"),
                "regularMarketChangePercent": info.get("regularMarketChangePercent"),
                "regularMarketPrice": info.get("regularMarketPrice"),
                "longName": info.get("longName"),
                "trailingPegRatio": info.get("trailingPegRatio"),
                "historical_price": asset.history(period="1y", interval="1mo")[
                    "Close"
                ].to_markdown(),
            }
            return analysis_data

        if quote_type == "CRYPTOCURRENCY":
            analysis_data = {
                "description": info.get("description"),
                "previousClose": info.get("previousClose"),
                "open": info.get("open"),
                "dayLow": info.get("dayLow"),
                "dayHigh": info.get("dayHigh"),
                "regularMarketPreviousClose": info.get("regularMarketPreviousClose"),
                "regularMarketOpen": info.get("regularMarketOpen"),
                "regularMarketDayLow": info.get("regularMarketDayLow"),
                "regularMarketDayHigh": info.get("regularMarketDayHigh"),
                "volume": info.get("volume"),
                "regularMarketVolume": info.get("regularMarketVolume"),
                "averageVolume": info.get("averageVolume"),
                "averageVolume10days": info.get("averageVolume10days"),
                "averageDailyVolume10Day": info.get("averageDailyVolume10Day"),
                "marketCap": info.get("marketCap"),
                "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow"),
                "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh"),
                "allTimeHigh": info.get("allTimeHigh"),
                "allTimeLow": info.get("allTimeLow"),
                "fiftyDayAverage": info.get("fiftyDayAverage"),
                "twoHundredDayAverage": info.get("twoHundredDayAverage"),
                "volume24Hr": info.get("volume24Hr"),
                "volumeAllCurrencies": info.get("volumeAllCurrencies"),
                "circulatingSupply": info.get("circulatingSupply"),
                "maxSupply": info.get("maxSupply"),
                "totalSupply": info.get("totalSupply"),
                "fullyDilutedValue": info.get("fullyDilutedValue"),
                "volume24HrMarketCapPercent": info.get("volume24HrMarketCapPercent"),
                "symbol": info.get("symbol"),
                "regularMarketChange": info.get("regularMarketChange"),
                "regularMarketDayRange": info.get("regularMarketDayRange"),
                "averageDailyVolume3Month": info.get("averageDailyVolume3Month"),
                "fiftyTwoWeekLowChange": info.get("fiftyTwoWeekLowChange"),
                "fiftyTwoWeekLowChangePercent": info.get(
                    "fiftyTwoWeekLowChangePercent"
                ),
                "fiftyTwoWeekRange": info.get("fiftyTwoWeekRange"),
                "fiftyTwoWeekHighChange": info.get("fiftyTwoWeekHighChange"),
                "fiftyTwoWeekHighChangePercent": info.get(
                    "fiftyTwoWeekHighChangePercent"
                ),
                "fiftyTwoWeekChangePercent": info.get("fiftyTwoWeekChangePercent"),
                "longName": info.get("longName"),
                "regularMarketChangePercent": info.get("regularMarketChangePercent"),
                "regularMarketPrice": info.get("regularMarketPrice"),
                "fiftyDayAverageChange": info.get("fiftyDayAverageChange"),
                "fiftyDayAverageChangePercent": info.get(
                    "fiftyDayAverageChangePercent"
                ),
                "twoHundredDayAverageChange": info.get("twoHundredDayAverageChange"),
                "twoHundredDayAverageChangePercent": info.get(
                    "twoHundredDayAverageChangePercent"
                ),
                "historical_price": asset.history(period="1y", interval="1mo")[
                    "Close"
                ].to_markdown(),
            }
            return analysis_data

    except Exception as e:
        return f"Error: {e}"
