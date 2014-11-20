import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.cross_validation import StratifiedKFold
from sklearn.externals.six import StringIO  
import pydot
from sklearn import tree
from wine_functions import get_data
from REC_curve import rec_curve

winetype='white'

dataset = get_data('./data/train-winequality-%s.csv' %winetype) 

skf = StratifiedKFold(dataset['labels'], n_folds=5)

clf = RandomForestRegressor(n_estimators=50, max_depth=11, min_samples_split=2, 
                                min_samples_leaf=1, max_features='auto', 
                                oob_score=True, n_jobs=-1, random_state=42, 
                                verbose=False)

AOC = []
tols = []

for train_index, test_index in skf:
    print train_index
    train_dat = dataset['data'].T[train_index]
    test_dat = dataset['data'].T[test_index]
    train_lab = dataset['labels'][train_index]
    test_lab = dataset['labels'][test_index]

    clf.fit(train_dat,train_lab)
    
    outlabels = clf.predict(test_dat)
    print mean_absolute_error(outlabels, test_lab)

    plt.scatter(test_lab,outlabels)
    plt.xlabel('true label')
    plt.ylabel('fitted label')

    train_curve = rec_curve(test_lab,outlabels)
    train_curve.calc_rec(0.0, 10.0)
    #train_curve.display(None)

    AOC.append(train_curve.AOC)
    tols.append(train_curve.get_accuracy(np.array([0.25,0.5,1.0])))

plt.close('all')

clf.fit(dataset['data'].T,dataset['labels'])
outlabels = clf.predict(dataset['data'].T)
print mean_absolute_error(outlabels, dataset['labels'])


train_curve = rec_curve(dataset['labels'],outlabels)
train_curve.calc_rec(0.0, 10.0)
    
print "Final AOC estimate: %0.3f" %np.array(AOC).mean()
print "Final Tolerance estimate (0.25, 0.5, 1.0): %s" %str(np.array(tols).mean(axis=0))

confusion = np.histogram2d(dataset['labels'],outlabels, bins=11,
                           range=[[-0.5,10.5], [-0.5,10.5]])#, weights=None)

plt.imshow(np.log10(confusion[0]), origin='lower', interpolation='none', vmin=0)
plt.colorbar()
plt.title('Confusion Matrix')
plt.xlabel('true label')
plt.ylabel('fitted label')
train_curve.display(None)



final_test = get_data('./data/train-winequality-%s.csv' %winetype) 
final_labels = clf.predict(dataset['data'].T)
outfile = open('alans_preds.txt','w')
for a in final_labels:
    outfile.write('%f\n' %a)
outfile.close()



