import json
import os
 
#First we write the words that need to be known in the code.
try:
    from termcolor import cprint
except ImportError:
    def cprint(*args, **kwargs):
        print(*args)
 
words = ["desk", "computer", "fatal", "jumping", "skunk", "cinema", "modem", "sweet", "headset"]
 
#We mix the words and write the number of lives we want into the code.
def game_preparation():
    global chosen_word, visible_word, life
    import random
    chosen_word = random.choice(words)
    visible_word = ["-"] * len(chosen_word)
    life = 10
 
#We ask the user for a letter. If no letter is entered, this will be an incorrect entry and will be repeated. If he wants to quit, he writes quit and the application closes. 
def get_letter():
    maintain = True
    while maintain:
        letter = input("Enter a letter: ")
        if letter.lower() == "quit":
            cprint("See you soon :)", color="red", on_color="on_blue")
            exit()
        elif len(letter) == 1 and letter.isalpha() and letter not in visible_word:
            maintain = False
        else:
            cprint("Incorrect Entry", color="red", on_color="on_grey")
    return letter.lower()
 
#If the letter selected by the user matches, the characters containing the word are updated. 
#When the user fails to match the letter, one health is reduced. 
#This situation continues until all letters are known or until the user's life is gone.
def game_loop():
    global visible_word, life
    while life > 0 and chosen_word != "".join(visible_word):
        cprint("word: " + "".join(visible_word), color="cyan", attrs=["bold"])
        cprint("life   : <" + "❤" * life + " " * (10 - life) + ">", color="cyan", attrs=["bold"])
        entered_letter = get_letter()
        positions = check_letter (entered_letter)
        if positions:
            for p in positions:
                visible_word[p] = entered_letter
        else:
            life -= 1
 
#It checks whether the incoming letter is in the word. 
def check_letter(entered_letter):
    pos = []
    for index, h in enumerate(chosen_word):
        if h == entered_letter:
            pos.append(index)
    return pos
 
#Shows the leaderboard.
def show_score_table():
    data = set_read()
    cprint("|Skor\t\tUser|", color="white", on_color="on_grey")
    cprint("|------------------------|", color="white", on_color="on_grey")
    for score, user in data["scores"]:
        cprint("|"+str(score) +"\t\t"+ user+" "*(9-len(user))+"|", color="white", on_color="on_grey")
    cprint("|------------------------|", color="white", on_color="on_grey")
 
#Updates the leaderboard with the last user's name and score 
def update_score_table():
    data = set_read()
    data["scores"].append((life, data["last_user"]))
    data["scores"].sort(key=lambda scpre_tuple: scpre_tuple[0], reverse=True)
    data["scores"] = data["scores"][:5]
    set_write(data)
 
#When the game is over, it writes to the screen whether we have won or not. 
def game_result():
    if life > 0:
        cprint("You Win :)", color="yellow", on_color="on_red")
        update_score_table()
    else:
        cprint("You Lose :(", color="red", on_color="on_yellow")
    show_score_table()
 
#It checks if the configuration file exists, checks if it is intact, creates the file with default values for corrupt or non-existent conditions. 
def check_file_if_not_create():
    write = False
    if os.path.exists("settings.json"):
        try:
            set_read()
        except ValueError as e:
            cprint("Error: ValueError(" + ",".join(e.args) + ")", color="red", on_color="on_blue", attrs=["bold"])
            os.remove("settings.json")
            write = True
    else:
        write = True
 
    if write:
        set_write({"scores": [], "last_user": ""})
 
#Reads the settings file. 
def set_read():
    with open("settings.json") as f:
        return json.load(f)
 
#Writes the data sent to the settings file. 
def set_write(data):
    with open("settings.json", "w") as f:
        json.dump(data, f)
 
#Prompts the user for a name. Then it sends the settings to print. 
def update_username():
    data = set_read()
    data["last_user"] = input("Your Username: ")
    while not data["last_user"] or len(data["last_user"]) > 9:
        data["last_user"] = input("Type 9 characters long: ")
    set_write(data)
 
#It shows the username of the user who logged in first and asks the user if this is you. 
def user_control():
    data = set_read()
    print("Last logged in: " + data["last_user"])
    if not data["last_user"]:
        update_username()
    elif input("Is that you?(y/n) ").lower() == "h":
        update_username()
 
#The main loop of the program 
def main():
    will_it_repeat = True
    check_file_if_not_create()
    cprint("Welcome to Hangman", color="cyan", on_color="on_magenta", attrs=["bold"])
    cprint("Help: You can exit by saying quit during the game", color="cyan", on_color="on_magenta", attrs=["bold"])
    cprint("-"*30, color="cyan", on_color="on_magenta", attrs=["bold"])
    show_score_table()
    user_control()
    while will_it_repeat:
        game_preparation()
        game_loop()
        game_result()
        if input("Continue?(y/n) ").lower() == "h":
            will_it_repeat = False
    cprint("See you soon :)", color="red", on_color="on_blue")
  
main()