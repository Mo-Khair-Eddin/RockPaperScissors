import time
from time import sleep
import sys
import random

# lists of possible typos which choosing a weapon
rock_list = ["r", "rr", "ro", "roc", "rock", "rok", "rokc", "kocr", "ockr", "ock", "korc", "kcro", "orck", "orkc"]
paper_list = ["paper", "pappar", "pepper", "papr", "p", "pp", "pa", "pap", "pep", "pape", "pepe", "papar", "pepar", "2"]
scissors_list = ["srossics", "scissors", "s", "ss", "sci", "sc", "sissors", "sisor", "scissor", "scisser", "scissers", "scisors", "ssissors", "scisors", "scis", "sciss", "scisso", "scisse"]
# thinking list & possible typos for "pick for me"
thinking_list = ["hhm", "hhmm", "hmmm", "hmmmm", "hmmmmmm", "hmmmmmmmmmmmm", "hm", "hmm", "uhh", "i dont know", "idk", "dont know" "don't know", "i don't know", "cant choose", "can't choose", "can't pick", "cant pick", "idfk"]
pick_for_me_list = ["pick 4me", "pick4 me", "pick forme", "pck for me", "pock for me", "pick for m", "pick for e", "pick for me", "pickforme", "pick4me", "pick 4 me", "pickfor me", "pick forme", "pick for me"]

# range of delay for the "results..." output
upper_range = 0.2
lower_range = 0.1
# delay duration after displaying the computer's weapon
# draw = lengthiest text
# win = shortest text
comp_delay_draw = 1.5
comp_delay_win = 0.5
comp_delay_lose = 0.8
# delay after repeating the player's weapon
choice_delay = 1
# delay for the "pick for me" easter egg computer result (all the same length)
comp_delay_pick = 1

def result_calc(player_weapon, comp_message, comp_delay, result_draw):
    print(player_weapon + " Nice choice!"); sleep(choice_delay)
    print(comp_message)
    sleep(comp_delay)
    sys.stdout.write('Result'); sleep(random.uniform(lower_range, upper_range))
    sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
    sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
    sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
    sys.stdout.write('\n' + result_draw); sleep(0.1)
    sys.stdout.write('\n')
    pick_one()

def pick_one():
# randomly generated number indicating the computer's move:
# 0 = rock
# 1 = paper
# 2 = scissors
    comp_weapon = random.randint(0, 2)
    while True:
        try:
            question = str(input('Your weapon of choice: '))
            question.lower()
            break
        except:
            print("That's not a valid option!")

    if question in pick_for_me_list:
        picked_weapon = random.randint(0, 2)
        if picked_weapon == 0:
            if comp_weapon == 0:
                result_calc("We chose rock for you.", "The clash of computers has lead the opposing computer to pick rock as well", comp_delay_draw, "Draw!")
                pick_one()
            if comp_weapon == 1:
                result_calc("We chose rock for you.", "Unfortunately, the opposing computer picked paper.", comp_delay_lose, "Defeat!")
                pick_one()
            if comp_weapon == 2:
                result_calc("We chose rock for you.", "The opposing computer picked scissors.", comp_delay_win, "Victory!")
                pick_one()
        elif picked_weapon == 1:
            if comp_weapon == 0:
                result_calc("We chose paper for you", "The opposing computer chose rock", comp_delay_win, "Victory!")
                pick_one()
            if comp_weapon == 1:
                result_calc("We chose paper for you", "Great computer minds think alike. The opposing computer chose paper as well.", comp_delay_draw, "Draw!")
                pick_one()
            if comp_weapon == 2:
                result_calc("We chose paper for you", "Unfortunately, the opposing computer chose scissors.", comp_delay_lose, "Defeated!")
                pick_one()
        elif picked_weapon == 2:
            if comp_weapon == 0:
                result_calc("We chose scissors for you.", "Unfortunately, the computer chose rock.", comp_delay_lose, "Defeated!")
                pick_one()
            if comp_weapon == 1:
                result_calc("We chose scissors for you.", "The computer chose paper.", comp_delay_win, "Victory!")
                pick_one()
            if comp_weapon == 2:
                result_calc("We chose scissors for you", "The clash of computers has lead the opposing computer to pick rock as well", comp_delay_draw, "Draw!")
                pick_one()

    elif question in rock_list:
        if comp_weapon == 0:
            result_calc("Rock!", "Great minds think alike. The computer chose rock as well.", comp_delay_draw, "Draw!")
            pick_one()
        if comp_weapon == 1:
            result_calc("Rock!", "Unfortunately, the computer chose paper.", comp_delay_lose, "Defeated!")
            pick_one()
        if comp_weapon == 2:
            result_calc("Rock!", "The computer chose scissors.", comp_delay_win, "Victory!")
            pick_one()
    elif question in paper_list:
        if comp_weapon == 0:
            result_calc("Paper!", "The computer chose rock", comp_delay_win, "Victory!")
            pick_one()
        if comp_weapon == 1:
            result_calc("Paper!", "Great minds think alike. The computer chose paper as well.", comp_delay_draw, "Draw!")
            pick_one()
        if comp_weapon == 2:
            result_calc("Paper!", "Unfortunately, the computer chose scissors.", comp_delay_lose, "Defeated!")
            pick_one()
    elif question in scissors_list:
        if comp_weapon == 0:
            result_calc("Scissors!", "Unfortunately, the computer chose rock.", comp_delay_lose, "Defeated!")
            pick_one()
        if comp_weapon == 1:
            result_calc("Scissors!", "The computer chose paper.", comp_delay_win, "Victory!")
            pick_one()
        if comp_weapon == 2:
            result_calc("Scissors!", "Great minds think alike. The computer chose scissors as well.", comp_delay_draw, "Draw!")
            pick_one()
    elif question in thinking_list:
        print("Can't think of what to choose? Maybe try \"pick for me\".")
        pick_one()
    else:
        pick_one()


pick_one()
