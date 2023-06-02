#14976_TIC_TAC_TOE CW_REFERRAL CSF


#First of all i create the board of the game
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

#Here i use first datatype - function. It is "printBoard". With this function i can print the updated board in the game.
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
# Now i'll write the main function which has all the gameplay functionality.
#Now, in the main function, i will first take the input from the player and check if the input is a valid move or not. If the block that player requests to move to is valid, player will fill that block else game will ask the user to choose another block.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
