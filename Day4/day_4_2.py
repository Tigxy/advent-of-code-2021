import numpy as np

with open("input.txt", "r") as fh:
	lines = fh.readlines()
	
drawn_numbers = [int(c) for c in lines[0].strip().split(",")]

boards = []
for i in range(2, len(lines), 6):
	# one board for the numbers, one as a mask numbers were called
	board = [None] * 2 
	board[0] = np.array([[int(c) for c in line.strip().split(" ") if c != ""] for line in lines[i:i+5]], dtype=np.int32)
	board[1] = np.full_like(board[0], fill_value=False, dtype=bool)
	boards.append(board)
n_boards = len(boards)

n_boards_won = 0
winner_board = None
winner_boards = []
for n in drawn_numbers:
	for i, board in enumerate(boards):
		if i in winner_boards:
			continue
	
		board[1] = board[1] | (board[0] == n)
		if (board[1].sum(axis=0) == 5).any() \
			or (board[1].sum(axis=1) == 5).any() \
			or np.diagonal(board).sum() == 5 \
			or np.diagonal(np.fliplr(board)).sum() == 5:
			board_won = True
			winner_board = board
			n_boards_won += 1
			winner_boards.append(i)
	if n_boards_won == n_boards:
		print("Done playing")
		break
		
print("n boards", n_boards_won, n_boards)
print("last board won: ")
print(winner_board[0])
print(winner_board[1])

item_sum = winner_board[0][~winner_board[1]].sum()
last_number_called = n

print("Item sum:", item_sum)
print("Last number called:", last_number_called) 
print("Final score:", item_sum * last_number_called)	