IoT Temperature Tweeter -  Arduino + Python + Twitter API

This project reads temperature data from an LM35 sensor using Arduino Mega and automatically tweets the live temperature using a Python script and Twitter API.
A perfect beginner-friendly IoT + Python + API integration project

#Project Overview:
This system works in 3 steps:
Arduino Mega reads temperature from the LM35 sensor
Sends temperature values to Python through Serial (COM Port)
Python program tweets the temperature using Twitter (X) API v2

#Components Used:

-Hardware
Arduino Mega (or Uno)
LM35 Temperature Sensor
Jumper Wires
USB Cable

-Software
Python 3.13+
Tweepy Library (Twitter API)
python-dotenv (for securely loading API keys)
PySerial (for reading Arduino data)

#Arduino Wiring:
| LM35 Pin | Arduino Pin |
| -------- | ----------- |
| + (VCC)  | 5V          |
| OUT      | A0          |
| – (GND)  | GND         |

#How It Works:
Arduino continuously prints temperature readings via Serial.
Python listens to the COM port.
Each new reading is sent to Twitter as a tweet.
Uses Twitter API v2

#Install required libraries:
-pip install tweepy python-dotenv pyserial

#Running the Project
Upload Arduino code
Check COM port (Device Manager → Ports)
Update COM port in Python script
Run: python tweet_temp.py

#License
MIT License
