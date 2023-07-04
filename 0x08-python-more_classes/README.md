# Python - More Classes

## 101-N-Queen

1. The function is_safe(board, row, col) checks if it is safe to place a queen at the given position (row, col) on the board. It iterates through all the previously placed queens (from row 0 to row-1) and checks if there is any conflict with the current position. It checks for conflicts in the same column, the same diagonal (both left and right diagonals). If any conflict is found, it returns False, indicating that it's not safe to place a queen at that position. Otherwise, it returns True.

2. The main function solve(board, row) is a recursive function that finds the solutions for the N-queen puzzle. It takes two parameters: board, which represents the current state of the board, and row, which represents the current row being considered.

3. If row == N, it means all N queens have been successfully placed on the board, and a valid solution has been found. In this case, it prints the coordinates of the queens and an empty line to separate solutions.

4. If row < N, it means there are still queens to be placed. It iterates through each column in the current row (col), and checks if it's safe to place a queen at (row, col) using the is_safe function.

5. If it's safe to place a queen at (row, col), it updates the board accordingly by assigning col to board[row]. Then, it recursively calls solve(board, row + 1) to move on to the next row and continue the process.

6. If it's not safe to place a queen at (row, col), it simply moves on to the next column and checks the next position.

By using backtracking and recursion, the algorithm systematically explores all possible configurations of queens on the board. It places queens row by row, checking for conflicts at each step and backtracking whenever a conflict is encountered. This way, it finds all the valid solutions for the N-queen puzzle.
