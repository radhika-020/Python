def binary_search(arr, low, high, item):
  mid = (low+high)//2
  if low<=high:
    if arr[mid]==item:
      return mid
    elif arr[mid]<item:
      return binary_search(arr, mid+1, high, item)
    else:
      return binary_search(arr, low, mid-1, item)
