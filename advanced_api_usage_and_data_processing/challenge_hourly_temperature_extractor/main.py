import requests

def print_first_five_paris_temperatures():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 48.85,
        "longitude": 2.35,
        "hourly": "temperature_2m"
    }
    response = requests.get(url, params=params)
    data = response.json()
    temps = data["hourly"]["temperature_2m"]      # extract full list
    first_five = temps[:5]                        # take first five
    for temp_str in first_five:                   # properly indented
        print(temp_str)

print_first_five_paris_temperatures()






