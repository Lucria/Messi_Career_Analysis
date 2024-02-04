import requests

# TODO display the current results for Chelsea and its position for the premier league
# TODO Find out the scores for Chelsea vs Mancity 18 Feb

class FootballInfo:
    def __init__(self, api_key):
        self.api_key = api_key
        # https://www.football-data.org/documentation/quickstart/
        self.base_url = "https://api.football-data.org/v4/"
        self.headers = {"X-Auth-Token": api_key}

    # 61 -> Chelsea
    # Retrieves information about a specific team
    def get_team_information(self, team_id):
        endpoint = f"teams/{team_id}"

        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers)

        if response.status_code == 200: # Success
            matches = response.json()
            print(matches)
        else:
            print(f"Error: {response.status_code}")


    # TODO check all the upcoming matches for Chelsea 61
    def get_upcoming_matches(self, team_id):
        print("UNDONE")



api_key = input("Please input your API key:")
footballInfo = FootballInfo(api_key) # Create an object of the class FootballInfo
footballInfo.get_team_information("61")


########################################################################
# ! Playground

# class Fruit:
#     # Constructor
#     def __init__(self, name, color, taste):
#         self.name = name
#         self.color = color
#         self.taste = taste

#     def display_info(self):
#         print(f"{self.name.capitalize()} is a {self.color} fruit with a {self.taste} taste.")

# # Child class - Inherits from parent class Fruit
# class TropicalFruit(Fruit):
#     def display_info(self):
#         super().display_info()
#         print(f"This is a tropical fruit")

# # Example usage:
# apple = Fruit("apple", "red", "sweet")
# banana = Fruit("banana", "yellow", "sweet and creamy")
# orange = Fruit("orange", "orange", "citrusy")
# mango = TropicalFruit("mango", "yellow", "sweet")

# # Display information about the fruits
# apple.display_info()
# banana.display_info()
# orange.display_info()
# mango.display_info()

########################################################################