#!/usr/bin/python3

import sys
from decimal import *

def fmt(x):
    count=0
    nblock=10
    ncol=5
    nrow=len(x)//(nblock*ncol)
    nleft=len(x)%(nblock*ncol)
    print("{:08d}:".format(count)+str(x[0:2]),end="")
    for j in range(0,ncol,1):
        print(x[2+(j*nblock):(2+(j+1)*nblock)],end=" ")
        count+=nblock
    print("\\\\")
    for i in range(1,nrow,1):
        print("{:08d}".format(count),end=":  ")
        for j in range(0,ncol,1):
            print(x[(2+i*ncol*nblock+j*nblock):(2+(i*ncol*nblock)+(j+1)*nblock)],end=" ")
            count+=nblock
        print("\\\\")

def main():
    dp=int(sys.argv[1])
    getcontext().prec = dp
    fmt(str((1+Decimal(5).sqrt())/2))

if __name__=="__main__":
    main()
