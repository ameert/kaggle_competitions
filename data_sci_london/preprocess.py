from sklearn import preprocessing as pre
from sklearn import decomposition as decom 
from sklearn import cross_validation as cross
from sklearn.linear_model import LogisticRegression as LogReg
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import numpy as np
import pylab as pl

def get_data(infile):
    """Reads in the data and vectorizes it"""
    indata = np.loadtxt(infile, delimiter=',', unpack = True)
    return indata

    
def plot_data(indata):
    """Plots the distributions of the data so that we 
can see what is going on"""
    
    dim = len(indata)

    for count, curdata in enumerate(indata):
        pl.subplot(np.ceil(np.sqrt(dim)),np.ceil(np.sqrt(dim)),count+1)
        pl.hist(curdata, bins=30)
        
    pl.subplots_adjust(left=0.05, bottom=0.05, top=0.95, right=0.95,
                      wspace = 0.5, hspace=0.5)
    pl.show()
    return

def renorm(indata):
    """rescales the data to have mean 0 and unit variance"""
    data_scaled = [pre.scale(a) for a in indata]

    return data_scaled

def do_pca(indata):
    pca = decom.PCA()#whiten=True)#n_components=28,
    pca.fit(indata)
    print pca.explained_variance_ratio_
    return pca

    
if __name__ == "__main__":
    indata = get_data('./data/train.csv')
    #plot_data(indata)
    
    scale_data = renorm(indata)
    
    #plot_data(scale_data)

    inlabels = get_data('./data/trainLabels.csv').astype(int)

    print np.sum(inlabels)
    
    x_train, x_test, y_train, y_test = cross.train_test_split(
        np.array(scale_data).T, inlabels, test_size=0.4, random_state=30)


    pca_out = do_pca(x_train)

    print pca_out
    x_train = pca_out.transform(x_train)
    x_test = pca_out.transform(x_test)


    log_reg_data = LogReg(penalty='l1',tol=0.0001, C=1.0)

    log_reg_data.fit(x_train, y_train)

    y_train_predict = log_reg_data.predict(x_train)
    y_train_proba = log_reg_data.predict_proba(x_train)[:,1]

    tp = np.where(y_train_predict==1,1,0)*np.where(y_train==1,1,0)
    tn = np.where(y_train_predict==0,1,0)*np.where(y_train==0,1,0)
    fp = np.where(y_train_predict==1,1,0)*np.where(y_train==0,1,0)
    fn = np.where(y_train_predict==0,1,0)*np.where(y_train==1,1,0)

    pl.subplot(2,2,1)
    pl.hist(np.extract(tp==1, y_train_proba), range=(0,1), bins = 20)
    pl.title('true positives')
    pl.subplot(2,2,2)
    pl.hist(np.extract(tn==1, y_train_proba), range=(0,1), bins = 20)
    pl.title('true negatives')
    pl.subplot(2,2,3)
    pl.hist(np.extract(fp==1, y_train_proba), range=(0,1), bins = 20)
    pl.title('false positives')
    pl.subplot(2,2,4)
    pl.hist(np.extract(fn==1, y_train_proba), range=(0,1), bins = 20)
    pl.title('false negatives')
    pl.show()

    y_test_predict = log_reg_data.predict(x_test)

    
    print accuracy_score(y_test_predict, y_test)
    print confusion_matrix(y_train, y_train_predict)

    #outfile = open('train_dat_predictions.csv','w')
    #outfile.write('#vals,Solution\n')
    #for count, prediction in enumerate(zip(x_train,y_train)):
    #    outfile.write('%d,%d\n' %(count+1, prediction))

    #outfile.close()

    
    

    indata_true = get_data('./data/test.csv').T
    indata_true = pca_out.transform(indata_true)


    y_answer = log_reg_data.predict(indata_true)

    outfile = open('london_predictions.csv','w')
    outfile.write('Id,Solution\n')
    for count, prediction in enumerate(y_answer):
        outfile.write('%d,%d\n' %(count+1, prediction))

    outfile.close()
    
    
    
    
