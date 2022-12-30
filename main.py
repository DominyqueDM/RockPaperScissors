# Rock Paper Scissors

import random
import os
import re

def check_wanna_play():
    valid_responses = ['yes', 'no']
    while True:
        try:
            answer= input('Do you wish to play again? (Yes or No): ')
            if answer.lower() not in valid_responses:
                raise ValueError('yes or No input only')

            if answer.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing')
                exit()

        except ValueError as err:
            print(err)

def loser_art():
    print("LLLLLLLLLLL                 OOOOOOOOOO         SSSSSSSSSSSSSS EEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR")
    print("L:::::::::L               OO:::::::::::OO    SS::::::::::::::SE::::::::::::::::::::ER::::::::::::::::R")
    print("L:::::::::L              OO::::::::::::::OO S::::SSSSSS::::::SE::::::::::::::::::::ER::::::RRRRRR:::::R")
    print("LL:::::::LL             O:::::::OOO:::::::OS:::::S     SSSSSSSEE::::::EEEEEEEEE::::ERR:::::R     R:::::R")
    print("  L:::::L               O:::::O    O::::::OS:::::S              E:::::E       EEEEEE  R::::R     R:::::R")
    print("  L:::::L               O:::::O     O:::::OS:::::S              E:::::E               R::::R     R:::::R")
    print("  L:::::L               O:::::O     O:::::O S::::SSSS           E::::::EEEEEEEEEE     R::::RRRRRR:::::R")
    print("  L:::::L               O:::::O     O:::::O  SS:::::::SSSSS     E:::::::::::::::E     R:::::::::::::RR")
    print("  L:::::L               O:::::O     O:::::O    SSS:::::::::SS   E:::::::::::::::E     R::::RRRRRR:::::R")
    print("  L:::::L               O:::::O     O:::::O       SSSSSS:::::S  E::::::EEEEEEEEEE     R::::R     R:::::R")
    print("  L:::::L               O:::::O     O:::::O            S::::::S E:::::E               R::::R     R:::::R")
    print("  L:::::L         LLLLLLO::::::O   O::::::O            S::::::S E:::::E          EEEEER::::R     R:::::R")
    print("LL:::::::LLLLLLLLL:::::LO:::::::OOO:::::::OSSSSSSS     S::::::SEE::::::EEEEEEEEEE    ERR:::R     R:::::R")
    print("L::::::::::::::::::::::L OO::::::::::::OO  S::::::SSSSSS::::::SE:::::::::::::::::::::EER:::R     R:::::R")
    print("L::::::::::::::::::::::L   OO:::::::::OO   S::::::::::::::::SS E::::::::::::::::::::::ER:::R     R:::::R")
    print("LLLLLLLLLLLLLLLLLLLLLLLL     OOOOOOOOO      SSSSSSSSSSSSSSSS   EEEEEEEEEEEEEEEEEEEEEEEERRRRR     RRRRRRR")

def winner_art():
    print("⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀")
    print("⢠⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣄⣤⣤⣠")
    print("⢸⠀⡶⠶⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡷⠶⠶⡆⡼")
    print("⠈⡇⢷⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢰⠇⠀⢸⢁⡗")
    print("⠀⢹⡘⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡸⠀⢀⡏⡼⠀")
    print("  ⢳⡙⣆⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢠⠇⢀⠞⡼⠁⠀")
    print("⠀⠀⠀⠙⣌⠳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣫⠞⠀⠀")
    print("⠀⠀⠀⠀⠈⠓⢮⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣩⠞⠉⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠉⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠋⠁⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⢸⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠒⠓⠚⠓⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⣀⡀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀ ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡇⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡇⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠓⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠖⠃⠀⠀⠀⠀⠀")

def play():
    play_stat = True
    while play_stat:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Rock, Paper, Scissors- Shoot!')
        choice = input('Choose your weapon'
                       '[R]ock, [P]aper, or [S]cissors: ')

        if not re.match("[SsRrPp]", choice):
            print('Please choose a letter (S, R, P): ')
            print('[R]ock, [P]aper, [S]cissors')
            continue

        print(f'You chose: {choice}')

        bank_choices = ['R', 'P', 'S']
        comp_choice = random.choice(bank_choices)

        print("")
        print(f'I chose: {comp_choice}')

        if comp_choice == choice.upper():
            print('Tie!')
            play_stat = check_wanna_play()
        elif comp_choice == 'R' and choice.upper() == 'S':
            print('Rock beats scissors loser, I win')
            loser_art()
            play_stat = check_wanna_play()
        elif comp_choice == 'S' and choice.upper() == 'P':
            print('Scissors beats paper! I win like I expected')
            loser_art()
            play_stat = check_wanna_play()
        elif comp_choice == 'P' and choice.upper() == 'R':
            print('Paper beats rock you dweeb, I win')
            loser_art()
            play_stat = check_wanna_play()
        else:
            print("You've seem to have defeated me this time- don't get used to it. You win!\n")
            winner_art()
            play_stat = check_wanna_play()

if __name__ == '__main__':
    play()