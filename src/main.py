# Import the information of other files
from data_players import all_players # works
from player import Player

# Testing if the import of the list works
print("Lets test the array by printing the length of the list.")
print(len(all_players))

"""
Let's see which players belong to which tier in batting avg. The players will be split into three teams. Depending 
their batting avg. \n
The groups will be between .300 - .500 / .200 - .299 / .000 - .199
"""

# Adding empty lists in which the names of the players will be added to depending on their batting avg.
high_batting_avg = []
mid_batting_avg = []
low_batting_avg = []

print("_____________________________________________________")
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

print("\nHigh batting avg. .300 or more:")
for player in high_batting_avg:
    print(player)

print("\nMid batting avg. between .200 and .299:")
for player in mid_batting_avg:
    print(player)

print("\nLow batting avg. .199 or less:")
for player in low_batting_avg:
    print(player)
print("_____________________________________________________")
# The following block of code will be used for the user to provide input and to use it as a search request.

# Adding a empty list to add players that are found to it
found_players = []


def search_request():
    # Defining a function to start the search request of the user

    # Writing the request input for the user
    extension_input = "\nIf you want to quit, fill in 'q'. >>> "
    # Adding a extended part to the request for input
    request_input = input("Which player would you like to look up? Please fill in the last name of the player. " +
                          extension_input)

    # Sanitizing the input of the user
    def retry_request():
        question = input("Would you like to search for another player? y/n > ")

        for answer in question:
            if answer.lower() == 'y':
                search_request()
            elif answer.lower() == 'n':
                print("Thank you for using my services.")
            else:
                print("Program will be terminated, you did not fill in a valid answer.")
                break

    # If statement that checks what the input of the user turned out
    # In case that the user fills in 'q', the program will be stopped
    if request_input == 'q' or request_input == "":
        print("Thank you. Bye.")
    else:
        # Else: the program will concatenate through the list to
        # check  the input of the user and if it matches to any names in the list
        for item in all_players:
            if item.last in request_input.lower():
                print("Full name of player: " + item.fullname().title())
                print("Batting average: " + str(round(item.average_hit(), 3)))
                found_players.append(item.fullname().title() + " " + str(round(item.average_hit(), 3)))
                retry_request()


search_request()
# Start the function by calling it.

# The text to inform the user which players were found and added to the found list
print("The following players were found and added to the found players list: ")
for name in found_players:
    print(name)