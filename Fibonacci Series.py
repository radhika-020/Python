def fibonacci(n):
  if n==0 or n==1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
  
#OR
from collections import defaultdict
m=defaultdict(int)
def fibonacci(n):
    if m[n]:
        return m[n]
    if n<=1:
        m[n]=n
        return m[n] 
    m[n]=fibonacci(n-1)+fibonacci(n-2)
    return m[n]
L=[]
for i in range(15):
    L.append(fibonacci(i))
print(" ".join(str(x) for x in L))
