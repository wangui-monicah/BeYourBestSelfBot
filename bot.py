import os
import tweepy
import random
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Debugging: Print the variables to confirm they are loaded
print(f"API_KEY: {API_KEY}")
print(f"API_SECRET: {API_SECRET}")
print(f"ACCESS_TOKEN: {ACCESS_TOKEN}")
print(f"ACCESS_TOKEN_SECRET: {ACCESS_TOKEN_SECRET}")

#authenticate to twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# Fetch and display the authenticated user's details
user = api.verify_credentials()
print(f"Authenticated as: {user.name} (@{user.screen_name})")

def post_quote():    
    
    try:
        with open("quotes.txt", "r", encoding="utf-8") as file:
            quotes = file.readlines()
        quote = random.choice(quotes).strip()
        api.update_status(quote)
        print(f"Successfully quotes: {quotes}")
    except:
        print(f"An error occurred: {e}") 

schedule.every().day.at("05:30").do(post_quote)

post_quote()  # Test posting a single quote
print("Bot is running. Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(1)


post_quote()
