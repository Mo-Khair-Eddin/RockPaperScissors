import time
from time import sleep
import sys
import random

#print('Reminder: you can input "0" to list this again.')
#print('1) Rock')
#print('2) Paper')
#print('3) Scissors')

# lists of possible typos which choosing a weapon
rock_list = ["r", "ro", "roc", "rock", "rok", "rokc", "kocr", "ockr", "ock", "korc", "kcro", "orck", "orkc"]
paper_list = ["paper", "pappar", "pepper", "papr", "p", "pa", "pap", "pep", "pape", "pepe", "papar", "pepar", "2"]
scissors_list = ["srossics", "scissors", "s", "sci", "sc", "sissors", "sisor", "scissor", "scisser", "scissers", "scisors", "ssissors", "scisors", "scis", "sciss", "scisso", "scisse"]
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
# I want it to set question to rock then continue with the if statements. I think I can do this by replicating
# the entire code again but only for this one portion, but that's seems like over-kill
# I could just have it print "It choose rock! Go rock next game! :D" but that's a poor comprise that I do not like
    if question in pick_for_me_list:
# Might work perfectly if the others were functions. Then you could easily call on the function depending on the no.
        picked_weapon = random.randint(0, 2)
# if the randomly chosen weapon for the player is a rock
        if picked_weapon == 0:
            print("We picked rock for you.")
            if comp_weapon == 0:
                print("The computer chose rock as well."); sleep(comp_delay_pick)
                sys.stdout.write('Result'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('\nDraw!'); sleep(0.1)
                sys.stdout.write('\n')
                pick_one()
            elif comp_weapon == 1:
                print("The computer chose paper."); sleep(comp_delay_pick)
                sys.stdout.write('Result'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('\nDefeat'); sleep(0.1)
                sys.stdout.write('\n')
                pick_one()
            elif comp_weapon == 2:
                print("The computer chose scissors."); sleep(comp_delay_pick)
                sys.stdout.write('Result'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('.'); sleep(random.uniform(lower_range, upper_range))
                sys.stdout.write('\nVictory!'); sleep(0.1)
                sys.stdout.write('\n')
                pick_one()
# if the player inputted a string that's in rock_list
    elif question in rock_list:
# if the randomly generated number = 0 (0 = rock) & the player choose rock = draw
        if comp_weapon == 0:
            print("Rock! Nice choice!"); sleep(choice_delay)
            print("Great minds think alike; the computer chose rock as well."); sleep(comp_delay_draw)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nDraw!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
# if the randomly generated number = 1 (1 = paper) & the player choose rock = defeat
        if comp_weapon == 1:
            print("Rock! Nice choice!"); sleep(choice_delay)
            print("unfortunately, the computer chose paper."); sleep(comp_delay_lose)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nDefeated!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
# if the randomly generated number = 2 (2 = scissors) & the player choose rock = victory
        if comp_weapon == 2:
            print("Rock! Nice choice!"); sleep(choice_delay)
            print("The computer chose scissors."); sleep(comp_delay_win)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nVictory!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
# if the player inputted a string that's in paper_list
    elif question in paper_list:
# if the randomly generated number = 0 (0 = rock) & the player choose paper = victory
        if comp_weapon == 0:
            print("Paper! Nice choice!"); sleep(choice_delay)
            print("The computer chose rock."); sleep(comp_delay_win)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nVictory!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
# if the randomly generated number = 1 (1 = paper) & the player choose paper = draw
        if comp_weapon == 1:
            print("Paper! Nice choice!"); sleep(choice_delay)
            print("Great minds think alike; the computer chose paper as well."); sleep(comp_delay_draw)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nDraw!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
# if the randomly generated number = 2 (2 = scissors) & the player choose paper = defeat
        if comp_weapon == 2:
            print("Paper! Nice choice!"); sleep(choice_delay)
            print("Unfortunately, the computer chose scissors."); sleep(comp_delay_lose)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nDefeated!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
# if the player inputted a string that's in scissor_list
    elif question in scissors_list:
# if the randomly generated number = 0 (0 = rock) & the player choose scissors = defeat
        if comp_weapon == 0:
            print("Scissors! Nice choice!"); sleep(choice_delay)
            print("Unfortunately, the computer chose rock."); sleep(comp_delay_lose)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nDefeated!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
# if the randomly generated number = 1 (1 = paper) & the player choose scissors = victory
        if comp_weapon == 1:
            print("Scissors! Nice choice!"); sleep(choice_delay)
            print("The computer chose paper."); sleep(comp_delay_win)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nVictory!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
# if the randomly generated number = 2 (2 = scissors) & the player choose scissors = draw
        if comp_weapon == 2:
            print("Scissors! Nice choice!"); sleep(choice_delay)
            print("It seems great minds think alike; the computer chose scissors as well."); sleep(comp_delay_draw)
            sys.stdout.write('Result'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('.'); sleep(random.uniform(lower_range,upper_range))
            sys.stdout.write('\nDraw!'); sleep(0.1)
            sys.stdout.write('\n')
            pick_one()
    elif question in thinking_list:
        print("Can't think of what to choose? Maybe try \"pick for me\".")
        pick_one()
# If non of the above occur, recall the function
    else:
        pick_one()


pick_one()
