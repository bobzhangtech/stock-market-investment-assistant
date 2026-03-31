import ollama
from src.data_fetcher import fetch_ticker_data
import urllib.request
import subprocess
import time


def ensure_ollama_running():
    try:
        urllib.request.urlopen("http://localhost:11434", timeout=2)
        return None
    except Exception:
        process = subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        for _ in range(30):
            time.sleep(1)
            try:
                urllib.request.urlopen("http://localhost:11434", timeout=2)
                return process
            except Exception:
                continue

        print("Warning: Could not start Ollama. Make sure it is installed.")
        return None


def main():
    ollama_process = ensure_ollama_running()

    while True:
        user_input = input("\nEnter ticker symbol (enter 'EXIT' to exit): ").strip()

        if user_input.lower() == "exit":
            if ollama_process:
                ollama_process.terminate()
            print()
            break

        if not user_input:
            print("\nPlease enter a ticker symbol.")
            continue

        print("\nFetching data and generating response...")

        ticker_data = fetch_ticker_data(user_input)

        if ticker_data is None:
            print(
                f"\n'{user_input.upper()}' is not a recognized equity, ETF, or cryptocurrency. Please check the ticker symbol and try again."
            )
            continue

        if isinstance(ticker_data, str) and ticker_data.startswith("Error:"):
            print(
                f"\nCould not retrieve data for '{user_input.upper()}'. Please check the ticker symbol and try again."
            )
            continue

        response = ollama.generate(
            model="ministral-3:3b",
            prompt="You are a stock market investment assistant. With the provided data, help me determine if the stock/ETF/cryptocurrency is a good buy or not. Give me a definitive answer in a single paragraph with supporting evidence while keeping it concise and to the point. If any part of the data is empty or returns none, it only means the data is not documented and doesn't mean the asset is not performing well in that regard. Don't ask any follow-up questions and just end it off after your answer."
            + str(ticker_data),
            keep_alive=0,
            options={
                "num_ctx": 8192,
            },
        )

        print("\n" + response["response"])


if __name__ == "__main__":
    main()
