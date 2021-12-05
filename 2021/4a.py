def print_board(board):
    for row in board:
        print(row)
    print()
    
def check_win(board):
    for row in board:
        win_row = True
        for cell in row:
            if cell != 'X':
                win_row = False
        if win_row:
            return True
    for col in range(len(board[0])):
        win_col = True
        for cell in [row[col] for row in board]:
            if cell != 'X':
                win_col = False
        if win_col:
            return True
    return False
    
def process_bingo_nr(board, nr):
    for ridx, row in enumerate(board):
        for cidx, cell in enumerate(row):
            if cell == str(nr):
                board[ridx][cidx] = 'X'
                
def compute_score(board, n):
    # sum unmarked numbers
    score = 0
    for row in board:
        for cell in row:
            if cell != 'X':
                score += int(cell)
    # multiple with n
    score *= int(n)
    return score        

with open('data/input_4.txt') as infile:
#with open('data/example_4.txt') as infile:
    # read list of numbers
    bingo_numbers = infile.readline().strip()
    print(bingo_numbers)
    # read bingo boards
    board_lists = [line.strip().split() for line in infile.readlines() if line.strip() != '']
    nr_boards = len(board_lists)/5
    boards = []
    print('nr of boards', nr_boards)
    for i in range(int(nr_boards)):
        new_board = board_lists[(i*5):(i*5)+5]
        boards.append(new_board)
    
    # tests
    # test print_board
    #for board in boards:
    #    print_board(board)

    # test win condition: row
    #boards[0][0] = ['X','X','X','X','X']
    #print(boards[0])
    #print(check_win(boards[0]))

    # test win condition: col
    #for i in range(5):
    #    boards[0][i][3] = 'X'
    #print_board(boards[0])
    #print(check_win(boards[0]))

    # test process number
    #print("Before")
    #print_board(boards[0])
    #process_bingo_nr(boards[0], 17)
    #print("After")
    #print_board(boards[0])
    won = False
    for n in bingo_numbers.split(","):
        if won:
            break
        print("processing number", n)
        for board in boards:
            process_bingo_nr(board, n)
            win = check_win(board)
            if win:
                print_board(board)
                print("Win!")
                print(compute_score(board, n))
                won = True
                break
