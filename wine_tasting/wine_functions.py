import numpy as np

def get_data(infile, get_labels = True):
    """Loads the data for the wine data"""
    data = np.loadtxt(infile, unpack=True, delimiter = ';')


    dataset ={'data':np.array(data[:11]), }
    if get_labels:
        dataset['labels']=np.array(data[11], dtype=float)
    else:
        dataset['labels']=[]

    return dataset


