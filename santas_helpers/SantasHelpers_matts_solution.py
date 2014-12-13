__author__ = 'Alan Meert'
__date__ = 'December 7, 2014'

import os
import csv
import math
import heapq
import time
import datetime
import numpy as np
from collections import OrderedDict
from bisect import bisect_left

from hours import Hours
from toy import Toy
from elf import Elf
from SantasHelpers_NaiveSolution import assign_elf_to_toy

def create_elves(NUM_ELVES):
    """ Elves are stored in a sorted list using heapq to maintain their order by next available time.
    List elements are a tuple of (next_available_time, elf object)
    :return: list of elves
    """
    list_elves = []
    for i in xrange(1, NUM_ELVES+1):
        list_elves.append(Elf(i))
    return list_elves

def newtoy(infile):
    newtoy = infile.readline()
    newtoy = newtoy.strip().split('\t')
    return Toy(newtoy[0], newtoy[1], newtoy[2])

def matts_solution(bj, tj, gj, soln_file, myelves):
    hrs = Hours()
    ref_time = datetime.datetime(2014, 1, 1, 0, 0)
    row_count = 0
    f =  open(gj, 'rb')
    f.readline()
    
    available_toys = []

    for row in f:
        available_toys.append(Toy(row[0], row[1], row[2]))
    f.close()
            
    with open(soln_file, 'wb') as w:
        wcsv = csv.writer(w)
        wcsv.writerow(['ToyId', 'ElfId', 'StartTime', 'Duration'])
    
        
    gjfile = open(gj)
    gjfile.readline()
    bjfile = open(bj)
    bjfile.readline()






    bjfile.close()
    gjfile.close()

    return

if __name__ == '__main__':

    for count in [900, ]:
        start = time.time()
        NUM_ELVES = count
        myelves = create_elves(NUM_ELVES)
        low_thresh = 0.5
        high_thresh = 2.0

        tj = os.path.join(os.getcwd(), 'data/tiny_jobs.csv' )
        bj = os.path.join(os.getcwd(), 'data/big_jobs.csv' )
        gj = os.path.join(os.getcwd(), 'data/good_jobs.csv' )
        soln_file = os.path.join(os.getcwd(), 'data/matts_%d.csv' %(count))

        matts_solution(bj, tj, gj, soln_file, myelves, low_thresh, high_thresh)
        
        print 'total runtime = {0}'.format(time.time() - start)
