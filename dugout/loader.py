import csv

from dugout.models import Player


def load_players(path):
    """Return a dict: player_id -> Player."""
    players = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            player = Player.from_row(row)
            players[player.player_id] = player
    return players