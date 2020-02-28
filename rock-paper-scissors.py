import random
import time
import os

def clear():

    os.system( 'cls' )

def end_menu():

    play_again = " "

    while play_again != "y" and play_again != "n":
        play_again = input("Would you like to play again? [y/n]: ")

        if play_again == "y":
            game()
        else:
            quit

def game():

    print(" ")
    print("Welcome to Rock, Paper, Scissors.")
    time.sleep(1)
    print("First to 3 wins")
    time.sleep(1)
    print("Good Luck :)")
    time.sleep(1)

    player_pts = 0
    opponent_pts = 0

    round = 1
    
    while player_pts < 3 and opponent_pts < 3:

        opponent = random.randint(1,3)

        while True:
            try:
                print(" ")
                print(f"---Round {round}---")
                print(" ")
                player = int(input("1-Rock Ø    2-Paper [ ]    3-Scissors 8< : "))
                print(" ")
                break
            except:
                print("Input 1, 2 or 3")
    
        if player == opponent:
            pass

        elif player == 1 and opponent == 2:
            opponent_pts += 1

        elif player == 1 and opponent == 3:
            player_pts += 1

        elif player == 2 and opponent == 1:
            player_pts += 1

        elif player == 2 and opponent == 3:
            opponent_pts += 1

        elif player == 3 and opponent == 2:
            player_pts += 1

        elif player == 3 and opponent == 1:
            opponent_pts += 1

        if player == 1:
            player_tran = "Rock Ø"
        elif player == 2:
            player_tran = "Paper [ ]"
        else:
            player_tran = "Scissors 8<"

        if opponent == 1:
            opponent_tran = "Rock Ø"
        elif opponent == 2:
            opponent_tran = "Paper [ ]"
        else:
            opponent_tran = "Scissors 8<"
        
        print(f"You: {player_tran}               pts: {player_pts}")
        print(f"Opponent: {opponent_tran}          pts: {opponent_pts}")

        round += 1
        
        #time.sleep(2)
        #clear()


    print(" ")

    time.sleep(1)

    if player_pts > opponent_pts:
        print("YOU WIN!")
    elif player_pts < opponent_pts:
        print("You lose :(")
    
    end_menu()

game()