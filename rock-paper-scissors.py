import random

def end_menu():

    play_again = " "

    while play_again != "y" and play_again != "n":
        play_again = input("Would you like to play again? [y/n]: ")

        if play_again == "y":
            game()
        else:
            quit

def game():

    player_pts = 0
    opponent_pts = 0

    while player_pts < 3 and opponent_pts < 3:
        
        opponent = random.randint(1,3)

        while True:
            try:
                print("[1:Rock] [2:Paper] [3:Scissors]")
                player = int(input(" "))
                break
            except:
                print("Input a number")
    
        if player == opponent:
            pass

        if player == 1 and opponent == 2:
            opponent_pts += 1

        elif player == 1 and opponent == 3:
            player_pts += 1

        elif player == 2 and opponent == 1:
            opponent_pts += 1

        elif player == 2 and opponent == 3:
            opponent_pts += 1

        elif player == 3 and opponent == 2:
            player_pts += 1

        elif player == 3 and opponent == 1:
            opponent_pts += 1

        if opponent == 1:
            translate = "Rock O"
        elif opponent == 2:
            translate = "Paper [ ]"
        else:
            translate = "Scissors 8<"
        
        print(f"Opponent: {translate}")

    if player_pts > opponent_pts:
        print("YOU WIN!")
    elif player_pts < opponent_pts:
        print("You lose :(")
    
    end_menu()

game()