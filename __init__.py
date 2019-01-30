# board
def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("----------")
    print(board[4] + ' | ' + board[5] + '| ' + board[6])
    print("----------")
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


# print('\n' * 100)
board = ['#', 'x', '0', 'x', '0', 'x ', '0', 'x', '0', 'x']
display_board(board)

# player imput
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: choose X OR O').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
