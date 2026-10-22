import requests
import streamlit as st

st.title("Weather API Demo")

# Retrieve API key from Streamlit secrets (or fallback to demo_key)
API_KEY = st.secrets.get("API_KEY", "demo_key")

city = st.text_input("Enter city", "Chennai")

if st.button("Get Weather"):
    resp = None

    # Fetch live weather data if a valid API key is present
    if API_KEY != "demo_key":
        try:
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(url, params=params, timeout=5)

            if response.status_code == 200:
                data = response.json()
                resp = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "condition": data["weather"][0]["main"],
                    "humidity": data["main"]["humidity"],
                }
            else:
                st.error(f"Error fetching weather data: {response.json().get('message', 'Unknown error')}")
        except Exception as e:
            st.error(f"Request failed: {e}")

    # Fallback to simulated response if demo_key is used or call fails
    if resp is None:
        if API_KEY == "demo_key":
            st.info("Using simulated data (Demo Mode). Add a valid API_KEY to .streamlit/secrets.toml for live results.")
        resp = {
            "city": city,
            "temperature": 30,
            "condition": "Sunny",
            "humidity": 65,
        }

    # Display JSON payload
    st.json(resp)

    # Display Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Temperature", f"{resp['temperature']}°C")
    c2.metric("Condition", resp["condition"])
    c3.metric("Humidity", f"{resp['humidity']}%")

st.markdown("---")
st.subheader("HTTP Methods")
st.markdown("""
- **GET** - Retrieve data
- **POST** - Send data
- **PUT** - Update data
- **DELETE** - Delete data
""")

# Exercise 1: Real Weather API (OpenWeather)

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

resp = requests.get(url, params=params).json()

# Exercise 2: Error Handling

try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    resp = r.json()
except requests.exceptions.Timeout:
    st.error("Request timed out. Try again.")
except requests.exceptions.HTTPError as e:
    st.error(f"HTTP error: {e}")
except Exception as e:
    st.error(f"Something went wrong: {e}")

# Exercise 3: Loading Spinner

with st.spinner("Fetching weather..."):
    resp = requests.get(url, params=params, timeout=10).json()
