import sklearn
import numpy as np
import matplotlib.pyplot as plt

from wine_functions import *

winetype = 'white'

dataset = get_data('./data/train-winequality-%s.csv' %winetype) 

print dataset
print dataset['data'].shape


datalabels = ['fixed acidity g/L tartaric','volatile acidity g/L accetic', 'citric acid g/L',
              'residual sugar g/L', 'chlorides g/L NaCL', 'free sulfur dioxide mg/L',
              'total sulfur dioxide mg/L', 'density g/cc', 'pH', 'sulphates g/L KSO$_4$',
              'alcohol % vol', 'density/residual sugar']


#for a in zip(datalabels, dataset['data']):
#    plt.scatter(a[1], dataset['labels'])
#    plt.title(a[0])
#    plt.show()

plotdat = dict(zip(datalabels, dataset['data']))

def do_2dplot(xdat, ydat, plotdat, labels):
    fig = plt.figure(figsize=(8,6))
    plt.scatter(plotdat[xdat],plotdat[ydat], edgecolor='none', s=6,c = labels)
    plt.xlabel(xdat)
    plt.ylabel(ydat)
    plt.colorbar()
    return

do_2dplot('fixed acidity g/L tartaric', 'volatile acidity g/L accetic', plotdat, dataset['labels'])
do_2dplot('residual sugar g/L', 'pH', plotdat, dataset['labels'])
do_2dplot('residual sugar g/L', 'fixed acidity g/L tartaric', plotdat, dataset['labels'])
do_2dplot('residual sugar g/L', 'alcohol % vol', plotdat, dataset['labels'])
do_2dplot('density g/cc','residual sugar g/L', plotdat, dataset['labels'])
do_2dplot('density g/cc', 'alcohol % vol', plotdat, dataset['labels'])
do_2dplot('density g/cc','residual sugar g/L', plotdat, plotdat['alcohol % vol'])
do_2dplot('density g/cc','residual sugar g/L', plotdat, plotdat['alcohol % vol'])


fig = plt.figure()
plt.hist(dataset['labels'], bins=np.arange(-0.5, 10.51,1.0))
plt.show()
