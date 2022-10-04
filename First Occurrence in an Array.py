def first_occur(arr, target, i):
  size=len(arr)
  if i == size:
    return -1
  elif a[i] == target:
    return i
  else:
    return first_occur(arr, target, i+1)
