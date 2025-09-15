from words import add_words, del_words, show_words, ensure_words_file, letters
from game import hangman_game, choose_word_singleplayer, get_word_multiplayer
from utils import clear_screen, pause


def main():
    f=True # stands for 'first', it is here to clear not the screen when the menu appears first, else the big message here wouldn't be displayed
    ensure_words_file() # create the words.json file if it does not exist
    clear_screen()
    print(
        "---------------------------------------------------------------\n" \
        "----------------------- Welcome to Hangman --------------------\n" \
        "---------------------------------------------------------------\n" \
        "------------------ Created by Lorenz9999999999 ----------------\n" \
        "------------- https://github.com/Lorenz9999999999/ ------------\n" \
        "---------------------------------------------------------------\n" \
        "\n\n\n"
    )
    while True:
        if not f:
            clear_screen()
        f=False
        print(
            "----- MENU -----\n" \
            "Play singleplayer: 1\n" \
            "Play multiplayer: 2\n" \
            "Add words for singleplayer: 3\n" \
            "Delete words for singleplayer: 4\n" \
            "Show all possible words in singleplayer: 5\n" \
            "Exit: x\n"
        )
        mode=input("")

        if mode == "1":
            clear_screen()
            word=choose_word_singleplayer()
            if not word:
                continue # don't start the game if there are no words available (I have no idea what is the exakt difference between break, pass, return and continue)
            hangman_game(word)
        elif mode == "2":
            first=True # for the look
            while True:
                word=get_word_multiplayer(first)
                if "_" in word:
                    print("'_' is no valid character in a word.")
                elif not any(char in letters for char in word):
                    print("This is no valid word.")
                else:
                    break
                first=False
            hangman_game(word)
        elif mode=="3":
            add_words()
        elif mode=="4":
            del_words()
        elif mode=="5":
            show_words()
        elif mode.lower() == "x":
            print("\n\nGame endet.")
            break
        else:
            print("Not a valid selection.")
            pause()
    
    

if __name__ == "__main__":
    main()