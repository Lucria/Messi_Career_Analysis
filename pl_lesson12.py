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
# ! Playground (Encapsulation)
# Private (__) -> Protected (_) -> Public

# class BankAccount:
#   def __init__(self, balance=0, name="Adwaita", pin=873821):
#     # Private attribute (using double underscores)
#     self.__balance = balance
#     self.name = name # This is a public attribute
#     self.__pin = pin

#   def get_balance(self):
#     # Public method to access balance indirectly
#     return self.__balance

#   def deposit(self, amount):
#     # Public method to modify balance (with validation)
#     if amount > 0:
#       self.__balance += amount
#     else:
#       print("Invalid deposit amount. Must be positive.")

#   def withdraw(self, amount):
#     # Public method to modify balance (with validation)
#     pin = int(input("Please enter your pin number."))
#     # Check input_pin with actual pin and only allow withdrawl if pin matches, else don't allow
#     if pin == self.__pin:
#         print("Correct pin!")
#     else:
#         print("Incorrect pin")
#         return

#     if amount <= self.__balance:
#       self.__balance -= amount
#       self.__withdraw_statement(amount)
#     else:
#       print("Insufficient funds. Withdrawal denied.")

#   def __withdraw_statement(self, amount):
#     # This is a private method
#     print(f"You are withdrawing {amount} dollars")

# account = BankAccount(100)
# print("Current Balance:", account.get_balance())
# account.deposit(50)
# account.withdraw(75)
# print("Current Balance:", account.get_balance())

# print(account.name)
# print(account.__balance) # This will not work
# account.__withdraw_statement() # This will not work

########################################################################