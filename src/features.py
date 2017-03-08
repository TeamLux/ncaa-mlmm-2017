class Features(object):
    """docstring for features"""

    def __init__(self, team_id, team_name):
        super(Features, self).__init__()
        self.team_id = team_id
        self.team_name = team_name

        self.n_win_H = 0
        self.n_match_H = 0

        self.n_win_A = 0
        self.n_match_A = 0

        self.n_win_N = 0
        self.n_match_N = 0

        self.n_score_H = 0
        self.n_score_concede_H = 0
        self.n_period_H = 0

        self.n_score_A = 0
        self.n_score_concede_A = 0
        self.n_period_A = 0

        self.n_score_N = 0
        self.n_score_concede_N = 0
        self.n_period_N = 0

    def add_H(self, score, score_concede, period, win):
        if win:
            self.n_win_H += 1
        self.n_match_H += 1

        self.n_score_H += score
        self.n_score_concede_H += score_concede
        self.n_period_H += period

    def add_A(self, score, score_concede, period, win):
        if win:
            self.n_win_A += 1
        self.n_match_A += 1

        self.n_score_A += score
        self.n_score_concede_A += score_concede
        self.n_period_A += period

    def add_N(self, score, score_concede, period, win):
        if win:
            self.n_win_N += 1
        self.n_match_N += 1

        self.n_score_N += score
        self.n_score_concede_N += score_concede
        self.n_period_N += period

    def get_features(self):

        # a,b,c,d,e,f,g,h,i = ['Nan']*9
        a,b,c,d,e,f,g,h,i = [0]*9
        if self.n_match_H > 0:
            a = self.n_win_H/self.n_match_H
            b = self.n_score_H/self.n_period_H
            c = self.n_score_concede_H/self.n_period_H
        if self.n_match_A > 0: 
            d = self.n_win_A/self.n_match_A
            e = self.n_score_A/self.n_period_A
            f = self.n_score_concede_A/self.n_period_A
        if self.n_match_N > 0:
            g = self.n_win_N/self.n_match_N
            h = self.n_score_N/self.n_period_N
            i = self.n_score_concede_N/self.n_period_N
        return [a,b,c,d,e,f,g,h,i]



def fill_features(filename, features, years_to_consider):
    with open(filename, newline='') as file:
        file.readline()
        for line in file:
            row = line.strip().split(',')
            if int(row[0]) not in years_to_consider:
                continue
            wTeam = int(row[2])
            wScore = int(row[3])
            lTeam = int(row[4])
            lScore = int(row[5])
            period = int(row[7])/2+4

            if row[6] == 'N':
                features[wTeam].add_N(wScore, lScore, period, True)
                features[lTeam].add_N(lScore, wScore, period, False)

            elif row[6] == 'H':
                features[wTeam].add_H(wScore, lScore, period, True)
                features[lTeam].add_A(lScore, wScore, period, False)

            elif row[6] == 'A':
                features[wTeam].add_A(wScore, lScore, period, True)
                features[lTeam].add_H(lScore, wScore, period, False)

def get_features_by_team(year_to_predict=2016,n_year=3):

    #Init all team
    features = dict()
    with open('./data/Teams.csv', newline='') as file:
        file.readline()
        for line in file:
            row = line.strip().split(',')
            features[int(row[0])] = Features(int(row[0]), row[1])

    years_to_consider = set()
    for year in range(year_to_predict-n_year,year_to_predict):
        years_to_consider.add(year)
   
    fill_features('./data/RegularSeasonCompactResults.csv', features, years_to_consider)
    fill_features('./data/TourneyCompactResults.csv', features, years_to_consider)

    return features