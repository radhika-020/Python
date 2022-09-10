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
