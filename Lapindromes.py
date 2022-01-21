for _ in range(int(input())):
  s=input()
  fh=s[0:len(s)//2]
  sh=s[len(s)//2 if len(s)%2 == 0 else ((len(s)//2)+1):]
  df={};ds={}
  for i in fh:
    if i in df:
      df[i]+=1
    else:
      df[i]=1
  for i in sh:
    if i in ds:
      ds[i]+=1
    else:
      ds[i]=1
  print("YES") if ds==df else print("NO")
