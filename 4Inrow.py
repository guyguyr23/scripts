import time
# the program create the game of 4 in a row

# size of the game bord
SIZE = 5
# first player value
FIRST = "1"
# seacond player value
SEACOND = "2"
# value of empty cell
EMPTY = "0"

def deep_copy(game_bord):
    # create a copy of the game bord
    new_game_bord = [[]]
    for x in range(SIZE):
        new_game_bord.append([])
        for y in range(SIZE):
            new_game_bord[x].append(game_bord[x][y])
    return new_game_bord


def clear_screen():
    # cleare the screan
    for i in range(15):
        print("\n")


def matrix_Init():
    # the function create a new game bord
    game_bord = [[]]
    for x in range(SIZE):
        game_bord.append([])
        for y in range(SIZE):
            game_bord[x].append(EMPTY)
    return game_bord


def matrix_Print(game_bord):
    # the function get the game bord and print it WITH ANIMATION
    clear_screen()
    for x in range(SIZE-1, -1, -1):
        print(' '.join(game_bord[x]))


def print_bord_animation(player_possion, game_bord):
    player_row = int(player_possion[0])
    player_col = int(player_possion[1])
    player = game_bord[player_row][player_col]
    copy_game_bord = deep_copy(game_bord)
    copy_game_bord[player_row][player_col] = EMPTY
    for i in range(5 - player_row):
        copy_game_bord[4-i][player_col] = player
        matrix_Print(copy_game_bord)
        time.sleep(0.4)
        copy_game_bord[4-i][player_col] = game_bord[4-i][player_col]


def currect_input(row, col, game_bord):
    # the function get the possion of the player
    # and the game bord and check if the input is good
    try:
        if (int(col) - 1) < 0 or (int(row) - 1) < 0:
            return False
        if game_bord[int(row)-1][int(col)-1] == EMPTY and \
            (int(row)-1 == 0 or game_bord[int(row)-2][int(col)-1] != EMPTY):
            #Check if the input is in an empty place and if there is somthing below it
            return True
        else:
            return False
    except:
        return False


def game_over(row, col, player, game_bord):
    # the function get the player new possion and check if the game is over
    row_sequence = 1
    col_sequence = 1
    i = 1 #the next possion to check
    # The player didnt win the game until now so if he is going to win the game
    # its beacuse of the last possion that he put in the game bord
    # so we need to check acurding to the current possion
    while row - i >= 0 and game_bord[row-i][col] == player:
        row_sequence += 1
        i += 1
    if row_sequence >= 4:
        return True
    i = 1 #rest the possion
    while row + i < SIZE and game_bord[row+i][col] == player:
        row_sequence += 1
        i += 1
    if row_sequence >= 4:
        return True
    i = 1
    while col + i < SIZE and game_bord[row][col+i] == player:
        col_sequence += 1
        i += 1
    if col_sequence >= 4:
        return True
    i = 1
    while col - i >= 0 and game_bord[row][col - i] == player:
        col_sequence += 1
        i += 1
    if col_sequence >= 4:
        return True
    return False


def game_play(player, game_bord):
    # the function get from a player his posision for the turn and place it if
    # it is currct
    player_possion = [1,1]
    player_row_possion = input(player + " Enter the your row: ")
    player_col_possion = input(player + " Enter the your col: ")
    while(not currect_input(player_row_possion, player_col_possion, game_bord)):
        # if the input of the user is not right he need to insert new place
        print("The input is not currect please try agine")
        player_row_possion = input(player + " Enter the your row: ")
        player_col_possion = input(player + " Enter the your col: ")

    game_bord[int(player_row_possion)-1][int(player_col_possion)-1] = player
    player_possion[0] = int(player_row_possion)- 1
    player_possion[1] = int(player_col_possion)- 1
    return player_possion

if __name__ == '__main__':
    game_bord = matrix_Init()
    matrix_Print(game_bord)
    game_over_with_tie = 0
    player_possion = [] # we need to save the possion of the player to use it for functions
    game_currnt_value = False #check if the game is over or not
    while True:
        # check if the game is over and play the player turn
        player_possion = game_play(FIRST, game_bord)
        game_currnt_value = game_over(player_possion[0], player_possion[1], FIRST, game_bord)
        print_bord_animation(player_possion, game_bord)
        game_over_with_tie += 1
        if game_currnt_value:
            print("The first player won the game!!")
            break
        # check if the game is over and play the player turn
        player_possion = game_play(SEACOND, game_bord)
        game_currnt_value = game_over(player_possion[0], player_possion[1], SEACOND, game_bord)
        print_bord_animation(player_possion, game_bord)
        game_over_with_tie += 1
        if game_currnt_value:
            print("The seacond player won the game!!")
            break
        if game_over_with_tie == (SIZE * SIZE):
            print("its a tie")
            break

