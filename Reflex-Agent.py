import random
class Environment:
    def __init__(self):
        #0 indicates clean and 1 indicates dirty
        self.locationCondition = {'A':0,'B':0}
        #randomize the conditions in loacation A and B
        self.locationCondition['A']=random.randint(0,1)
        self.locationCondition['B']=random.randint(0,1)

class SimpleReflexAgent(Environment):
    def __init__(self,Environment):
        print(Environment.locationCondition)
        #Performance Measure
        score=0
        #place vacum at random location
        
        vacumLocation=random.randint(0,1)
        
        #Conditions
        
        if vacumLocation==0:
            print("Agent is at location A")
            #suck the dirt and make it clean
            if Environment.locationCondition['A']==1:
                print("A is Dirty")
                Environment.locationCondition['A']=0
                score+=1
                print("A has been cleaned")
                print("Move to B")
                score-=1
                if Environment.locationCondition['B']==1:
                    print("B is Dirty")
                    Environment.locationCondition['B']=0
                    score+=1
                    print("B has been cleaned")
            else:
                score-=1
                print("Moving to B")
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
                Environment.locationCondition['B']=0
                score+=1
                print("B has been cleaned")
                print("Move to A")
                score-=1
                if Environment.locationCondition['A']==1:
                    print("A is Dirty")
                    Environment.locationCondition['A']=0
                    score+=1
                    print("A has been cleaned")
            else:
                score-=1
                print("Moving to A")
                if Environment.locationCondition['A']==1:
                    print("A is Dirty")
                    Environment.locationCondition['A']=0
                    score+=1
                    print("A has been cleaned")
        print(Environment.locationCondition)
        print("Performance  Measure"+str(score))
            