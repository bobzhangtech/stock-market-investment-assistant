# Stock Market Investment Assistant

## Purpose
I built this project to help me easily analyze various investment metrics to better determine if a particular stock, ETF, or cryptocurrency is a good buy or not. 

## Function
* The data fetcher grabs real-time data of various metrics such as the P/E ratio from Yahoo Finance through the yfinance library, and also historical monthly prices of the past year
* The program calls a local AI model via Ollama and runs both the data and custom instructions through it
* After processing, the program outputs a concise paragraph of investment advice

## Free Tech Stack
* Programming language: Python
* Market data: yfinance
* AI analysis: Ministral 3 8B via Ollama

## How To Use
1. Install [Ollama](https://ollama.com)
2. Open terminal and run `ollama`
3. Install Ministral 3 8B by running `ollama pull ministral-3:8b`
4. Download source code from GitHub
5. Download packages in `requirements.txt` with `pip install -r requirements.txt` (assuming you already have Python installed)
6. Run `main.py`