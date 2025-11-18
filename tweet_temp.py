import serial
import time
from dotenv import load_dotenv
import os
import tweepy

# Load API keys from .env
load_dotenv()

api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate using Twitter API
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Set correct COM port 
ser = serial.Serial('COM5', 9600)
time.sleep(2)

while True:
    try:
        raw_value = ser.readline().decode().strip()
        temperature = float(raw_value)

        tweet = f"Current room temperature: {temperature:.2f}°C"
        client.create_tweet(text=tweet)

        print("Tweet Sent:", tweet)
        time.sleep(10)  

    except Exception as e:
        print("Error:", e)
