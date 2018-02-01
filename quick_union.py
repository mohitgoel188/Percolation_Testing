class QUnion:                        
        uid=[]
        sz=[]
        def __init__(self,N):
                for i in range(N):
                        self.uid.append(i)
                        self.sz.append(1)
        def root(self,i):
                while i!=self.uid[i]:
                        self.uid[i]=self.uid[self.uid[i]]              
                        i=self.uid[i]
                return i
        def connected(self,p,q):
                return self.root(p)==self.root(q)
        def union(self,p,q):
                i=self.root(p)
                j=self.root(q)
                if(self.sz[i]>self.sz[j]):
                        self.uid[j]=i
                        self.sz[i]+=self.sz[j]
                else:
                        self.uid[i]=j
                        self.sz[j]+=self.sz[i]

def main():
    N=int(input("Enter No. of Objects: "))
    qu=QUnion(N)
    while True:
        p=int(input())
        q=int(input())
        if qu.connected(p,q)==0:
            qu.union(p,q)
            print(qu.uid)
            print("Pair added: "+str(p) + " "+ str(q))
        else:
            print("Pair already exist.")
        i=int(input("Add more pairs?(0/1): "))
        if i==0:
            break     

if __name__ == '__main__':
    main() 
