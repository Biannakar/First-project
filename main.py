from prettytable import PrettyTable
import local
x = PrettyTable()
x.field_names = [local.team, local.plays, local.wins, local.draws, local.loses, local.washers, local.missed, local.points]
a = int(input(local.number))
for i in range(a):
    team = str(input(local.name))
    games = int(input(local.games))
    clogged = 0
    missing = 0
    wins = 0
    draws = 0
    loses = 0
    points = 0
    for k in range(games):
        score = (input(local.scores))
        goals = score.split(':')
        if goals[0] > goals[1]:
            points += 2
            wins += 1
        elif goals[0] == goals[1]:
            points += 1
            draws += 1
        else:
            points += 0
            loses += 1
        clogged += int(goals[0])
        missing += int(goals[1])
    x.add_row([team, games, wins,draws,loses, clogged, missing, points])
x.sortby =  local.points
x.reversesort = True
print(x)