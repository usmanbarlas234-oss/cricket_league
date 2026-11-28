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