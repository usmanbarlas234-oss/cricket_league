import csv

from dugout.models import Player, FantasyTeam, find_player


def load_players(path):
    """Return a dict: player_id -> Player."""
    players = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            player = Player.from_row(row)
            players[player.player_id] = player
    return players


def team_from_row(row, players):
    """Build one FantasyTeam from a row of a teams CSV."""
    team = FantasyTeam(row["team_name"], row["owner"])
    for player_id in row["players"].split(";"):
        team.add_player(find_player(players, player_id.strip()))
    team.set_captain(
        find_player(players, row["captain"]),
        find_player(players, row["vice_captain"]),
    )
    return team


def load_team(path, players):
    """Return the first team in a teams CSV file."""
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            return team_from_row(row, players)

def load_teams(path, players):
    """Return a list of every team in a teams CSV file."""
    teams = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            teams.append(team_from_row(row, players))
    return teams