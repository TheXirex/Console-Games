def init():
    index_board = [i for i in range(10)]
    print("It's Tic Tac Toe game!"
          "\nThis is what the field indices for the game look like:")
    print_board(index_board)
    player_list = player_choice()
    while True:
        start_game = input('Are you ready to start? (Y) ').lower()
        if start_game != 'y':
            print('The answer must be Y or y.')
            continue
        else:
            clear_console()
            return player_list

def print_board(board):
    counter = 0
    for i in range(3):
        for j in range(3):
            print(' {} '.format(board[counter]), end='')
            counter += 1
            if j != 2: print('|', end='')
        if i != 2: print('\n---|---|---')
    print()

def clear_console():
    print('\n' * 100)

def player_choice():
    while True:
        first_player = input('First player, choose between X and O:').lower()
        if first_player != 'x' and first_player != 'o':
            print('The answer must be X or O.')
            continue
        else:
            second_player = 'o' if first_player == 'x' else 'x'
            print('The first player plays for: {}'.format(first_player.upper()))
            print('The second player plays for: {}'.format(second_player.upper()))
            return [first_player, second_player]

def input_position(board, player):
    print('Turn X') if player == 'x' else print('Turn O')
    while True:
        position = input('Choose an index from 1 to 9:')
        if not position.isdigit():
            print('The answer must be a number.')
            continue
        position = int(position)
        if position in range(1, 10):
            position -= 1
            if board[position] == ' ':
                return position
            else:
                print('This position is taken, choose another one.')
                continue
        else:
            print('The index must be between 1 and 9.')
            continue

def change_board(board, position, player):
    board[position] = 'X' if player == 'x' else 'O'
    return board

def check_win(b):
    if b[0] == b[1] == b[2] != ' ' or b[3] == b[4] == b[5] != ' ': return True
    elif b[6] == b[7] == b[8] != ' ' or b[0] == b[3] == b[6] != ' ': return True
    elif b[1] == b[4] == b[7] != ' ' or b[2] == b[5] == b[8] != ' ': return True
    elif b[2] == b[4] == b[6] != ' ' or b[0] == b[4] == b[8] != ' ': return True
    else: return False

def win(board, player):
    clear_console()
    print_board(board)
    print('{} win the game!'.format(player.upper()))

def check_tie(b):
    return ' ' not in b

def tie(board):
    clear_console()
    print_board(board)
    print('Tie!')

def restart():
    while True:
        ans = input('Do you want to continue? (Y/N)').lower()
        if ans != 'y' and ans != 'n':
            print('The answer must be Y or N.')
            continue
        if ans == 'y':
            return True
        else:
            return False

def game(player_list, board):
    while True:
        clear_console()
        print_board(board)
        position = input_position(board, player_list[0])
        change_board(board, position, player_list[0])
        if check_win(board):
            win(board, player_list[0])
            break
        elif check_tie(board):
            tie(board)
            break
        else:
            player_list.reverse()
            continue
def start():
    player_list = init()
    while True:
        game(player_list, board = [' '] * 9)
        if restart():
            continue
        else:
            print('Good luck!')
            break

start()