from dugout.matches import load_match, deliveries

match = load_match("data/matches/match_01.json")

print(list(match.keys()))
print(match["info"]["teams"])
print(match["info"]["venue"])
print(len(match["innings"]), "innings")
print(len(match["innings"][0]["overs"]), "overs in the first")

count = 0
for team, over, delivery in deliveries(match):
    count = count + 1

print(count, "deliveries in the match")