# Word Guessing Game
import random
import string
import time


def guess_letter(guesses):
    while True:
        user_input = input("Guess a letter or the word: ").strip().lower()

        if user_input not in guesses:
            if len(user_input) == 1:
                if user_input not in string.ascii_letters:
                    print("You've entered an incorrect character. Please enter a letter.\n")
                else:
                    break
            elif user_input == "":
                print("Bad input, try again.\n")
            else:
                break
        else:
            print("You've already guessed that. Try again!")

    return user_input


def fill_word(word, guesses):
    guess_string = ""
    for character in word:
        if character not in string.ascii_letters:
            guess_string += character
        elif character in guesses:
            guess_string += character
        else:
            guess_string += '_'

    return guess_string


def run_game():
    remaining_guesses = 7
    guesses = []
    win = False

    word = random.choice(dictionary_list)
    dictionary_list.remove(word)

    while remaining_guesses > 0:
        print(fill_word(word, guesses))

        if remaining_guesses > 0:
            print(f"Number of guesses remaining: {remaining_guesses}")
            print("Your previous guesses: " + ", ".join(guesses))

        user_guess = guess_letter(guesses)
        guesses.append(user_guess)
        print("You guessed: " + user_guess + "\n")

        if user_guess == word:
            win = True
            break

        remaining_guesses -= 1


    print("The word is: " + word)

    if win is True:
        return True
    else:
        return False


if __name__ == '__main__':
    dictionary_list = []
    with open("words.txt", 'r') as f:
        for line in f:
            if line.__contains__("-.,"):
                pass
            else:
                dictionary_list.append(line.strip('\n'))
        f.close()

    wins = 0
    loses = 0

    print("Welcome to my Word Guessing Game. Do you have what it takes to win?\n")
    while True:
        if run_game():
            wins += 1
            print("You've won!")
        else:
            loses += 1
            print("You've lost...")

        print(f"Wins: {wins} | Loses: {loses}")
        play_again = input("Care to play again? Press Enter to play again or enter any character to exit: ")
        if play_again == '':
            pass
        elif play_again:
            print("Thanks for playing!")
            exit()
