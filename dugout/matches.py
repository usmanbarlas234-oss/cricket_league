"""Reading a real match file."""

import json


def load_match(path):
    """Return one match file as a dict."""

    with open(path, encoding="utf-8") as f:
        return json.load(f)


def deliveries(match):
    """Yield every delivery as (batting_team, over_number, delivery)."""

    for innings in match["innings"]:
        for over in innings["overs"]:
            for delivery in over["deliveries"]:
                yield innings["team"], over["over"], delivery


def is_ball_faced(delivery):
    """Wides and no-balls are not balls faced, by our league rules."""

    extras = delivery.get("extras", {})

    return "wides" not in extras and "noballs" not in extras


def batter_runs(match, batter):
    """Return the runs this batter scored with the bat in this match."""

    runs = 0

    for team, over, delivery in deliveries(match):
        if delivery["batter"] == batter:
            runs = runs + delivery["runs"]["batter"]

    return runs


def batter_card(match, batter):
    """Return runs, balls faced, fours and sixes for one batter."""

    runs = 0
    balls = 0
    fours = 0
    sixes = 0

    for team, over, delivery in deliveries(match):
        if delivery["batter"] != batter:
            continue

        off_the_bat = delivery["runs"]["batter"]
        runs = runs + off_the_bat

        if is_ball_faced(delivery):
            balls = balls + 1
        if off_the_bat == 4:
            fours = fours + 1
        if off_the_bat == 6:
            sixes = sixes + 1

    return {"runs": runs, "balls": balls, "fours": fours, "sixes": sixes}

def innings_runs(match):
    """Return a dict of batting team -> total runs scored, extras included."""

    totals = {}

    for team, over, delivery in deliveries(match):
        totals[team] = totals.get(team, 0) + delivery["runs"]["total"]

    return totals


def top_scorers(match, how_many=3):
    """Return the leading run-scorers as a list of (name, runs), highest first."""

    runs = {}

    for team, over, delivery in deliveries(match):
        batter = delivery["batter"]
        runs[batter] = runs.get(batter, 0) + delivery["runs"]["batter"]

    ranked = sorted(runs.items(), key=lambda pair: pair[1], reverse=True)

    return ranked[:how_many]


def match_summary(match):
    """Return the headline facts of a match as a dict of plain values."""

    info = match["info"]
    outcome = info["outcome"]

    # A match with no result has no winner and no margin, so use .get()
    by = outcome.get("by", {})

    if "runs" in by:
        margin = f"by {by['runs']} runs"
    elif "wickets" in by:
        margin = f"by {by['wickets']} wickets"
    else:
        margin = ""

    return {
        "date": info["dates"][0],
        "teams": info["teams"],
        "venue": info["venue"],
        "winner": outcome.get("winner", "no result"),
        "margin": margin,
    }