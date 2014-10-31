import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv('./data/train_original.csv', index_col=0, header=0)

print train
print np.sum(train['Age'].isnull())

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
