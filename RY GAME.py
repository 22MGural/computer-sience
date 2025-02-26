
board = [[' ' for _ in range(7)] for _ in range(6)]
for row in board:
   print('|'.join(row))
print('-' * 13)
print('0 1 2 3 4 5 6')
player = 1
winner = None
while not winner:
   col = int(input(f"Drop a {'Red (R)' if player == 1 else 'Yellow (Y)'} disk at column (0-6): "))
   for row in range(5, -1, -1):
       if board[row][col] == ' ':
           board[row][col] = 'R' if player == 1 else 'Y'
           break
   for row in board:
       print('|'.join(row))
   print('-' * 13)
   print('0 1 2 3 4 5 6')
   for r in range(6):
       for c in range(7):
           if board[r][c] == ' ':
               continue
           p = board[r][c]
           if c + 3 < 7 and p == board[r][c + 1] == board[r][c + 2] == board[r][c + 3]:
               winner = p
           if r + 3 < 6 and p == board[r + 1][c] == board[r + 2][c] == board[r + 3][c]:
               winner = p
           if r + 3 < 6 and c + 3 < 7 and p == board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3]:
               winner = p
           if r + 3 < 6 and c - 3 >= 0 and p == board[r + 1][c - 1] == board[r + 2][c - 2] == board[r + 3][c - 3]:
               winner = p
   if winner:
       print(f"{'Red' if winner == 'R' else 'Yellow'} wins!")
       break
   player = 3 - player  