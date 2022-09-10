num = 1234
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)

#OR for the Palindrome Number

num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
  
#OR using sring slcing
  
num = 1234
reverse = int(str(num)[::-1])

if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
