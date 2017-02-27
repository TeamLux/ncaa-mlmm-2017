from matplotlib import pyplot

days = []
scores = []
labels = []

dates = set()
colors = {
	'H': 0.33,
	'A': 0.66,
	'N': 0.99
}

with open('./data/RegularSeasonCompactResults.csv') as csv:
	for (index, line) in enumerate(csv):
		if index == 0:
			continue

		components = line.split(',')

		date = components[0] + '-' + components[1]

		if date not in dates:
			dates.add(date)

		day = len(dates)

		wscore = int(components[3], 10)
		wlocation = components[6]

		lscore = int(components[5], 10)
		llocation = (
			'N'
			if wlocation == 'N'
				else 'H'
					if wlocation == 'A'
					else 'A'
		)

		days.append(day)
		scores.append(wscore)
		labels.append(colors[wlocation])

		days.append(day)
		scores.append(lscore)
		labels.append(colors[llocation])

pyplot.scatter(days, scores, s=1, c=labels, alpha=0.5)

pyplot.xlabel('Day')
pyplot.ylabel('Score')

pyplot.title('Season - Score by location')

pyplot.savefig('./plots/season-score-by-location-plot.png', bbox_inches='tight')
