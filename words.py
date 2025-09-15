from utils import clear_screen, pause
import os
import json

# i know i can do that better, but i only found out when i already had it like that and i didn't want to change it anymore
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


WORDS_FILE="words.json" # the file where the words that the computer can choise are saved

def show_words():
    clear_screen()
    words=load_words()
    if len(words)==0:
        print("No words available. Come on, add a bunch!")
        pause()
        return
    for word in words:
        print(word)
    print("\n")
    pause()
    clear_screen()

def add_words():
    words=load_words()
    while True:
        clear_screen()
        word=input("\nEnter a new word (or press only enter to cancel): ").strip()
        if not word:
            break
        if "_" in word:
            print("\n'_' is no valid character in a word.")
            pause()
            continue
        elif not any(char in letters for char in word):
            print("\nThis is no vaild word.")
            pause()
            continue
        elif word in words:
            print("\nThis word already exists.")
            pause()
            continue
        else:
            words.append(word)
            save_words(words)
            print(f"\n'{word}' was added.")
        
        again=input("\nDo you want to add more words? (y/n) ").lower()
        if again != "y":
            break

def del_words():
    words=load_words()
    clear_screen()
    if len(words)==0:
        print("No words available. Come on, add a bunch!")
        pause()
        return
    while True:
        clear_screen()
        for i, w in enumerate(words, start=1):
            print(f"{i}: {w}")
        number=input("Enter the number of the word you want to delete (or press only enter to cancel): ")
        if not number:
            break
        if not number.isdigit():
            print("This isn't a valid entry.")
            pause()
            continue
        number=int(number)
        
        if number < 1 or number > len(words):
            print("This isn't a valid number.")
            pause()
            continue
        word_to_rm=words[number - 1]
        words.remove(word_to_rm)
        save_words(words)
        print(f"'{word_to_rm}' was deleted.")
        if words:
            again=input("\nDo you want do delete more words? (y/n) ").lower()
        else:
            break
        clear_screen()
        if again != "y":
            break

def ensure_words_file():
    if not os.path.exists(WORDS_FILE): # only create if the file does not exist (I know, this if statement exists 3 times... what the hell)
        default=[
            "python",
            "computer",
            "coding",
            "hangman",
            "player"
        ]
        with open(WORDS_FILE, "w", encoding="utf-8") as f:
            json.dump(default, f, indent=4, ensure_ascii=False)

def load_words():
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_words(words):
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, indent=4, ensure_ascii=False)
