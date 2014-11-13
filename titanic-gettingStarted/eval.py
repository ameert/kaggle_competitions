import sys
from utilities import *
from sklearn import preprocessing
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import accuracy_score

choice='logistic'

if choice=='logistic':
    from logistic import *


pdata = get_data('train.csv')
survived = get_survived('train_survived.csv')

for pos, sur_val in enumerate(survived):
    pdata[pos].survived = sur_val

train_data = np.array([a.vectorize() for a in pdata])
scaler = preprocessing.StandardScaler().fit(train_data)
train_scaled = scaler.transform(train_data)

skf = StratifiedKFold(survived, 5)
for tin, tes in skf:
    model = train(train_scaled[tin], survived[tin])
    predictions = model.predict(train_scaled[tes])
    print accuracy_score(survived[tes], predictions)


model = train(train_scaled, survived)

new_pdata = get_data('test.csv')
test_data = np.array([a.vectorize() for a in new_pdata])
test_scaled = scaler.transform(test_data)

predictions =  model.predict(test_scaled)

outfile = open('predictions.csv', 'w')
outfile.write('PassengerId,Survived\n')

for a in zip(new_pdata, predictions):
    outfile.write('%d,%d\n' %(a[0].Pid, a[1]))

outfile.close()

