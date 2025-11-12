from random import choice
list = ['paper', 'rock', 'scissors']

computer_choice = choice(list)
user_choice = input("Enter paper, rock, or scissors: ")
print(f"Computer chose: {computer_choice}\nYou chose: {user_choice}")
match user_choice:
    case 'paper':
        if computer_choice == 'paper':
            print("It's a tie!")
        elif computer_choice == 'rock':
            print("You win! Paper covers rock.")
        else:
            print("You lose! Scissors cut paper.")
    case 'rock':
        if computer_choice == 'rock':
            print("It's a tie!")
        elif computer_choice == 'scissors':
            print("You win! Rock crushes scissors.")
        else:
            print("You lose! Paper covers rock.")
    case 'scissors':
        if computer_choice == 'scissors':  
            print("It's a tie!")
        elif computer_choice == 'paper':
            print("You win! Scissors cut paper.")
        else:
            print("You lose! Rock crushes scissors.")
    case _:
            print("Invalid input! Please enter paper, rock, or scissors.")
