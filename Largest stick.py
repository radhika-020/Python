def cut_height(height, n, cut):
  cnt = 0
  for i in range(1, n):
    cnt+=height[i]/cut
    i+=1
  return cnt
    
#Height is the array in which height of each individual stick is contained, n is the number of sticks and cut is the number of cuts that can be made on any individual stick.

def find_max_height(height, n, x, max_height):
  l = 0
  h = max_height
  ans = -1
  while(l<h):
    m = l + (h-l)//2
    if cut_height(height, n, m) >= x:
      ans = m
      l = m+1
    else:
      h = m-1
 return ans

#x is the number of sticks that are to be made from the given number of sticks, max-height is the maximum height of the sticks given.
