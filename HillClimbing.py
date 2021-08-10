class hillClimb:
    def __init__(self,h,k):
        self.i=h
        self.j=k
        self.tsp =[
    [0, 400, 500, 300],
    [300, 0, 300, 500],
    [500, 300, 0, 400]
]
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
    
    def hillclimbing(self):
        i=self.i
        j=self.j
        current_state=(i,j)
        neigh=self.neigbours(i,j)
        t=[]
        for p in range(len(neigh)):
            h=neigh[p][0]
            k=neigh[p][1]
            t.append(self.tsp[h][k])
        d=max(t)
        if self.tsp[i][j] > d:
            current_state=(i,j)
            return current_state
        for i in range(len(neigh)):
            h=neigh[i][0]
            k=neigh[i][1]
            if self.tsp[h][k]==d:
                current_state=(h,k)
        return current_state
    def print_grid(self):
            for i in range(3):
                for j in range(4):
                    print(self.tsp[i][j],end=" ")
                print(end="\n") 

#It will take row and column for the current state and return next move
t1=hillClimb(0,3)
t1.print_grid()
print(t1.hillclimbing())