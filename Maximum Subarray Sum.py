from sys import maxint

def find_max_subarray-sum(arrr, size):
  max_so_far = -maxint - 1
  max_ending_here = 0
  
  for i in range(0, size):
    max-ending here = max_ending_here + arr[i]
    if max_so_far < max-ending_here:
      max_so_far = max_ending_here
      
      if max_ending_here < 0:
        max_ending_here = 0
  return max_so_far
