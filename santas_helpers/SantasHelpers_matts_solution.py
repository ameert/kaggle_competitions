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

def next_newtoy(infile):
    try:
        newline = infile.readline()
        toy = newtoy(newline)
    except:
        toy=None
    return toy

def newtoy(newtoy):
    newtoy = newtoy.strip().split('\t')
    newtoy[1] = newtoy[1].replace('-', ' ')
    newtoy[1] = newtoy[1].replace(':', ' ')
    return Toy(newtoy[0], newtoy[1], newtoy[2])

    
def get_best_job(available_toys, rating, available_time, hrs):
    minleft =hrs.day_minutes_remaining(available_time)
    if minleft*rating < available_toys[-1].duration:
        best_job = None
    jobs = np.array([a.duration/rating for a in available_toys])
    job = np.where(jobs<minleft)[0]
    if job.size>0:
        best_job = available_toys.pop(np.min(job))
    return best_job    
        

def matts_solution(bj, tj, gj, soln_file, myelves,low_thresh, high_thresh):
    hrs = Hours()
    ref_time = datetime.datetime(2014, 1, 1, 0, 0)
    row_count = 0
    f =  open(gj, 'rb')
    f.readline()
    
    available_toys = []
    while True:
        try:
            line=f.readline()
            available_toys.append(newtoy(line))
        except:
            break
    f.close()
     
    tjfile = open(tj)
    tjfile.readline()
    bjfile = open(bj)
    bjfile.readline()

    with open(soln_file, 'wb') as w:
        wcsv = csv.writer(w)
        wcsv.writerow(['ToyId', 'ElfId', 'StartTime', 'Duration'])
    
        next_tiny = next_newtoy(tjfile)
        next_big = next_newtoy(bjfile)

        while len(available_toys)>0 :
            for elf in myelves:
                print 'elf ', elf.id
                job_to_ass=None
                if elf.rating >= high_thresh  and next_big is not None:
                    job_to_ass = next_big
                    next_big = next_newtoy(bjfile)
                elif elf.rating>=low_thresh:
                    job_to_ass = get_best_job(available_toys, elf.rating, elf.next_available_time, hrs) 
                if job_to_ass==None and next_tiny is not None:
                    job_to_ass = next_tiny
                    next_tiny = next_newtoy(tjfile)

                
                work_start_time = elf.next_available_time
                elf.next_available_time, work_duration, unsanctioned = \
                    assign_elf_to_toy(work_start_time, elf, job_to_ass, hrs)
                elf.update_elf(hrs, job_to_ass, work_start_time, work_duration)

                tt = ref_time + datetime.timedelta(seconds=60*work_start_time)
                time_string = " ".join([str(tt.year), str(tt.month), str(tt.day), str(tt.hour), str(tt.minute)])
                wcsv.writerow([job_to_ass.id, elf.id, time_string, work_duration])
                print job_to_ass.id, elf.id, time_string, work_duration, elf.rating

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

        tj = os.path.join(os.getcwd(), 'data/tiny_test.csv' )
        bj = os.path.join(os.getcwd(), 'data/big_test.csv' )
        gj = os.path.join(os.getcwd(), 'data/good_test.csv' )
        soln_file = os.path.join(os.getcwd(), 'data/matts_%d.csv' %(count))

        matts_solution(bj, tj, gj, soln_file, myelves, low_thresh, high_thresh)
        
        print 'total runtime = {0}'.format(time.time() - start)
