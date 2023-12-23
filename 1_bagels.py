import random


MAX_GUESSES = 10
NUM_DIGITS = 3


def get_secret_number():
    numbers = list("0123456789")
    random.shuffle(numbers)
    return numbers[0:NUM_DIGITS]


def check_guess(guess, secret_number):
    count = 0
    
    if guess == secret_number:
        print("you got it")
        return 1
    
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            print(" fermi")
            continue
        elif guess[i] in secret_number:
            print("pico")
        else:
            count+=1
            
    if(count >= NUM_DIGITS):
        print("bagels")
                    

def game():
    print(f"I am thinking of a {NUM_DIGITS} number with no repeated digits.\nTry to guess what the number is with the following clues...\n\
When I say\t\tIt means\nPico\t\tOne digit is correct but in the wrong position\nFermi\t\tOne digit is correct and in the right position\n\
Bagels\t\tNo digit is correct")
    print(f"\nI have thought up a number.\nYou have {MAX_GUESSES} tries to guess it...\n")
    secret_number = get_secret_number()
    print(secret_number)
    for i in range(MAX_GUESSES):
        print(f"\nGuess no. {i}\n")
        x = list(input(">"))
        
        while(len(x) > NUM_DIGITS or (len([j for j in x if not j.isdigit()]))):
            print(f"\nError...Enter Guess no. {i}\n")
            x = list(input(">"))
        
        if(check_guess(x,secret_number)):
            break
    else:
        print(f"\nOh that's too bad, you didn't get it...Try again next time.\nThe secret number was : {secret_number}")
    print("\nDo you want to play again? (Y/N)")
    if input(">").lower() == "y":
        return 1

def main():
    while(game()):
        game()

if (__name__) == '__main__':
    main()