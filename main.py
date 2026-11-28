from dugout.loader import load_players, load_team, load_teams
from dugout.models import League
from dugout.rules import MAX_CREDITS


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


def show_verdict(team):
    """Print LEGAL, or ILLEGAL followed by every problem."""
    problems = team.check_rules()
    if problems:
        print("ILLEGAL:")
        for problem in problems:
            print(f"  - {problem}")
    else:
        print("LEGAL")


def main():
    players = load_players("data/players.csv")
    print(f"Player pool: {len(players)} players")
    show_pool(players)

    league = League("Dugout League")
    for team in load_teams("data/sample_teams.csv", players):
        show_team(team)
        show_verdict(team)
        league.add_team(team)

    legal = league.legal_teams()
    illegal = len(league.teams) - len(legal)
    print(f"\nSummary: {len(legal)} legal, {illegal} illegal out of {len(league.teams)} teams")

    print("\n===== MY TEAM =====")
    my_team = load_team("data/my_team.csv", players)
    show_team(my_team)
    print(f"Credits left: {MAX_CREDITS - my_team.total_credits()}")
    show_verdict(my_team)


if __name__ == "__main__":
    main()