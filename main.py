import random

while True:
    user_action = input("Enter a choice(R, P, S): ")
    possible_action = ["R", "P", "S"]
    computer_action = random.choice(possible_action)
    print(f"\nYou chose{user_action}, computer chose{computer_action}.\n")
    print(f"\nuser_action{user_action}:computer_action{computer_action}.\n")

    if user_action == computer_action:
        print(f"It's a Tie!")
        continue
    elif user_action == "R":
        if computer_action == "S":
            print("R smashes S! You Win.")
        else:
            print("P covers R! You lose.")
            break
    elif user_action == "P":
        if computer_action == "R":
            print("P covers R! You Win.")
        else:
            print("S cut P! You lose.")
            break
    elif user_action == "S":
        if computer_action == "P":
            print("S cut P! You win.")
        else:
            print("R smashes S! You lose.")
            break
    else:
        print("Error! Enter a valid option next time")
        break