class QFind:
    uid=[]
    def __init__(self,N):
        for i in range(N):
            self.N=N
            self.uid.append(i)
    def connected(self,p,q):
        if(self.uid[p]==self.uid[q]):
            return 1
        return 0
    def union(self,p,q):
        pid=self.uid[p]
        qid=self.uid[q]
        for i in range(self.N):
            if(self.uid[i]==pid):
                self.uid[i]=qid        
                                
def main():
    N=int(input("Enter No. of Objects: "))
    qu=QFind(N)
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
