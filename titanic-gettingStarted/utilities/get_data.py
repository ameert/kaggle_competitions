import numpy as np
import csv

datapath = '/home/ameert/git_projects/kaggle_competitions/titanic-gettingStarted/data/'

class passenger(object):
    """contains passenger data for titanic passengers"""
    def __init__(self, data):
        """passenger data:
VARIABLE DESCRIPTIONS:
survived        Survival (0 = No; 1 = Yes)
pid             Passenger ID
pclass          Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
name            Name
sex             Sex
age             Age
sibsp           Number of Siblings/Spouses Aboard
parch           Number of Parents/Children Aboard
ticket          Ticket Number
fare            Passenger Fare
cabin           Cabin
embarked        Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

SPECIAL NOTES:
Pclass is a proxy for socio-economic status (SES)
 1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

Age is in Years; Fractional if Age less than One (1)
 If the Age is Estimated, it is in the form xx.5

With respect to the family relation variables (i.e. sibsp and parch)
some relations were ignored.  The following are the definitions used
for sibsp and parch.

Sibling:  Brother, Sister, Stepbrother, or Stepsister of Passenger Aboard Titanic
Spouse:   Husband or Wife of Passenger Aboard Titanic (Mistresses and Fiances Ignored)
Parent:   Mother or Father of Passenger Aboard Titanic
Child:    Son, Daughter, Stepson, or Stepdaughter of Passenger Aboard Titanic

Other family relatives excluded from this study include cousins,
nephews/nieces, aunts/uncles, and in-laws.  Some children travelled
only with a nanny, therefore parch=0 for them.  As well, some
travelled with very close friends or neighbors in a village, however,
the definitions do not support such relations.
"""
        self.Pid,self.Pclass,self.Name, self.Sex, self.Age, self.SibSp,self.ParCh, self.Ticket, self.fare,self.cabin, self.embark =data
        self.survived = None
        return

    def print_port(self):
        """print the name of the port based on the letter assigned"""
        if self.embark == 'C':
            port = 'Cherbourg'
        elif self.embark == 'Q':
            port = 'Queenstown'
        elif self.embark == 'S':
            port =  'Southampton'
        print port
        return port

    def vectorize(self):
        """returns a vector useful for machine learning"""
        convert_sex = {'M':0.5, 'F':-0.5}

        return np.array((self.Pclass, convert_sex[self.Sex], self.Age, self.SibSp, self.ParCh,self.fare), dtype=float)

        return data

def get_data(filename, ftype='train'):
    csvfile =  open(datapath+filename, 'rb')
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    data.next() #skip the first row

    pdata = []
    for row in data:
        print row
        row = [a if a!='' else '999' for a in row]
        row = [a[0](a[1]) for a in zip([int, int, str, str, float, 
                                        int, int,str, float, str, str], row)]
        print row
        pdata.append(passenger(row))            
    return pdata


if __name__ == "__main__":
    pdata = get_data('train.csv', ftype='train')
    print pdata[0]
