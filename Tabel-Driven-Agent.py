import random
class Environment:
    def __init__(self):
        #0 indicates clean and 1 indicates dirty
        self.locationCondition = {'A':0,'B':0}
        #randomize the conditions in loacation A and B
        self.locationCondition['A']=random.randint(0,1)
        self.locationCondition['B']=random.randint(0,1)

class TableDrivenAgent(Environment):
    def __init__(self,Environment):
        print(Environment.locationCondition)
        #Performance Measure
        score=0
        #place vacum at random location
        
        vacumLocation=random.randint(0,1)
        loc_A='A'
        loc_B='B'
        table = {(loc_A, 'Clean'): 'Right',
             ((loc_A, 'Dirty')): 'Suck',
             ((loc_B, 'Clean')): 'Left',
             ((loc_B, 'Dirty')): 'Suck',
             ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
             ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
             ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
             ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left'
        }
        if vacumLocation==0:
            print("Agent is at location A")
            if Environment.locationCondition['A']==1:
                print("A is Dirty")
                print("I am going to "+table[('A','Dirty')]+" it")
                Environment.locationCondition['A']=0
                score+=1
                print("A has been cleaned")
                print("I am going to "+table[('A','Clean')])
                score-=1
                if Environment.locationCondition['B']==1:
                    print("B is Dirty")
                    print("I am going to "+table[('B','Dirty')]+" it")
                    Environment.locationCondition['B']=0
                    score+=1
                    print("B has been cleaned")
            else:
                score-=1
                print("Move "+table[('A','Clean')])
                if Environment.locationCondition['B']==1:
                    print("B is Dirty")
                    Environment.locationCondition['B']=0
                    score+=1
                    print("B has been cleaned")
        elif vacumLocation==1:
            print("Agent is at location B")
            #suck the dirt and make it clean
            if Environment.locationCondition['B']==1:
                print("B is Dirty")
                print("I am going to "+table[('B','Dirty')]+" it")
                Environment.locationCondition['B']=0
                score+=1
                print("B has been cleaned")
                print("I am going to "+table[('B','Clean')])
                score-=1
                if Environment.locationCondition['A']==1:
                    print("A is Dirty")
                    print("I am going to "+table[('A','Dirty')]+" it")
                    Environment.locationCondition['A']=0
                    score+=1
                    print("A has been cleaned")
            else:
                score-=1
                print("I am going to "+table[('B','Clean')])
                if Environment.locationCondition['A']==1:
                    print("A is Dirty")
                    print("I am going to "+table[('A','Dirty')]+" it")
                    Environment.locationCondition['A']=0
                    score+=1
                    print("A has been cleaned")
        print(Environment.locationCondition)
        print("Performance  Measure "+str(score))