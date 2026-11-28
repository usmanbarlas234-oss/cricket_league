# from dugout.loader import load_players, load_teams

# players = load_players("data/players.csv")
# teams = load_teams("data/sample_teams.csv", players)

# print(len(teams))
# for team in teams:
#     problems = team.check_rules()
#     verdict = "LEGAL" if not problems else "ILLEGAL"
#     print(team.team_name, team.owner, team.total_credits(), verdict)


from dugout.loader import load_players, load_teams
from dugout.models import League


def show_pool(players):
    """Print how many players there are per franchise and per role."""
    by_franchise = {}
    by_role = {}
    for player in players.values():
        by_franchise[player.franchise] = by_franchise.get(player.franchise, 0) + 1
        by_role[player.role] = by_role.get(player.role, 0) + 1

    print("PLAYERS BY FRANCHISE")
    for franchise in sorted(by_franchise):
        print(f"  {franchise}: {by_franchise[franchise]}")

    print("PLAYERS BY ROLE")
    for role in sorted(by_role):
        print(f"  {role}: {by_role[role]}")


def show_team(team):
    """Print one fantasy team's details."""
    print(f"\nTeam: {team.team_name} | Owner: {team.owner}")
    for player in team.players:
        print(f"  {player}")
    print(f"Total credits: {team.total_credits()}")
    print(f"Captain: {team.captain.name} | Vice-captain: {team.vice_captain.name}")


def main():
    players = load_players("data/players.csv")
    print(f"Player pool: {len(players)} players")
    show_pool(players)

    league = League("Dugout League")
    for team in load_teams("data/sample_teams.csv", players):
        show_team(team)
        problems = team.check_rules()
        if problems:
            print("ILLEGAL:")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print("LEGAL")
        league.add_team(team)

    legal = league.legal_teams()
    print(f"\nSummary: {len(legal)} legal out of {len(league.teams)} teams")


if __name__ == "__main__":
    main()