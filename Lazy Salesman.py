for _ in range(int(input())):
  n,r=map(int,input().split())
  l=list(map(int,input().split()))
  l.sort(reverse= True)
  
  sum=0
  for i in range(n):
    sum+=l[i]
    if sum>=r:
      break
  print(n-i-1)
