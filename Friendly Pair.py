#Friendly pairs are the numbers whose all the divisors except the number itself gives a sum which is equal to the number given. For example, 6, 28, this is a friendly pair because divisors of 6 = 1, 2, 3, 6 and divisors of 28 = 1, 2, 4, 7, 14, 28, in the following example, divisors of 6 except 6 = 1+2+3 = 6 and divisors of 28 except 28 = 1+2+4+7+14 = 28. 

def friendly_pair(n, factors):
  i = 1
  while i<=n:
    if (n%i==0):
      factors.append[i]
      i+=1
  return sum(factors)-n #Subtracting the number from the sum of the factors list.

#OR

def printDivisors(n, factors) :
     
    # Note that this loop runs till square root
    i = 1
    while i <= pow(n,0.5):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                factors.append(i)
            else :
                # Otherwise print both
                factors.append(i)
                factors.append(int(n/i))
        i = i + 1
    return sum(factors) - n

if __name__ == "__main__": 
  number1, number2 = 6, 28
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print("Friendly pair")
  else:
    print("Not a Friendly Pair")
    
