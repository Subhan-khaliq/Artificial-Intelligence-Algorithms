#To store data of the grid into a 2D-list
Grd = [[['1', 3], ['4', '15']],
        [['2', 4], ['21']],
        [['3', 1], ['2', '8', '4']],
        [['4', 3], ['1', '18']],
        [['5', 1], ['4', '9']],
        [['6', 3], ['Goal', '20']],
        [['7', 3], ['21', '9']],
        [['8', 3], ['22']],
        [['Goal', 'G']],
        [['9', 2], ['8', '19']],
        [['10', 3], ['13']],
        [['11', 1], ['7', '10', '12', '16']],
        [['12', 2], ['3', '10', '14', '22']],
        [['13', 2], ['4', '11', '23']],
        [['14', 3], ['11']],
        [['15', 4], ['19']],
        [['16', 2], ['7', '18']],
        [['17', 3], ['3']],
        [['18', 3], ['4', '15']],
        [['19', 3], ['5', '16']],
        [['20', 4], ['1', '24']],
        [['21', 1], ['16', '20', '22']],
        [['22', 4], ['3']],
        [['23', 3], ['Goal', '20']],
        [['24', 2], ['14', '22']],
       ] 

#Now to create Node
class Node:
    #Constructor
    def __init__(self,key):
        self.val=key
        #Childs can be multiple so we need list
        self.child=[]

#Function to create Nodes
def createNode(key):
    addr=Node(key)
    return addr

#Function to travers nodes

def traversal_nodes(root):
    if root==None:
        return
    Queue=[]
    Queue.append(root)
    while len(Queue)!=0:
        n=len(Queue)
        while n>0:
            p=Queue[0]
            Queue.pop(0)
            print(p.val,end=" ")
            for i in range(len(p.child)):
                Queue.append(p.child[i])
            n -=1
        print(end="\n")

def child_nodes(root):
    for i in range(0,25):
        temp=""
        if root.val==Grd[i][0][0]:
            temp=Grd[i][1]
        for j in temp:
            root.child.append(createNode(j))
#Now to travel in the grid and find the goal
#it will take the grid and the state by the user
def travel(grid,state):
    root = createNode(grid[state][0][0])
    real_root = root
    queue = []
#To find the cost of the Path
    Cost = 0
    #if the state is the goal
    if root.val == 'Goal':
        print('At Last Reached at the Goal')
        return
    #to print the queue frontier
    print('Queue-Maintaning: ', root.val)
    queue.append(root)
    #Here, I am finding the Goal state
    while root.val != 'Goal':
        child_nodes(root)
        print('Visiting Nodes')
        traversal_nodes(real_root)
        Cost += 1
        limit = len(root.child)
        for j in range(0,limit):
            print('Append in Queue: ', root.child[j].val)
            queue.append(root.child[j])
        print('Popping: ',queue.pop(0).val)
        root = queue[0]
        print('Latest Root: ', root.val)
    print('Finally Reached at the Goal state')
    print('Path Cost: ', Cost)

travel(Grd,11)