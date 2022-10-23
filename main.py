import random
import sys
from termcolor import colored

human_score = 0
comp_score = 0
draw_score = 0
Rock = colored("Rock", "yellow")
Paper = colored("Paper", "cyan")
Scissors = colored("Scissors", "blue")

weapon_list = [Rock, Paper, Scissors]

win_score = abs(int(input("First to ___ wins: ")))


def human_weapon():
    human_input = input("R = Rock, P = Paper, & S = Scissors\nYour weapon: ")
    if human_input == "R" or human_input == "r":
        return Rock
    elif human_input == "P" or human_input == "p":
        return Paper
    elif human_input == "S" or human_input == "s":
        return Scissors


def decider(hw, cw):
    global human_score
    global comp_score
    global draw_score

    print(f"\n{hw} vs {cw}")
    win_msg = colored("You've won!", "green")
    if hw is None:
        return print(colored("Error: please pick a weapon.", "red"))
    elif hw == Rock and cw == Scissors:
        print(win_msg)
        human_score += 1
    elif hw == Paper and cw == Rock:
        print(win_msg)
        human_score += 1
    elif hw == Scissors and cw == Paper:
        print(win_msg)
        human_score += 1
    elif hw == cw:
        print(colored("It's a draw!", "magenta"))
    else:
        print(colored("You've lost.", "red"))
        comp_score += 1
    print(f"\nScore: {comp_score} to {human_score_color()}\n ")


def human_score_color():
    human_score_green = colored(str(human_score), "green")
    human_score_yellow = colored(str(human_score), "yellow")
    human_score_red = colored(str(human_score), "red")
    humans_green = colored("humans", "green")
    comp_red = colored("computer", "red")
    if human_score > comp_score:
        return f"{human_score_green}\nThe {humans_green} are winning!"
    elif human_score == comp_score:
        return f"{human_score_yellow}\nIt's a tie for now"
    else:
        return f"{human_score_red}\nThe {comp_red} is winning!"


while True:
    if human_score >= win_score:
        print(colored("You've won the game!", "green"))
        sys.exit()
    elif comp_score >= win_score:
        print(colored("The computer has won the game.", "red"))
        sys.exit()
    else:
        decider(human_weapon(), random.choice(weapon_list))
