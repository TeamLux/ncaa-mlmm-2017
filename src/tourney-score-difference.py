from matplotlib import pyplot

days = []
scores = []
labels = []

dates = set()

with open('./data/TourneyCompactResults.csv') as csv:
	for (index, line) in enumerate(csv):
		if index == 0:
			continue

		components = line.split(',')

		date = components[0] + '-' + components[1]

		if date not in dates:
			dates.add(date)

		day = len(dates)

		wscore = int(components[3], 10)
		lscore = int(components[5], 10)

		days.append(day)
		scores.append(wscore - lscore)

pyplot.scatter(days, scores, s=1, alpha=0.5)

pyplot.xlabel('Day')
pyplot.ylabel('Score')

pyplot.title('Tourney - Score difference')

pyplot.savefig('./plots/tourney-score-difference-plot.png', bbox_inches='tight')
