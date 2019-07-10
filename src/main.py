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

# adding a empty list to add players that are found to it
found_players = []

def search_request():


    extension_input = ("\nIf you want to quit, fill in 'q'. >>> ")
    request_input = input("Which player would you like to look up? Please fill in the last name of the player. " +
                          extension_input)
    #sanatized input (variabel aanmaken)
    # list maken van matches en die daar in stoppen, vervolgens dit uitprinten
    # als len > 0: dan block of code vervolgen


    def retry_request():
        question = input("Would you like to search for another player? y/n > ")

        for answer in question:
            if answer.lower() == 'y':
                search_request()
            elif answer.lower() == 'n':
                print("Thank you for using my services.")
            else:
                print("Program will be stopped because you did not fill in a valid answer.")
                break



    if request_input == 'q'or request_input == "":
        print("Thank you. Bye.")
    else:
        for item in all_players:
            if item.last in request_input.lower():
                print("Full name of player: " + item.fullname().title())
                print("Batting average: " + str(round(item.average_hit(), 3)))
                found_players.append(item.fullname().title())
                retry_request()
            # else:
            # print("Player not found.")
    #     elif request_input.lower() == 'q':
    #         break
    #     else:
    #         print("No player with that last name was found.")
    #         break

search_request()


# The text to inform the user which players were found and added to the found list
print("The following players were found and added to the found players list: ")
for name in found_players:
    print(name)