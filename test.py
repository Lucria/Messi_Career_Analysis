# import requests

# class FootballMatchInfo:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         self.base_url = "https://api.football-data.org/v2/"
#         self.headers = {"X-Auth-Token": api_key}

#     def get_upcoming_matches(self, team_name):
#         endpoint = f"teams/{team_name}/matches"
#         params = {"status": "SCHEDULED"}

#         response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params)

#         if response.status_code == 200:
#             matches = response.json()["matches"]
#             return matches
#         else:
#             print(f"Error: {response.status_code}")
#             return None

#     def display_match_info(self, matches):
#         if not matches:
#             print("No upcoming matches.")
#             return

#         print("Upcoming Football Matches:")
#         for match in matches:
#             home_team = match["homeTeam"]["name"]
#             away_team = match["awayTeam"]["name"]
#             date_time = match["utcDate"]

#             print(f"{home_team} vs {away_team} on {date_time}")

# if __name__ == "__main__":
#     # Get your API key from https://www.football-data.org/
#     api_key = "your_api_key_here"

#     # Example Usage
#     match_info = FootballMatchInfo(api_key)

#     # Replace "arsenal" with the desired team name (lowercase)
#     upcoming_matches = match_info.get_upcoming_matches("arsenal")

#     match_info.display_match_info(upcoming_matches)














def analyze_text(text):
  """
  This function analyzes a text and returns the number of words, vowels, and consonants.

  Args:
      text: A string containing the text to analyze.

  Returns:
      A dictionary containing the number of words, vowels, and consonants.
  """
  # Convert the text to lowercase for case-insensitive analysis
  text = text.lower()

  # Split the text into words
  words = text.split()

  # Initialize counters
  vowel_count = 0
  consonant_count = 0

  # Loop through each character in the text
  for char in text:
    # Check if character is a letter
    if char.isalpha():
      # Check for vowels
      if char in "aeiou":
        vowel_count += 1
      else:
        consonant_count += 1

  # Return the analysis results in a dictionary
  return {
    "words": len(words),
    "vowels": vowel_count,
    "consonants": consonant_count
  }

# Get text input from the user
text = input("Enter some text to analyze: ")

# Analyze the text and get results
analysis_result = analyze_text(text)

# Print the analysis results
print(f"\nAnalysis Results:")
print(f"  Number of words: {analysis_result['words']}")
print(f"  Number of vowels: {analysis_result['vowels']}")
print(f"  Number of consonants: {analysis_result['consonants']}")





