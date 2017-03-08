from data import get_XY_by_year
from features import get_features_by_team
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn import svm

def get_teams_id(year):
    teams_id = list()
    with open('./data/TourneyCompactResults.csv', newline='') as file:
        file.readline()
        for line in file:
            row = line.strip().split(',')
            if int(row[0]) != year:
                continue
            wTeam = int(row[2])
            lTeam = int(row[4])
            if wTeam not in teams_id:
                teams_id.append(wTeam)
            if lTeam not in teams_id:
                teams_id.append(lTeam)
    return sorted(teams_id)


nYear = 3
clf = svm.SVC(probability=True)
# clf = tree.DecisionTreeClassifier()
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
XY = get_XY_by_year(nYear)
X = list()
Y = list()
for year in XY:
    if year >= 2013:
        continue
    X += XY[year]['X']
    Y += XY[year]['Y']

clf = clf.fit(X, Y)

f_res = open('./data/tmp.csv','w')
f_res.write('id,pred\n')

for year in range(2013, 2017):
    temp = get_features_by_team(year, nYear)
    teams_id = get_teams_id(year)
    feat = dict()
    for key in temp:
        feat[key] = temp[key].get_features()
    X = list()
    IDs = list()
    for i in range(len(teams_id)):
        for j in range(i+1,len(teams_id)):
            X.append(feat[teams_id[i]]+feat[teams_id[j]])
            IDs.append(str(year)+'_'+str(teams_id[i])+'_'+str(teams_id[j]))
    prob = clf.predict_proba(X)
    for i in range(len(IDs)):
        f_res.write(IDs[i]+','+str(prob[i][1])+'\n')

f_res.close()
