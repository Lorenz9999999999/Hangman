################ the classic import shit #########################
from utils import pause, clear_screen
from graphics import get_hangman_state
from words import ensure_words_file, WORDS_FILE, load_words, letters
import os
import random

################# get/chooce the word #####################

def choose_word_singleplayer():
    if not os.path.exists(WORDS_FILE):
        ensure_words_file() # create the words.json file if it doesn't exist
    words=load_words()
    if len(words)==0:
        print("No words available. Come on, add a bunch!")
        pause()
        return None # return None if there are no words available
    return random.choice(words).lower()

def get_word_multiplayer(first):
    if first:
        clear_screen()
    word=input("Player 1, enter a word: ").lower()
    clear_screen()
    return word

#################### display the word ##########################

def display_word(word, guessed_letters):
    global letters
    display=""
    for letter in word:
        if letter in guessed_letters:
            display+=letter + " "
        elif letter not in letters: # display the character if it isn't a letter
            display+=letter + " "
            if not letter in guessed_letters:
                guessed_letters.append(letter) # add the character that isn't a letter to the already guessed letters, because else you have to guess the character that it will notice that you have guessed the word
        else:
            display+="_ "
    return display.strip()


################ game ####################

def hangman_game(word):
    global guessed
    guessed=False
    guessed_letters=[]
    attempts=11

    while attempts > 0: # the mainloop
        print("\n" + display_word(word, guessed_letters) + "\n")
        guess=input("Guess letter or a word: ").lower()
        if not guess in letters and len(guess)==1:
            clear_screen()
            print("Only letters can be guessed.")
            print(get_hangman_state(attempts)) # display the hangman graphic
            continue
        clear_screen()

        if len(guess)==1:
            if guess in guessed_letters:
                print("\nYou have already guessed this letter.")
            elif guess in word:
                print("\nCorrect!")
                guessed_letters.append(guess)
            else:
                print("\nWrong")
                guessed_letters.append(guess)
                attempts-=1
        else:
            if guess==word:
                guessed=True
                print(f"\nCongratulations! You guessed the word '{word}'.\n")
                pause()
                break
            else:
                print("\nFalsch!")
                attempts-=1
        if all(letter in guessed_letters for letter in word):
            guessed=True
            print(f"\nGCongratulations! You guessed the word '{word}'.\n")
            pause()
            break
        
        print(get_hangman_state(attempts)) # display the hangman graphic (again)
    if not guessed:
        print(f"\nGame over! The word was: {word}")
        pause()
    return