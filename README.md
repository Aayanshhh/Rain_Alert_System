# Rain_Alert_System

#### A Python script for fetching weather data from OpenWeatherMap and sending SMS alerts via Twilio based on weather conditions.

#### Features
- **Weather Data Retrieval**: Fetches weather data (temperature, conditions) using OpenWeatherMap API.
- **SMS Alerts**: Sends SMS alerts via Twilio if it's going to rain.
- **Error Handling**: Includes robust error handling for API requests and SMS sending operations.
- **Time-based Scheduling**: Can be scheduled to run periodically to check weather conditions and send alerts.

#### Configuration
- **Location**: Modify the latitude and longitude in `main.py` to change the location for which weather data is fetched.
- **Alert Thresholds**: Customize the conditions under which alerts are triggered (e.g., temperature thresholds, weather conditions).

