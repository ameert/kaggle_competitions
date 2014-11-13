import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv('./data/train_original.csv', index_col=0, header=0)

print train
print np.sum(train['Age'].isnull())

good_cabins = train['Cabin'].isnull()==0

cabins = train[['Survived','Pclass','Fare','Cabin']]
cabins= cabins[good_cabins]

deckmap = {'A':1, 'B':2,'C':3, 'D':4,'E':5, 'F':6,'G':7, 'H':8,'I':9, 'J':10}

cabins['Deck']=map(lambda a: deckmap.get(a[0], 0),cabins['Cabin'])
cabins['Rooms']=map(lambda a: len(a.split()),cabins['Cabin'])
cabins['NormFare'] = cabins['Fare'].values/cabins['Rooms'].values

cabins = cabins[['Survived','Pclass','NormFare','Deck', 'Rooms']]

good_class = train['Pclass']==2
cabins = cabins[good_class]

print float(cabins['Survived'].values.sum())/len(cabins['Survived'].values)
plt.scatter(cabins['Deck'].values, cabins['NormFare'].values, c = cabins['Pclass'].values)
plt.show()
#print cabins

sys.exit()
nfig = plt.figure()
cfig = plt.figure()
count = 0
for pclass in [1,2,3]:
    for gender in ['male', 'female']:
        for survived in [0,1]:
            data = train[(train['Pclass']==pclass) & (train['Sex'] == gender) & (train['Survived']==survived)]
        
            print data[['Survived','Pclass','Sex','Age', 'Fare', 'Cabin']]




print train.loc[300]


#['Age'].hist(by=train['Survived'], alpha=0.5, bins = 50, range=(0,100), normed=True)
#train[train['Pclass']==3]['Age'].hist(by=train['Survived'], alpha=0.5, bins = 50, range=(0,100), normed=True, cumulative=True)


#plt.show()


#plt.figure(f1.number)
