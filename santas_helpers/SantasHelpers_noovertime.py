__author__ = 'Alan Meert'
__date__ = 'December 7, 2014'

import os
import csv
import math
import heapq
import time
import datetime
import numpy as np

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

def solution_noovertime(toy_file, soln_file, myelves):
    """ Creates a simple solution where the next available elf is assigned a toy. Elves do not start
    work outside of sanctioned hours.
    :param toy_file: filename for toys file (input)
    :param soln_file: filename for solution file (output)
    :param myelves: list of elves in a priority queue ordered by next available time
    :return:
    """
    hrs = Hours()
    ref_time = datetime.datetime(2014, 1, 1, 0, 0)
    row_count = 0
    with open(toy_file, 'rb') as f:
        toysfile = csv.reader(f)
        toysfile.next()  # header row

        available_toys = []
        for row in toysfile:
            available_toys.append(Toy(row[0], row[1], row[2]))
            

    with open(soln_file, 'wb') as w:
        wcsv = csv.writer(w)
        wcsv.writerow(['ToyId', 'ElfId', 'StartTime', 'Duration'])
    

        toys_assigned = [9999,]
        while len(available_toys)>0:
            print 'available_toys ', len(available_toys)
            tot_ass = 0
            to_pop =[]
            for toycount, currtoy in enumerate(available_toys[:]):
                start_times = np.array([a.next_available_time for a in myelves])
                start_times = np.where(currtoy.arrival_minute>start_times, np.nan, start_times)
                best_times = np.argsort(start_times)
                    
                if np.isnan(start_times[best_times[0]]):
                    continue
                for elfpos in best_times:
                    try:
                        work_start_time = int(start_times[elfpos])
                    except ValueError:
                        continue
                    current_elf = myelves[elfpos]
                # work_start_time cannot be before toy's arrival
                #if work_start_time < current_toy.arrival_minute:
                #    print 'Work_start_time before arrival minute: {0}, {1}'.\
                #        format(work_start_time, current_toy.arrival_minute)
                #    exit(-1)

                    next_available_time, work_duration, unsanctioned = \
                        assign_elf_to_toy(work_start_time, current_elf, currtoy, hrs)
                    if (unsanctioned == 0 or toys_assigned[-1]==0):
                        current_elf.next_available_time = next_available_time
                        current_elf.update_elf(hrs, currtoy, work_start_time, work_duration)
                        
                # write to file in correct format
                        tt = ref_time + datetime.timedelta(seconds=60*work_start_time)
                        time_string = " ".join([str(tt.year), str(tt.month), str(tt.day), str(tt.hour), str(tt.minute)])
                        wcsv.writerow([currtoy.id, current_elf.id, time_string, work_duration])
                        to_pop.append(toycount)
                        tot_ass+=1
                        break
            for a in to_pop[::-1]:
                available_toys.pop(a)
            toys_assigned.append(tot_ass)
        print toys_assigned
        return

if __name__ == '__main__':

    start = time.time()

    NUM_ELVES = 900

    toy_file = os.path.join(os.getcwd(), 'data/toys_rev2.csv')
    soln_file = os.path.join(os.getcwd(), 'data/noovertime2.csv')

    myelves = create_elves(NUM_ELVES)
    solution_noovertime(toy_file, soln_file, myelves)

    print 'total runtime = {0}'.format(time.time() - start)
