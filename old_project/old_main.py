from player import Playerfrom data import all_playersfrom data import players_list# how many players?print("The amount of players on the team:")print(len(all_players))print("")# print some playertarget_player = all_players[0]print("Requested player of the New York Yankees:")print(target_player.first.title()+" "+target_player.last.title())print("")# prompt for input players# this example only shows the information of the players if you write the whole name of the playersrequest_player = input("Which player are you looking for? ")user_input = request_playerfor player in players_list:    if user_input.lower() in player:        print(player)# example I have been working on"""for player in all_players:    request_player = input("Please provide the name of the player you want to look up? ")    if request_player in all_players:        print(all_players)    else:        print("No player with that name was found.")    break"""# find_player(query):# A - example query "higash", returns player with name that partially matches# B - example query "ro", returns ALL players with "ro" in their first OR last name"""Loop over players.Save all "matches" in an Arrayreturn array"""# print (avg_atbat_team[0])# avg_atbat(team)