def permutation(a, left, right):
  left = 0
  right = len(a)-1
  if left==right:
    return a
  else:
    swap(a[left], a[i])
    
    permutation(a, left+1, right)
    
    #backtrack
    swap(a[left], a[i])
    
#Time Complexity:- O(n*n!)
