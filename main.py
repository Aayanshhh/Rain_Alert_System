import os
import requests
from twilio.rest import Client

# Fetch API keys from environment variables
api_key = os.getenv("WEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

if not api_key or not account_sid or not auth_token:
    raise ValueError("Please set the environment variables for API keys and tokens")

# Fetch weather data
try:
    response = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/forecast",
        params={"lat": 28.704060, "lon": 77.102493, "cnt": 4, "appid": api_key}
    )
    response.raise_for_status()
    weather_data = response.json()
except requests.RequestException as e:
    print(f"Error fetching weather data: {e}")
    weather_data = None

if weather_data:
    # Check if it will rain
    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
            break

    if will_rain:
        # Send SMS using Twilio
        try:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body="It's going to rain today. Remember to bring an Umbrella.",
                from_='+12765657787',
                to='+917007400374'
            )
            print(message.status)
        except Exception as e:
            print(f"Error sending SMS: {e}")
else:
    print("Failed to retrieve weather data.")
