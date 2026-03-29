import ollama
from data_fetcher import fetch_ticker_data


def main():
    while True:
        user_input = input("\nEnter ticker symbol (enter 'EXIT' to exit): ")

        if user_input.strip().lower() == "exit":
            print()
            break

        print("\nGenerating response...")

        response = ollama.generate(
            model="deepseek-r1:7b",
            prompt="You are a stock market investment assistant. With the provided data, help me determine if the stock/ETF/cryptocurrency is a good buy or not. Give me a definitive answer in a single paragraph with supporting evidence while keeping it concise and to the point. If any part of the data is empty or returns none, it only means the data is not documented and doesn't mean anything else. Don't ask any follow-up questions and just end it off after your answer."
            + f"{(fetch_ticker_data(user_input))}",
            keep_alive=0,
            options={
                "num_ctx": 10000,
            },
        )

        print("\n" + response["response"])


if __name__ == "__main__":
    main()
