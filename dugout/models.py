from dugout.rules import (
    check_players_count,
    check_budget,
    check_franchise_limit,
    check_roles,
    check_captains,
)

class Player:
    """One real cricketer in the PSL player list."""

    def __init__(self, player_id, name, franchise, role, credits):
        self.player_id = player_id
        self.name = name
        self.franchise = franchise
        self.role = role
        self.credits = credits

    @classmethod
    def from_row(cls, row):
        """Build a Player from one row (dict) of the players CSV."""
        return cls(
            row["player_id"],
            row["name"],
            row["franchise"],
            row["role"],
            float(row["credits"]),
        )

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"


class FantasyTeam:
    """A fantasy XI picked by one person."""

    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
        total = 0
        for player in self.players:
            total = total + player.credits
        return total

    def count_by_role(self):
        counts = {"WK": 0, "BAT": 0, "AR": 0, "BOWL": 0}
        for player in self.players:
            counts[player.role] = counts[player.role] + 1
        return counts

    def count_by_franchise(self):
        counts = {}
        for player in self.players:
            counts[player.franchise] = counts.get(player.franchise, 0) + 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain
    def check_rules(self):
        """Return a list of rule violations. An empty list means the team is legal."""
        errors = []
        errors.extend(check_players_count(self))
        errors.extend(check_budget(self))
        errors.extend(check_franchise_limit(self))
        errors.extend(check_roles(self))
        errors.extend(check_captains(self))
        return errors


    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner: {self.owner}, {size} players, {cost} cr)"