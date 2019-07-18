# Import the information of other files
from data_players import all_players # works
from player import Player
import time

# to do: let's give the user the possibility to choose a certain function
# The user can choose from:
# Displaying_averages -> This will show all the players and their averages
# Display_average_groups -> This will show all the groups in which the players are listed in(depending on their average)
# Search_request -> This will prompt the user to provide the program with input to search for a specific player

# Functions needed for the whole program

# Function to print out the whole team and their individual stats
def display_averages():
    for player in all_players:
        print("\t* Full name of the player is: {}".format(player.fullname().title()))
        print("\t* Batting Average: {}".format(round(player.average_hit(), 3)))
        print("\t* Position: {}".format(player.position().upper()))
        print("\t* Team: {}".format(player.team_group().upper()))
        print("\n")
    main_menu_func()
"""
Let's see which players belong to which tier in batting avg. The players will be split into three teams. Depending 
their batting avg. \n
The groups will be between .300 - .500 / .200 - .299 / .000 - .199
"""

# Creating empty lists/ categories
high_batting_avg = []
mid_batting_avg = []
low_batting_avg = []

# Create an empty list to place found players
found_players = []

# The next for loop will add players to the top tier list of "high, mid or low batting averages"
for player in all_players:
    average_hitting = player.average_hit()
    name_hitter = player.fullname()
    if average_hitting >= 0.300:
        high_batting_avg.append(str(round(average_hitting, 3)) + " " + name_hitter.title())
    elif average_hitting <= 0.199:
        low_batting_avg.append(str(round(average_hitting, 3)) + " " + name_hitter.title())
    else:
        mid_batting_avg.append(str(round(average_hitting, 3)) + " " + name_hitter.title())

# The continue request for the user
def continue_request():
    category_continue = input("Would you like to continue? (Y/N)")
    if category_continue.lower() == "y":
        category_input()
    elif category_continue.lower() == "n":
        print("I understand, you will be redirected to the Main Menu.")
        main_menu_func()
    else:
        print("No valid answer was given, please do so.")
        main_menu_func()

# The function for the second
def category_input():
    print("""
    The following categories are available:
    1. High Batting Averages
    2. Mid Batting Averages
    3. Low Batting Averages
    4. All Categories
    5. Quit
    """)

# Asking the user which category he/she would want to see
    category_request = input("Which category would you like to see? ")
    category_request = int(category_request)
    # If-statement to use the user's answer for the category to show
    if category_request == 1:
        print("\nHigh batting avg. .300 or more:")
        for player in high_batting_avg:
            print(player)
        # Asking the user if they want to continue
        continue_request()
    elif category_request == 2:
        print("\nMid batting avg. between .200 and .299:")
        for player in mid_batting_avg:
            print(player)
        continue_request()
    elif category_request == 3:
        print("\nLow batting avg. .199 or less:")
        for player in low_batting_avg:
            print(player)
        continue_request()
    elif category_request == 4:
        print("\nHigh batting avg. .300 or more:")
        for player in high_batting_avg:
            print(player)
        print("\nMid batting avg. between .200 and .299:")
        for player in mid_batting_avg:
            print(player)
        print("\nLow batting avg. .199 or less:")
        for player in low_batting_avg:
            print(player)
        continue_request()
    elif category_request == 5:
        print("I understand, this service will stop")
    else:
        print("No valid answer was given, please do so.")
        category_input()
    # Redirecting the user back to the Main Menu
    main_menu_func()

# Category 3: The search request function for the user
def search_request():
    # Defining a retry_request function to ask the user if they want to look for another player after a search
    def retry_request():
        question = input("Would you like to search for another player? y/n > ")
        if question.lower() == 'y':
            search_request()
        elif question.lower() == 'n':
            print("Thank you for using my services.")
        else:
            print("Program will be terminated, you did not fill in a valid answer.")

    # Asking the user for input regarding the name and informing the player how to quit in case they want to
    quit_service = "If you want to quit the service fill in Q...\n> "
    question_user = input("Which player would you like to look up? Please fill in the last name of the player. "
                          + quit_service)

    # Sanitizing the input of the user
    if question_user.lower() == "q" or question_user == "":
        print("I understand, this service will be stopped.")
    # In case the
    else:
        for item in all_players:
            if item.last in question_user.lower():
                print("Full name of player: " + item.fullname().title())
                print("Batting average: " + str(round(item.average_hit(), 3)))
                found_players.append(item.fullname().title() + " " + str(round(item.average_hit(), 3)))
        retry_request()




# First: Get the user's name
name = input("Welcome, what is your name? ")

# Extra check to see if the user has typed in a valid name
if len(name) == 0:
    print("That's not a valid name please type your name correctly.")
    retry_naming = input("What is your name? ")
else:
    greeting = ("Welcome {}, you will be soon prompted to choose between certain options in the main menu."
                .format(name.title()))
    print("\n" + greeting)

# Adding a time function to give a more interactive show to the user
time.sleep(3)

# Show the main menu
print("""
\nThis is the Main Menu. In here you will find the three functions this program has to offer. A HELP-menu will follow 
later. Please feel free to look around.
""")


# Main menu options
def main_menu_func():
    main_menu_request = input("""
    Which function-service would you like to use? Choose between the numbers given per option.
    1. Display Averages of Players
    2. Display Averages in Categories
    3. Search for a player specifically
    4. Quit
    > """)
    main_menu_request = int(main_menu_request)
    if main_menu_request == 1:
        print("You have chosen for option 1: Display Averages of Players.")
        time.sleep(1)
        print("Here is the requested list of players of the team.")
        display_averages()
    elif main_menu_request == 2:
        print("You have chosen for option 2: Display Averages in Categories.")
        time.sleep(1)
        category_input()
    elif main_menu_request == 3:
        print("You have chosen for option 3: Search for a player specifically.")
        time.sleep(1)
        search_request()
        print("The following players were found and added to the found players list: ")
        for player in found_players:
            print(player)
        print("You will now be redirected to the Main Menu.")
        main_menu_func()
    elif main_menu_request == 4:
        print("I understand. This service will be terminated")
        pass
    else:
        print("No valid answer was given, please do so.")
        continue_request()


main_menu_func()
