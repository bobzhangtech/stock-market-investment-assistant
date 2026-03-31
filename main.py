import ollama
from src.data_fetcher import fetch_ticker_data


def main():
    while True:
        user_input = input("\nEnter ticker symbol (enter 'EXIT' to exit): ").strip()

        if user_input.lower() == "exit":
            print()
            break

        if not user_input:
            print("Please enter a ticker symbol.")
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
            prompt="You are a stock market investment assistant. With the provided data, help me determine if the stock/ETF/cryptocurrency is a good buy or not. Give me a definitive answer in a single paragraph with supporting evidence while keeping it concise and to the point. If any part of the data is empty or returns none, it only means the data is not documented and doesn't mean anything else. Don't ask any follow-up questions and just end it off after your answer."
            + str(ticker_data),
            keep_alive=0,
            options={
                "num_ctx": 10000,
            },
        )

        print("\n" + response["response"])


if __name__ == "__main__":
    main()
