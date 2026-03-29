from data_fetcher import fetch_ticker_data
import ollama


def main():
    while True:
        user_input = input("\nEnter ticker symbol (enter 'EXIT' to exit): ")

        if user_input.strip().lower() == "exit":
            print()
            break

        print("\nGenerating response...")

        response = ollama.generate(
            model="huihui_ai/qwen3.5-abliterated:2B",
            think=True,
            stream=False,
            prompt=f"With only the following data, help me determine if this stock is a good buy or not: {(fetch_ticker_data(user_input))}. Don't say you don't know, and don't say you're not a financial advisor, just give me a solid answer in one paragraph with supporting evidence while keeping it concise and to the point. Only refer to the stock by its ticker symbol and not what you think its actual name is. Don't ask any follow-up questions and just end it off after your answer.",
            keep_alive=0,
        )

        print("\n" + response["response"])


if __name__ == "__main__":
    main()
