# importing the module
import wikipedia
 
# finding result for the search
# sentences = 2 refers to numbers of line
# while True:
#     q=input("You : ")
#     result = wikipedia.summary(q,sentences=3)
    
#     # printing the result
#     print("Result : ", result)

import requests

def fetch_from_google(query, api_key, engine_id):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": engine_id,
        "q": query
    }
    response = requests.get(search_url, params=params)
    data = response.json()

    if "items" in data:
        # Extract and return the first search result
        return data["items"][0]["snippet"]
        # return data
    else:
        return "Sorry, I couldn't find any relevant information."

def chat_bot(api_key, engine_id):
    print("Welcome to the chat bot! How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat bot: Goodbye!")
            break

        if "who is" in user_input.lower() or "tell me about" in user_input.lower():
            response = wikipedia.summary(user_input,sentences=3)
        
        else:
            response = fetch_from_google(user_input, api_key, engine_id)

        print("Chat bot:", response)

# Set up your API key and engine ID
api_key = "AIzaSyBVTNW1Z2VEkLcgSjW9q71hvFgu81Tlpyk"
engine_id = "4157e0d91e4b64fd5"

# Run the chat bot
chat_bot(api_key, engine_id)
