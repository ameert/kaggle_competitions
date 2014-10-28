import sys
from utilities import *

choice='logistic'

if choice=='logistic':
    from logistic import *


pdata = get_data('train.csv')
survived = get_survived('train_survived.csv')

for pos, sur_val in enumerate(survived):
    pdata[pos].survived = sur_val

train_data = np.array([a.vectorize() for a in pdata])

model = train(train_data, survived)


new_pdata = get_data('test.csv')
test_data = np.array([a.vectorize() for a in new_pdata])

predictions =  model.predict(test_data)

outfile = open('predictions.csv', 'w')
outfile.write('PassengerId,Survived\n')

for a in zip(new_pdata, predictions):
    outfile.write('%d,%d\n' %(a[0].Pid, a[1]))

outfile.close()

