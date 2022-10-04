def last_occur(arr, target, i, pos):
  size = len(arr)
  if i == size:
    return pos
  elif arr[i]==target:
    pos = i
  else:
    return last_occur(arr, target, i+1, pos)
