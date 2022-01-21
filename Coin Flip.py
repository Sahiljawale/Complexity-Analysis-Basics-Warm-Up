for t in range(int(input())):
    for g in range(int(input())):
        i,n,q=map(int,input().split())
        if(i==q):
            print(n//2)
        else:
            print(n-int(n/2))
