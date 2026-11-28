import csv
import json
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

def read_team_rows(path):
    """Return the raw rows of a teams CSV file, without building any teams."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
def read_team_entries(path):
    """Return the raw entries of a teams JSON file, without building any teams."""

    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_teams_json(path, teams):
    """Write a list of FantasyTeams to a JSON file."""

    data = [team.to_dict() for team in teams]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_teams_json(path, players):
    """Return a list of FantasyTeams read from a JSON file."""

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return [FantasyTeam.from_dict(entry, players) for entry in data]