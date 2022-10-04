def tribonacci(n):
  if n==0 or n==1 or n==2:
    return 1
  else:
    return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
  
#OR
from collections import defaultdict
m = defaultdict(int)
def tribonacci(n):
  if m[n]:
    return m[n]
  elif n<=2:
    m[n]=n
    return m[n]
  else:
    m[n] = tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
    return m[n]
  
L=[]
for i in range(15):
    L.append(tribonacci(i))
print(" ".join(str(x) for x in L))
