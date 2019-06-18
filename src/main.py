# Import the information of other files
from data_players import all_players # works
from player import Player

# Testing if the import of the list works
print("Let's test the array by printing the length of the list.")
print(len(all_players))

"""
Let's see which players belong to which tier in batting avg. The players will be split into three teams. Depending 
their batting avg. \n
The groups will be between .300 - .500 / .200 - .299 / .000 - .199
"""

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

def search_request():
    extension_input = ("\nIf you want to quit, fill in 'q'. >>> ")
    request_input = input("Which player would you like to look up? Please fill in the last name of the player. " +
                          extension_input)

    for item in all_players:
        if item.last in request_input.lower():
            print("Full name of player: " + item.fullname().title())
            print("Batting average: " + str(round(item.average_hit(), 3)))
            break
        elif item.last not in request_input.lower():
            print("The requested name cannot be found, please fill in a correct last name.")
            search_request()
        else:
            if request_input.lower() == 'q' or 'Q':
                break
search_request()