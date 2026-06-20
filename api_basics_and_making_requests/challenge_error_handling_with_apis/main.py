import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()             # <-- might raise ValueError
        print(data["fact"])
    except Exception:
        print("Failed to retrieve cat fact.")

get_cat_fact()
