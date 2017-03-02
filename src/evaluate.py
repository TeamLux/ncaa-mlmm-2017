import math

def logloss(y_pred, y_real):
    if y_pred == y_real:
        return 0
    return y_real*math.log(y_pred)+(1-y_real)*math.log(1-y_pred)


def evaluate(filename_to_evaluate):
    res = 0
    n = 0
    to_evaluate = dict()
    with open(filename_to_evaluate) as file:
        file.readline()
        for line in file:
            row = line.strip().split(',')
            if row[0] != 'id':
                to_evaluate[row[0]] = float(row[1])

    with open('./data/cheat_submission.csv') as file:
        file.readline()
        for line in file:
            row = line.strip().split(',')
            res += logloss(to_evaluate[row[0]],float(row[1]))
            n+=1
    return -res/n


if __name__ == '__main__':
    pass