from dugout.loader import load_players, load_teams

players = load_players("data/players.csv")
teams = load_teams("data/sample_teams.csv", players)

print(len(teams))
for team in teams:
    problems = team.check_rules()
    verdict = "LEGAL" if not problems else "ILLEGAL"
    print(team.team_name, team.owner, team.total_credits(), verdict)