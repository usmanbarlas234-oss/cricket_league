from dugout.loader import load_players
from dugout.models import FantasyTeam

players = load_players("data/players.csv")

# A legal team
ids = ["P122", "P089", "P056", "P037", "P065", "P028",
       "P068", "P066", "P140", "P069", "P101"]
team = FantasyTeam("Lahore Thunder", "Usman")
for player_id in ids:
    team.add_player(players[player_id])
team.set_captain(players["P089"], players["P068"])

print(team)
print("Errors:", team.check_rules())

# An illegal team (only 3 players)
short = FantasyTeam("Too Short", "Test")
for player_id in ["P089", "P068", "P122"]:
    short.add_player(players[player_id])
short.set_captain(players["P089"], players["P068"])

print()
print(short)
for error in short.check_rules():
    print(" -", error)