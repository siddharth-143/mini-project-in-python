def welcome_message():
    print("""
    This is 2 player game
    The computer - human based game.
    There are a total of 13 sticks.
    Each player chose minimum 1 and maximum 4 sticks in one turn.
    The player who picks up the last stick wins.
    All the best for both player........!.
    """)

def get_players():
    player_1 = input("Enter 1'st player name : ")
    player_2 = input("Enter 2'nd player name : ")
    return player_1, player_2

def game_logic():
    total_sticks = 13
    num_of_sticks_pick = 0
    turn = 1

    while total_sticks:
        print("Numbers of sticks remaining : ", total_sticks)
        print("player", turn, "'s turn")
        num_of_sticks_pick = int(input("Pick the minimum 1 and maximum 4 sticks : \n"))
        if num_of_sticks_pick > total_sticks \
        or num_of_sticks_pick > 4 \
        or num_of_sticks_pick < 1:
            print("That is not allowed. Try picking again.")
            continue
        total_sticks = total_sticks - num_of_sticks_pick
        if turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1

    if turn == 1:
        return 1
    else:
        return 0

def win_message(turn, player_1, player_2):
    if turn:
        print(player_2 + "  ->  Won")
    else:
        print(player_1 + "  ->  Won")

def main():
    welcome_message()
    player_1, player_2 = get_players()
    turn = game_logic()
    win_message(turn, player_1, player_2)

# staring the program
main()