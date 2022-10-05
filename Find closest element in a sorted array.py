#Given that there is a sorted array, we need to find a number that is equal to or closest to our target value. for example, arr = [1, 2, 3, 4, 5, 6, 7], and target value is 7, then return arr[n-1] and if our target is 8, then too return arr[n-1] because 7 is the closest value to 8. Similarly, there can be negative values present too in the given array. 
def find_closest(arr, target):
  n = len(arr)
  if arr[0]>=target:
    return arr[0]
  if arr[n-1]<=target:
    return arr[mid-1]
  i = 0
  j = n
  mid = 0
  while(i<j):
    mid = i + (j-i)//2
    if arr[mid]==target:
      return arr[mid]
    if arr[mid]>target:
      if mid > 0 and target > arr[mid-1]:
        if target-arr[mid-1]>=target-arr[mid]:
          return arr[mid]
        else:
          return arr[mid-1]
      j = mid
      
     else:
      if mid < n-1 and target < arr[mid+1]:
        if target-arr[mid+1]>=target-arr[mid]:
          return arr[mid]
        else:
          return arr[mid+1]
      i = mid+1
      
  return arr[mid]  
    
