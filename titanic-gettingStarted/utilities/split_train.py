





infile = open('/home/ameert/git_projects/kaggle_competitions/titanic-gettingStarted/data/train_original.csv')

outfile_train = open('/home/ameert/git_projects/kaggle_competitions/titanic-gettingStarted/data/train.csv', 'w')

outfile_survived = open('/home/ameert/git_projects/kaggle_competitions/titanic-gettingStarted/data/train_survived.csv', 'w')

for row in infile.readlines():
    row = row.strip().split(',')
    outfile_survived.write(row[1]+'\n')
    outfile_train.write(','.join([row[0],]+row[2:]) +'\n')
outfile_train.close()
outfile_survived.close()
