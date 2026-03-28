from data_fetcher import fetch_ticker_data
from ollama import chat
from ollama import ChatResponse

user_input = input("\nEnter ticker symbol: ")
print("\nGenerating response...")

response: ChatResponse = chat(
    model="huihui_ai/gemma3-abliterated:4b",
    messages=[
        {
            "role": "user",
            "content": f"With only the following data, help me determine if this stock is a good buy or not: {(fetch_ticker_data(user_input))}. Don't say you don't know, and don't say you're not a financial advisor, just give me a solid answer in one paragraph with supporting evidence while keeping it concise and to the point. Don't ask any follow-up questions and just end it off after your answer.",
        },
    ],
)

print("\n" + response["message"]["content"] + "\n")
# or access fields directly from the response object
# print(response.message.content)


def main():
    pass


if __name__ == "__main__":
    main()


def menu():
    print("Hi! I'm your stock market investment assistant!")
    print("1. Add ticker symbol")
    print("2. Remove ticker symbol")
    user_input = int(input("Please enter the number of your selection: ").strip())


def display_tickers():
    pass


def add_ticker(user_input):
    pass


def remove_ticker(user_input):
    pass
