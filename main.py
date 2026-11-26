# from dugout.models import Player

# babar = Player("P089", "Babar Azam", "Peshawar Zalmi", "BAT", 10.5)
# print(babar)


from dugout.models import Player, FantasyTeam

babar = Player("P089", "Babar Azam", "Peshawar Zalmi", "BAT", 10.5)
shaheen = Player("P068", "Shaheen Shah Afridi", "Lahore Qalandars", "BOWL", 10.5)
rizwan = Player("P122", "Mohammad Rizwan", "Rawalpindiz", "WK", 10.5)

team = FantasyTeam("Lahore Thunder", "Usman")
team.add_player(babar)
team.add_player(shaheen)
team.add_player(rizwan)
team.set_captain(babar, shaheen)

print(team)
print(team.total_credits())
print(team.count_by_role())
print(team.count_by_franchise())
print(team.captain)