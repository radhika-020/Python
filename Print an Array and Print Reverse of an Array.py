def print_arr(arr, i):
  size = len(arr)
  if i==size:
    return
  print(arr[i], " ")
  print_arr(arr, i+1)
  
#Reverse of an Array
def print_reverse(arr, i):
  size = len(arr)
  if i == size:
    return
  print_reverse(arr, i+1)
  print(arr[i] , " ")
