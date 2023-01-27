from collections import deque
# Importing deque from the collections lib


def solve(board):
    # finding length of the column of the board
    m=len(board)
    # Finding len of the row of the board  
    n=len(board[0])

    queue = deque()

    # Traversing the borders and storing the cells with entry 'O' in queue
    for i in range(l):
        if board[i][0] == 'O':
            queue.append((i, 0))
        if board[i][n-1] == 'O':
            queue.append((i, n-1))
  
    for j in range(n):
        if board[0][j] == 'O':
            queue.append((0, j))
        if board[l-1][j] == 'O':
            queue.append((l-1, j))
    
    # Implementation of BFS(Breadth First Search)
    while queue:
        # Popinng the vertices from left end of queue
        x, y = queue.popleft()
        # If we come across any 'O' in border we mark it as Z as we cannot capture it.
        if 0 <= x < l and 0 <= y < n and board[x][y] == 'O':
            board[x][y] = 'Z'
            queue.append((x-1, y)) # Moving Up
            queue.append((x+1, y)) # Moving Down
            queue.append((x, y-1)) # Moving Left
            queue.append((x, y+1)) # Moving Right

    # Traversing every element in board and If we come across Z we make it 'O' else we make it X.
    for i in range(l):
        for j in range(n):
            if board[i][j] == 'Z':
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'


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