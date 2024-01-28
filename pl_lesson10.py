import requests

api_key = input("Please input your API key:")
# Docs: https://www.football-data.org/documentation/quickstart/
base_url = "https://api.football-data.org/v4/"
headers = {"X-Auth-Token": api_key}

# TODO check all the upcoming matches for Chelsea 61
# TODO display the current results for Chelsea and its position for the premier league
# TODO Find out the scores for Chelsea vs Mancity 18 Feb
endpoint = f"teams/61"

# https://api.football-data.org/v4/teams
# requests is a HTTP library for Python.
# requests.get()
# requests.post()
# requests.put()
# requests.delete()
response = requests.get(f"{base_url}{endpoint}", headers=headers)

if response.status_code == 200: # Success
    matches = response.json()
    print(matches)
else:
    print(f"Error: {response.status_code}")

