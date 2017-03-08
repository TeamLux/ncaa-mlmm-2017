from features import get_features_by_team

countNan = 0
def fill_XY(res, filename, feat, year):
    global countNan
    with open(filename, newline='') as file:
        file.readline()
        for line in file:
            row = line.strip().split(',')
            if int(row[0]) != year:# or row[6] != 'N':
                continue
            wTeam = int(row[2])
            lTeam = int(row[4])

            if 'Nan' in (feat[wTeam]+feat[lTeam]):
                countNan += 1
                continue

            if wTeam < lTeam:
                res[year]['X'].append(feat[wTeam]+feat[lTeam])
                res[year]['Y'].append(1)
                res[year]['teams'].append([filename,year,wTeam,lTeam])
            else:
                res[year]['X'].append(feat[lTeam]+feat[wTeam])
                res[year]['Y'].append(0)
                res[year]['teams'].append([filename,year,lTeam,wTeam])


def get_XY_by_year(nYear = 1):
    res = dict()
    for year in range(1985+nYear,2017):
        print(year)
        temp = get_features_by_team(year, nYear)
        feat = dict()
        for key in temp:
            feat[key] = temp[key].get_features()
        res[year] = {'X': list(), 'Y': list(), 'teams': list()}
        fill_XY(res, './data/RegularSeasonCompactResults.csv', feat, year)
        fill_XY(res, './data/TourneyCompactResults.csv', feat, year)
    print(countNan)
    return res
