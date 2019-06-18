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
