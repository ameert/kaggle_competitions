import  Queue as qu 
from toy import Toy
from hours import Hours
from elf import Elf
import sys

class node(object):
    """A tree structure for efficently sorting and searching the elf jobs
Taken from http://cbio.ufs.ac.za/live_docs/nbn_tut/trees.html"""

    def __init__(self, value, height):
        self.value = value
        self.height = height
        if self.height >0:
            self.jobs = None
            self.children = dict([ (a,node(a, height-1)) for a in range(0,10)])
        else:
            self.children = None
            self.jobs = qu.Queue()
        return

    def __repr__(self, level=0):
        ret = "\t"*abs(level)+repr(self.value)+"\n"
        if self.children is not None:
            for child in self.children.values():
                ret += child.__repr__(level-1)
        else:
            ret = "\t"*abs(level)+repr(self.value)+" : "+ repr(self.jobs.qsize())+"\n"

        return ret
    
    def walk_tree(self, duration):
        """returns the tree path for a given duration
        tree: node class
        duration: int value of minutes"""
        sdur = str(duration)
        sdur = '0'*(self.height-len(sdur)) +sdur
        sdur = [int(a) for a in sdur]
        return sdur

def add_job(tree, ctoy, location):
    """add job to the correct queue"""
    if len(location)==1:
        tree.children[location[0]].jobs.put(ctoy)
    else:
        tree.children[location[0]] = add_job(tree.children[location[0]], ctoy, location[1:])
    return tree

def get_job(tree, location):
    """get job from the correct queue. This is a depth first search of the tree"""
    job = None
    if len(location)==1:
        while tree.children[location[0]].jobs.empty():
            location[0]-=1
            if location[0]<0:
                break
        if location[0]>=0:
            job = tree.children[location[0]].jobs.get()
    else:
        while job == None:
            job = get_job(tree.children[location[0]], location[1:])
            location[0]-=1
            if location[0]<0:
                break
    return job
    
    
def newtoy(newtoy):
    newtoy = newtoy.strip().split('\t')
    newtoy[1] = newtoy[1].replace('-', ' ')
    newtoy[1] = newtoy[1].replace(':', ' ')
    return Toy(newtoy[0], newtoy[1], newtoy[2])


if __name__ == "__main__":
    import numpy as np
    f =  open('data/tiny_jobs.csv', 'rb')
    f.readline()

    line=f.readline()
    ctoy = newtoy(line)
    height = int(np.floor(np.log10(ctoy.duration)))
    tree = node(0, height+1)
    loc = tree.walk_tree(ctoy.duration)
    tree = add_job(tree, ctoy, loc)
            
    print "loading toys"
    available_toys = 0
    while True:
        if available_toys %10000 ==0:
            print available_toys
        try:
            line=f.readline()
            ctoy = newtoy(line)
            loc = tree.walk_tree(ctoy.duration)
            tree = add_job(tree, ctoy, loc)
            available_toys+=1
        except IndexError:
            if line == '':
                #EOF
                break
            else:
                print "bad line"
                print line
    f.close()
    print "toys loaded"

    print tree

    job = 1
    while job != None:
        job= get_job(tree, tree.walk_tree(9))
        print job
        try:
            print job.id, job.duration
        except AttributeError:
            print None
