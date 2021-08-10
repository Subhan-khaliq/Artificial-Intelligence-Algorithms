class UCS:
    def __init__(self,x,y):
        self.i=x
        self.j=y
        self.tsp=[['Z','A','E','B','W','$'],
                  ['H','F','G','X','F','D'],
                  ['*','R','S','#','M','K'],
                  ['G','H','T','O','R','L'],
                  ['D','I','@','S','C','Y'],
                  ['V','W','N','P','Q','X']]
    def neigbours(self,i,j):
        neig=[]
        if i==0 and j==0:
            neig.append((i+1,j))
            neig.append((i,j+1))
        elif j==len(self.tsp[i])-1 and i==len(self.tsp)-1:
            neig.append((i,j-1))
            neig.append((i-1,j))
        elif i==0 and j!=len(self.tsp[i])-1:
            neig.append((i+1,j))
            neig.append((i,j+1))
            neig.append((i,j-1))
        elif i==len(self.tsp)-1 and j!=len(self.tsp[i])-1 and j!=0:
            neig.append((i-1,j))
            neig.append((i,j+1))
            neig.append((i,j-1))
        elif j==len(self.tsp[i])-1 and i!=0 and i!=len(self.tsp)-1:
            neig.append((i,j-1))
            neig.append((i+1,j))
            neig.append((i-1,j))
        elif j==0 and i==len(self.tsp)-1:
            neig.append((i-1,j))
            neig.append((i,j+1))
        elif j==len(self.tsp[i])-1 and i==0:
            neig.append((i,j-1))
            neig.append((i+1,j))
        elif j==0 and i!=len(self.tsp) and i!=0:
            neig.append((i-1,j))
            neig.append((i+1,j))
            neig.append((i,j+1))
        else:
            neig.append((i-1,j))
            neig.append((i+1,j))
            neig.append((i,j+1))
            neig.append((i,j-1))
        return neig
    
    def manhattan_Distance(self,x,y):
        l=self.neigbours(x,y)
        distance=[]
        for i in range(len(l)):
            distance.append((abs(x-l[i][0])+abs(y-l[i][1]),l[i]))
        distance.sort()
        return distance
    def goal(self,distance,path):
        x=distance[0][1][0]
        y=distance[0][1][1]
        if self.tsp[x][y]=='Y':
            path.append((x,y))
            return 1
        i=0
        while distance[i][0]==distance[0][0]:
            x=distance[i][1][0]
            y=distance[i][1][1]
            if self.tsp[x][y]=='Y':
                path.append((x,y))
                return 1
            if i==len(distance)-1:
                break
            else:
                i=i+1
        return 0
    def if_not_visited(self,d,v):
        p=[]
        p=d
        j=0
        for i in range(len(d)):
            if d[0][1] in v:
                p.pop(0)
        return p
    def visited_(self,visited):
        l=[]
        x=set(visited)
        visited=[]
        for i in x:
            l.append(i)
        return l
    def show_path(self,path):
        for i in path:
            if i==path[len(path)-1]:
                print(self.tsp[i[0]][i[1]])
            else:
                print(self.tsp[i[0]][i[1]],end=" -> ")
    def UCS(self):
        #Initially start state
        i=self.i
        j=self.j
        x=i
        y=j
        visited=[]
        distance=[]
        path=[]
        path.append((i,j))
        distance=self.manhattan_Distance(i,j)
        visited.append((x,y))
        if self.goal(distance,path)==1:
            print("Hurrah Goal is Found!","\n")
            self.show_path(path)
        else:
            while self.goal(distance,path)!=1:
                if self.tsp[x][y]=='Y':
                    print("Hurrah Goal is Found!","\n")
                    self.show_path(path)
                distance=self.if_not_visited(distance,visited)
                x=distance[0][1][0]
                y=distance[0][1][1]
                visited.append((x,y))
                path.append((x,y))
                visited=self.visited_(visited)
                distance = self.manhattan_Distance(x,y)
                if self.goal(distance,path)==1:
                    print("Hurrah Goal is Found!","\n")
                    self.show_path(path)
    def print_grid(self):
        for i in range(6):
            for j in range(6):
                print(self.tsp[i][j],end=" ")
            print(end="\n")


t1=UCS(0,0)
t1.print_grid()
print("\n","Now find the Shortest Path to the Goal","\n")
t1.UCS()