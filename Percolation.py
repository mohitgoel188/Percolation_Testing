from union_find import QUnion

def xyto1d(x,y):
        index=N*x+y+1
        if validate(index,1)==1:
                return index
        else:
                return -1

def validate(i,j):
        if(i<0):
                if j==0:
                        print("Illegal Arguments")
                """raise ValueError("Illegal Arguments")"""
        elif(i>=N*N+1):
                if j==0:
                        print("Aruguments Out of Range")
                """raise ValueError("Aruguments Out of Range")"""
                return 0
        else:
                return 1
        
class Percolation:
        status=[]
        def __init__(self,n):
                global N
                N=n
                self.grid=QUnion(N*N+2)                 #2 virtual sites 
                for i in range(1,N+1):
                        self.grid.union(0,i)
                for i in range(N*N-N+1,N*N+1):
                        self.grid.union(N*N+1,i)
                for i in range(N*N):                        
                        self.status.append(0)        
        def Open(self,row,col):
                index=xyto1d(row,col)
                if validate(index,0)==0:
                        return
                self.status[index-1]=1
                neighbour=[xyto1d(row-1,col),xyto1d(row+1,col),xyto1d(row,col-1),xyto1d(row,col+1)]
                for i in range(4):
                        if neighbour[i]==-1:
                                continue
                        elif self.status[neighbour[i]-1]==1:
                                self.grid.union(index,neighbour[i])   
        def isOpen(self,row,col):
                index=xyto1d(row,col)
                if validate(index,0)==0:
                        return 2
                if  self.status[index-1]==1:
                        return 1
                else:
                        return 0   
        def isFull(self,row,col):
                index=xyto1d(row,col)
                if validate(index,0)==0:
                        return 2
                if  self.status[index-1]==1:
                        if self.grid.connected(0,index)==1 :
                                return 1
                else:
                        return 0
        def numberofOpenSites(self):
                count=0
                for i in range(N*N):
                        if  self.status[i]==1:
                                count+=1
                return count
        def percolates(self):
                if self.grid.connected(0,N*N+1)==1:
                        return 1
                return 0
        def out(self):
                print(self.numberofOpenSites())
                print(self.percolates())
                for i in range(N):
                        for j in range(N):
                                index=N*i+j
                                print(self.status[index]),
                        print("")
                print(self.grid.uid)
                
def main():
        p=Percolation(N)
        while True:
                while True:
                        row=input("Row:")
                        col=input("Coloumn: ")
                        if p.isOpen(row,col)==0:
                                p.Open(row,col)
                        else:
                                print("Site already opened.")
                        i=input("Open more sites(0/1): ")
                        if i==0:
                                break     
                p.out()
                i=input("Open more sites(0/1): ")
                if i==0:
                        break

#N=input("Enter Grid length: ")
#main()
