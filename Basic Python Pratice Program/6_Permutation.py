def npr(n, r):
  i = n-r+1
  perm = 1;
  while (i<=n):
    perm *= i;
    i+=1
    
    
npr(7, 2)
