# Solving the problem in DFS Depth first search

def solve(board):
    # finding length of the column of the board
    m=len(board)
    # Finding len of the row of the board  
    n=len(board[0])

    #Creating dfs function 
    def dfs(m,n):
        if n <0 or m<0 or n == len(board[0]) or m == len(board) or board[m][n]!='O':
            return
       
        board[m][n]='Z'
        dfs(m+1,n) # Moving Down
        dfs(m,n+1) # Moving Right
        dfs(m-1,n) # Moving Up
        dfs(m,n-1) # Moving Left
    # Traversing every element in board and If we come across 'O' we move it to dfs and explore its neighbours.
    for i in range(m):
        for j in range(n):
            #If element is 'O; and is in borders of board we move it to dfs
            if (board[i][j]=='O' and (i in [0,m-1] or j in [0,n-1])):
                dfs(i,j)
    # Traversing every element in board and If we come across Z we make it 'O' else we make it. X.
    for i in range(m):
        for j in range(n):
            if board[i][j]=='O':
                board[i][j]='X'
            if board[i][j]=='Z':
                board[i][j]='O'


# Getting the input from the user 
no_columns = int(input("Enter no of columns"))
no_rows =int(input("Enter no of rows"))
board = [[""]*no_columns]*no_rows
print(board)
for i in range(no_columns):
    for j in range(no_rows):
        board[j][i] = input(f"enter the value in the {i}, {j} th positon\n")
print(board)


# Default board input  
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print("Solution using Breadth First Search")
print("\nBoard before captures")
for r in board:
   for c in r:
      print(c,end = " ")
   print()

solve(board)
print("\nBoard after captures - ")
for r in board:
   for c in r:
      print(c,end = " ")
   print()
