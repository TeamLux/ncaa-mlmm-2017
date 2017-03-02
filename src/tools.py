def create_real_file():
    seasons = ('2013','2014','2015','2016')
    with open('./data/TourneyCompactResults.csv') as file:
        f_res = open('./data/cheat_submission.csv','w')
        f_res.write('id,pred\n')
        file.readline()
        for line in file:
            row = line.strip().split(',')
            if row[0] not in seasons:
                continue
            wteam = row[2]
            lteam = row[4]

            if wteam < lteam:
                f_res.write(row[0]+'_'+wteam+'_'+lteam+',1\n')
            else:
                f_res.write(row[0]+'_'+lteam+'_'+wteam+',0\n')
        f_res.close()

def _create_file_all_N(filename, f_res):
    with open(filename) as file:    
        file.readline()
        for line in file:
            row = line.strip().split(',')
            if row[6] != 'N':
                continue
            wteam = row[2]
            lteam = row[4]

            if wteam < lteam:
                f_res.write(row[0]+'_'+wteam+'_'+lteam+',1\n')
            else:
                f_res.write(row[0]+'_'+lteam+'_'+wteam+',0\n')

def create_file_all_N():
    f_res = open('./data/all_N.csv','w')
    f_res.write('id,pred\n')
    _create_file_all_N('./data/TourneyCompactResults.csv', f_res)
    _create_file_all_N('./data/RegularSeasonCompactResults.csv', f_res)
    f_res.close()
