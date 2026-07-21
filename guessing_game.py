def game():
    print("Welcome to the game!")
    print("You have 3 chances to guess the correct number between 1 and 10.")
    
    import random
    number_to_guess = random.randint(1, 10)
    attempts = 3
    
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        
        if guess == number_to_guess:
            print("Congratulations! You've guessed the correct number.")
            break
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

game()