import math
import csv


def create_real_file():
    seasons = ('2013','2014','2015','2016')
    with open('./data/TourneyCompactResults.csv') as f:
        f_res = open('./data/cheat_submission.csv','w')
        f_res.write('id,pred\n')
        reader = csv.reader(f)
        for row in reader:
            if row[0] not in seasons:
                continue
            wteam = row[2]
            lteam = row[4]

            if wteam < lteam:
                f_res.write(row[0]+'_'+wteam+'_'+lteam+',1\n')
            else:
                f_res.write(row[0]+'_'+lteam+'_'+wteam+',0\n')
        f_res.close()


def logloss(y_pred, y_real):
    if y_pred == y_real:
        return 0
    return y_real*math.log(y_pred)+(1-y_real)*math.log(1-y_pred)


def evaluate(filename_to_evaluate):
    res = 0
    n = 0
    to_evaluate = dict()
    with open(filename_to_evaluate) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'id':
                to_evaluate[row[0]] = float(row[1])

    with open('./data/cheat_submission.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != 'id':
                res += logloss(to_evaluate[row[0]],float(row[1]))
                n+=1
    return -res/n


if __name__ == '__main__':
    pass