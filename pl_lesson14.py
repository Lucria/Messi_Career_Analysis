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
# ! Playground (Simple Program)
# TODO write a program to analyze text
# Count the number of words, vowels and consonants

# "I am going outside." -> 4 words, 5 vowels, ?? consonants
# Vowels is aeiou
# Consonants are just everything else that is an alphabet

"I am going outside"
# Quick Two Line Codes
countOfWords = len("I am going outside.".split())
print("Count of Words in the given Sentence:", countOfWords)

# TODO fix logic
countOfVowels = 0
for character in "I am going outside":
    countOfVowels += len(character.split())
print("Count of Vowels in the given Sentence:", countOfVowels)
countOfConsonants = 0
countOfConsonants += len(character.split())

if character in "aeiou":
    print(countOfVowels)
else:
    print(countOfConsonants)



########################################################################