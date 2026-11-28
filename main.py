# from dugout.loader import load_players
# from dugout.models import FantasyTeam

# players = load_players("data/players.csv")

# # A legal team
# ids = ["P122", "P089", "P056", "P037", "P065", "P028",
#        "P068", "P066", "P140", "P069", "P101"]
# team = FantasyTeam("Lahore Thunder", "Usman")
# for player_id in ids:
#     team.add_player(players[player_id])
# team.set_captain(players["P089"], players["P068"])

# print(team)
# print("Errors:", team.check_rules())

# # An illegal team (only 3 players)
# short = FantasyTeam("Too Short", "Test")
# for player_id in ["P089", "P068", "P122"]:
#     short.add_player(players[player_id])
# short.set_captain(players["P089"], players["P068"])

# print()
# print(short)
# for error in short.check_rules():
#     print(" -", error)


# from dugout.loader import load_players, load_team

# players = load_players("data/players.csv")
# team = load_team("data/my_team.csv", players)

# print(team)
# print("Captain:", team.captain)
# print("Vice-captain:", team.vice_captain)
# print("Errors:", team.check_rules())

# from dugout.loader import load_players, load_team
# from dugout.models import FantasyTeam, find_player
# from dugout.errors import PlayerNotFoundError, InvalidTeamError

# players = load_players("data/players.csv")

# 1. My real team passes validation
# team = load_team("data/my_team.csv", players)
# team.validate()
# print("Legal team:", team)

# # 2. A player id that does not exist
# try:
#     find_player(players, "P999")
# except PlayerNotFoundError as error:
#     print("Caught:", error)

# # 3. An illegal team
# short = FantasyTeam("Too Short", "Test")
# short.add_player(players["P089"])
# try:
#     short.validate()
# except InvalidTeamError as error:
#     print("Caught:", error)
#     print("Number of problems:", len(error.problems))

from dugout.loader import load_players, load_team
from dugout.models import FantasyTeam, League

players = load_players("data/players.csv")

league = League("Dugout League")
league.add_team(load_team("data/my_team.csv", players))

short = FantasyTeam("Too Short", "Test")
short.add_player(players["P089"])
short.set_captain(players["P089"], players["P068"])
league.add_team(short)

print(len(league.teams))
print(league.find_team("Usman"))
print(league.find_team("Nobody"))

print("Legal teams:")
for team in league.legal_teams():
    print(" ", team.team_name)

print("Ranked (cheapest first):")
for team in league.rank_teams():
    print(" ", team.team_name, team.total_credits())