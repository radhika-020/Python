class solution:
  def solveQueens(self, n:int) -> List[List[str]]
  col = set()
  posDiag = () # (r+c), this should always remain constant for each positive diagnol, i.e., top to down.
  negDiag = () # (r-c). this should also remain always constant for each negative diagnol, i.e., bottom to up.
  res = []
  board = [["."] * n for i in range(n)] #Empty chessboard created
  
  def backtract(r):
    if r == n: #i.e, we have reached at the end where the present row has become equal to the number of queens
      copy = ["".join(row) for row in board]
      res.append(copy)
      return
    
    for c in range(n): #c here is the current column
      if c in col or (r+c) in posDiag or (r-c) in negDiag: #Which menas that the current column i.e., in use is either present in the column set, or r+c is present in positive diagonal set or r-c is present in negative diagonal set, then the queen cannot be added in the following column, therefore, we need to backtrack from this situation.
        continue
      
      #The following step is done to add the following c, r+c and r-c in their respective sets.
      col.add(c)
      posDiag(r+c)
      negDiag(r-c)
      board = [["Q"]] #or board[r][c] = "Q"
      
      backtrack(r+1)
      
      #And as we know, when we backrack, we remove all the added solution from our list or array and add a new solution to it which can be considered.
      #Therefore,
      col.remove(c)
      posDiag(r+c)
      negDiag(r-c)
      board[r][c] = "."
      
backtrack(0)
return res
      
  
  
