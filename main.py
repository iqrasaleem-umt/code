
import random

# Problem 1
def play_round_problem_1(round_num, score):
    print(f"Round {round_num}")
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number is {user_number}")
    guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
    
    if guess not in ["higher", "lower"]:
        print("Invalid input, please type 'higher' or 'lower'.")
        return score  

    if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    print(f"Your score is now {score}\n")
    return score

def main_problem_1():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    rounds = 5
    score = 0
    
    for round_num in range(1, rounds + 1):
        score = play_round_problem_1(round_num, score)

    print(f"Thanks for playing! Your final score is {score}")

# Problem 2
def play_game_problem_2():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)
    
    print(f"The computer's number is {computer_number}")
    print(f"Your number is {user_number}")
    
    guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
    
    print(f"You guessed that your number is {guess} than the computer's.")

# Problem 3
def start_game_problem_3():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)
    
    print(f"The computer's number is {computer_number}")
    print(f"Your number is {user_number}")
    
    guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
    
    if user_number == computer_number:
        print("The computer's number is the same as yours, so the computer wins.")
    elif (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

# Problem 4
NUM_ROUNDS = 3

def play_round_problem_4(round_num):
    print(f"Round {round_num}")
    
    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)
    
    print(f"Your number is {user_number}")
    
    guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
    
    if user_number == computer_number:
        print("The computer's number is the same as yours, so the computer wins.")
    elif (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    print()

def start_game_problem_4():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    for round_num in range(1, NUM_ROUNDS + 1):
        play_round_problem_4(round_num)

# Problem 5
NUM_ROUNDS = 5

def play_round_problem_5(round_num, score):
    print(f"Round {round_num}")
    
    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)
    
    print(f"Your number is {user_number}")
    
    while True:
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        if guess in ["higher", "lower"]:
            break
        else:
            print("Please enter either 'higher' or 'lower':")
    
    if user_number == computer_number:
        print("The computer's number is the same as yours, so the computer wins.")
    elif (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    print(f"Your score is now {score}\n")
    return score

def start_game_problem_5():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0
    
    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round_problem_5(round_num, score)
    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# To execute one of the problems, you can uncomment the corresponding line below:

main_problem_1()
play_game_problem_2()
start_game_problem_3()
start_game_problem_4()
start_game_problem_5()
