# import json
# import requests

# # TODO display the current results for Chelsea and its position for the premier league
# # TODO Find out the scores for Chelsea vs Mancity 18 Feb

# class FootballInfo:
#     # Constructor
#     def __init__(self, api_key):
#         self.api_key = api_key
#         # https://www.football-data.org/documentation/quickstart/
#         self.base_url = "https://api.football-data.org/v4/"
#         self.headers = {"X-Auth-Token": api_key}

#     # 61 -> Chelsea
#     # Retrieves information about a specific team
#     def get_team_information(self, team_id):
#         endpoint = f"teams/{team_id}"

#         response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)

#         # TODO format this into a pretty table
#         if response.status_code == 200: # Success
#             info = response.json()
#             info_formatted_str = json.dumps(info, indent=2)
#             print(info_formatted_str)
#         else:
#             print(f"Error: {response.status_code}")

#     def get_upcoming_matches(self, team_id):
#         # https://api.football-data.org/v4/teams/86/matches?status=SCHEDULED
#         endpoint = f"teams/{team_id}/matches?status=SCHEDULED"
#         response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)


#         if response.status_code == 200: # Success
#             matches = response.json()
#             matches_formatted_str = json.dumps(matches, indent=2)
#             print(matches_formatted_str)
#         else:
#             print(f"Error: {response.status_code}")


# api_key = input("Please input your API key:")
# footballInfo = FootballInfo(api_key) # Create an object of the class FootballInfo

# # footballInfo.get_team_information("61")
# footballInfo.get_upcoming_matches("61")


########################################################################
# ! Playground (Polymorphism)
# # Length of a string
# text = "Python"
# print(len(text))  # Output: 6

# # Length of a list
# numbers = [1, 2, 3]
# print(len(numbers))  # Output: 3

def add(x, y = 0, z = 0):
    return x + y + z

# Driver code
print(add(2))
print(add(2, 3)) # Output: 5
print(add(2, 3, 4)) # Output: 9


########################################################################