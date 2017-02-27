from matplotlib import pyplot

days = []
fieldShots = []
threeShots = []
freeShots = []
labels = []

dates = set()
colors = {
	'W': 0.33,
	'L': 0.66
}

with open('./data/RegularSeasonDetailedResults.csv') as csv:
	for (index, line) in enumerate(csv):
		if index == 0:
			continue

		components = line.split(',')

		date = components[0] + '-' + components[1]

		if date not in dates:
			dates.add(date)

		day = len(dates)

		wFieldShotsRatio = int(components[8], 10) / float(max(int(components[9], 10), 1))
		wThreeShotsRatio = int(components[10], 10) / float(max(int(components[11], 10), 1))
		wFreeShotsRatio = int(components[12], 10) / float(max(int(components[13], 10), 1))

		lFieldShotsRatio = int(components[21], 10) / float(max(int(components[22], 10), 1))
		lThreeShotsRatio = int(components[23], 10) / float(max(int(components[24], 10), 1))
		lFreeShotsRatio = int(components[25], 10) / float(max(int(components[26], 10), 1))

		days.append(day)
		fieldShots.append(wFieldShotsRatio)
		threeShots.append(wThreeShotsRatio)
		freeShots.append(wFreeShotsRatio)
		labels.append(colors['W'])

		days.append(day)
		fieldShots.append(lFieldShotsRatio)
		threeShots.append(lThreeShotsRatio)
		freeShots.append(lFreeShotsRatio)
		labels.append(colors['L'])

pyplot.scatter(days, fieldShots, s=1, c=labels, alpha=0.5)

pyplot.xlabel('Day')
pyplot.ylabel('Field Shot Ratio')

pyplot.title('Season - Field Shot Ratio')

pyplot.savefig('./plots/season-field-shot-ratio-plot.png', bbox_inches='tight')

pyplot.clf()

pyplot.scatter(days, threeShots, s=1, c=labels, alpha=0.5)

pyplot.xlabel('Day')
pyplot.ylabel('Three Pointer Ratio')

pyplot.title('Season - Three Pointer Ratio')

pyplot.savefig('./plots/season-three-pointer-ratio-plot.png', bbox_inches='tight')


pyplot.clf()

pyplot.scatter(days, freeShots, s=1, c=labels, alpha=0.5)

pyplot.xlabel('Day')
pyplot.ylabel('Free Shot Ratio')

pyplot.title('Season - Free Shot Ratio')

pyplot.savefig('./plots/season-free-shot-ratio-plot.png', bbox_inches='tight')
