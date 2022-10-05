bool check(n, m, x, y, mid):
  if (m + (y * (n - mid - 1)) - (x * mid) > 0):
    return true
  else:
    return false
  
def count_Pokemons(n, m, x, y):
  low = 0
  high = n
  mid = 0
  while(low<high):
    mid = low + (high-low)//2
    if check(n, m, x, y, mid):
      low = mid+1
    else:
      high = mid-1
      
  return mid 

#Driver code
n = 3 #No. of pokemons
m = 10 #Money
x = 4 #Cost to evolve a single pokemon
y = 2 #Selling bonus
print(count_Pokemons(n, m, x, y))

#This progam deals with counting the number of pokemons that can be evolved using the given money, given that x is the cost to evolve a single pokemon, n is the number of pokemons that are already present, m is the amount of money in rupees, y is the selling bonus of each pokemon in rupees.
