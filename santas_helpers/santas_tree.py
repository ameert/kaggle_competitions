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
            self.children = [ node(a, height-1) for a in range(0,10)]
        else:
            self.children = None
            self.jobs = qu.Queue()
        return

    def __repr__(self, level=0):
        ret = "\t"*abs(level)+repr(self.value)+"\n"
        if self.children is not None:
            for child in self.children:
                ret += child.__repr__(level-1)
        return ret
    
    
def newtoy(newtoy):
    newtoy = newtoy.strip().split('\t')
    newtoy[1] = newtoy[1].replace('-', ' ')
    newtoy[1] = newtoy[1].replace(':', ' ')
    return Toy(newtoy[0], newtoy[1], newtoy[2])


if __name__ == "__main__":
    import numpy as np
    f =  open('data/good_jobs.csv', 'rb')
    f.readline()

    line=f.readline()
    ctoy = newtoy(line)
    height = int(np.floor(np.log10(ctoy.duration)))
    value = ctoy.duration / 10**height 
    print ctoy.duration, value
    tree = node(0, height+1)
    print tree
    sys.exit()
            
    print "loading toys"
    available_toys = []
    while True:
        try:
            line=f.readline()
            ctoy = newtoy(line)
            
        except IndexError:
            if line == '':
                #EOF
                break
            else:
                print "bad line"
                print line
    f.close()
    print "toys loaded"


    joblens = np.array([ a.duration for a in available_toys], dtype=int)

    print len(joblens)
    print joblens.max()
    print "maxval ", np.ceil(np.log10(joblens.max()))
