# Stock Market Investment Assistant

## Purpose
I'm building this project to help me in keeping up with the market and index changes, in order to allow me to make better decisions in stock investments. 

I feel like the actual stock trading action probably can't be automated, and a stock market prediction tool is out of my skill level currently, so for now the main feature would be achieved by using existing free APIs to grab stock, index, and market data periodically, adding them into a database for tracking and logging, and automatically pushing the information inferred from these data onto my phone through one of those bot services. 

## Functions
* Track popular market indexes such as the NASDAQ and S&P
* Grab the latest stock market news
* Automated daily reminders and summaries
* (Optional) Relate the news and market/company research to the user's portfolio and give suggestions (may be difficult to achieve)

## Free Tech Stack
* Language: Python
* Market data: yfinance
* Database: SQLite
* Bot platform: Telegram
* Automation: GitHub Actions
* (Optional) AI analysis: Google AI Studio or GroqCloud free tier