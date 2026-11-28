
from dugout.errors import InvalidTeamError, PlayerNotFoundError
from dugout.loader import (
    load_players,
    load_team,
    load_teams,
    read_team_rows,
    team_from_row,
)
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
def report(team_name, problems):
    """Print one verdict. An empty list of problems means the team is legal."""
    if not problems:
        print(f"  {team_name}: LEGAL")
        return

    print(f"  {team_name}: REJECTED")
    for problem in problems:
        print(f"    - {problem}")


def report_on_row(row, players):
    """Build one team from a CSV row and say whether it is legal."""
    try:
        team = team_from_row(row, players)
        team.validate()
    except PlayerNotFoundError as error:
        report(row["team_name"], [str(error)])
    except InvalidTeamError as error:
        report(error.team_name, error.problems)
    else:
        report(team.team_name, [])

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

    league.add_team(my_team)

    print("\n===== LEAGUE TABLE (cheapest first) =====")
    for team in league.rank_teams():
        verdict = "LEGAL" if not team.check_rules() else "ILLEGAL"
        print(f"{team.team_name:<18} {team.owner:<14} {team.total_credits():>6}  {verdict}")


    print("\nThe six teams the league office could not accept")
    for row in read_team_rows("data/bad_teams.csv"):
        report_on_row(row, players)

    print("\nDone. Six teams were refused and the program did not crash.")




if __name__ == "__main__":
    main()