num = 371
num = temp
sum1 = 0
digit = 0
length = len(str(num))
for i in range(length):
  digit = int(num%10)
  num = num//10
  sum1 += pow(digit, length)
  if sum1 == temp:
    print("Armstrong")
   else:
    print("Not Armstrong")
    
#OR Armstrong Number within a provided range

low, high = 10, 10000

for i in range(low, high+1):
  length = len(str(i))
  sum = 0
  temp = n
  while temp!=0:
    digit = n%10
    sum+=digit**length
    n//=10
    
    if temp==sum:
      print(n)
      
#OR

import math

first, second = 150, 10000


def is_Armstrong(val):
    sum1 = 0

    # this splits the val into its digits
    # example val : 153 will become [1, 5, 3]
    arr = [int(d) for d in str(val)] # Used list comprehension

    # now we iterate on array items (digits)
    # add these (digits raised to power of len i.e., order) to sum
    for i in range(0, len(arr)):
        sum1 = sum1 + math.pow(arr[i], len(arr))

    # if sum1 == val then its armstrong
    if sum1 == val:
        print(str(val) + ", ", end="")


for i in range(first, second + 1):
    is_Armstrong(i)
    
