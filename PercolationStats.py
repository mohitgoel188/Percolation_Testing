import Percolation as per
import secrets
import statistic as stat
import time
class PercolationStats: 
        trials=[]
        def __init__(self,n, T):                       #    perform trials independent experiments on an n-by-n grid
                if n<=0 or T<=0:
                        raise ValueError("Illegal Arguments")
                self.numTrials=T
                for i in range(T):
                        p=per.Percolation(n)
                        while p.percolates()!=1:
                                row=secrets.randbelow(n)#random.randint(0,n)
                                col=secrets.randbelow(n)#random.randint(0,n)
                                #print(str(row)+"    "+str(col))
                                p.Open(row,col)
                        self.trials.append(float(p.numberofOpenSites())/(n**2))
                        """
                        for i in range(N):
                                for j in range(N):
                                        index=N*i+j
                                        print(p.status[index]),
                                print("")
                        print("")
                        """
        def mean(self):                                          #    sample mean of percolation threshold
                """mean=0
                for i in range(self.numTrials):
                       mean+=self.trials[i]/self.numTrials
                return mean"""
                return stat.mean(self.trials)
        def stddev(self):                                       #    sample standard deviation of percolation threshold
                """val=0
                x=self.mean()
                for i in range(self.numTrials):
                        val+=(self.trials[i]**2)/self.numTrials
                var=val-x**2
                if var<0:
                        var=-var
                return var**0.5"""
                return stat.stdev(self.trials)
        def confidenceLo(self):                            #     low  endpoint of 95% confidence interval
                return self.mean()-(1.96*self.stddev()/self.numTrials**0.5)
        def confidenceHi(self):                            #     high endpoint of 95% confidence interval
                return self.mean()+(1.96*self.stddev()/self.numTrials**0.5)

def main():
    N=int(input("Enter Grid Length: "))
    T=int(input("Enter Number of Trials: "))
    begt=time.time()
    test=PercolationStats(N,T)
    print("mean = "+str(test.mean()))
    print("stddev = "+str(test.stddev()))
    print("95% confidence interval = "+str(test.confidenceLo())+" , "+ str(test.confidenceHi()))
    endt=time.time()
    print("Total Time Elapsed: ")
    print(endt-begt)

if __name__ == '__main__':
    main()





      
