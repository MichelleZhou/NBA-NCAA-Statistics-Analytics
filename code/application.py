import tkinter as tk
import time
import os
from queries import *

def printHomeMenu():
    print("\nWhat would you like to do today?")
    print("Enter a number to get started or 'Quit' to exit.\n")
    print("1. NCAA Player Lookup")
    print("2. NBA Player Lookup")
    print("3. Annual NCAA Statistics")
    print("4. Annual NBA Statistics")
    print("5. Something Fun!")

def redirectMenu(user_input):
    if (user_input == '1'): ncaaLookup()
    elif (user_input == '2'): nbaLookup()
    elif (user_input == '3'):
        print("You selected Annual NCAA Statistics")
    elif (user_input == '4'):
        print("You selected Annual NBA Statistics")
    elif (user_input == '5'):
        print("You selected Something Fun!")
    else:
        print("Please check your selection: {}".format(user_input))


def ncaaLookup():
    print("You selected NCAA Player Lookup...")
    player = input("Who do you wish to look up? ==> ")
    results = ncaa_player_lookup(player)

    print("\n"+"=" * 50)
    print("NCAA Data for {}:".format(player))
    if (len(results) == 0):        
        print("Player {} was not on any NCAA team\nbetween 2008 and 2010".format(player))
    else:
        # Print NCAA data that was found.
        school, yr, pos = [], [], [] 
        tot_game, tot_fg, tot_fgatt, tot_thrp, tot_thrpatt, tot_rb = 0, 0, 0, 0, 0, 0
        tot_ass, tot_bl, tot_st, tot_pt = 0, 0, 0, 0

        for r in results[0]:
            if (r[2] not in school): school.append(r[2])
            if (r[1] not in yr): yr.append(r[1])
            if (r[3] not in pos): pos.append(r[3])

            tot_game += r[4]
            tot_fg += r[5]
            tot_fgatt += r[6]
            tot_thrp += r[7]
            tot_thrpatt += r[8]
            tot_rb += r[9]
            tot_ass += r[10]
            tot_bl += r[11]
            tot_st += r[12]
            tot_pt += r[13]

        print("School(s): ",end='')
        print( *school, sep=', ', end='\n')
        print("Year(s): ", end='')
        print( *yr, sep=', ', end='\n')
        print("Position(s): ", end='')
        print(*pos, sep=' ', end='\n')
        print("Total Games Played: {}".format(tot_game))

        print("\nField Goal %: {:.2%}".format(float(tot_fg)/tot_fgatt))
        print("Three Point %: {:.2%}".format(float(tot_thrp)/tot_thrpatt))
        print("Average Rebounds/Game: {:.3f}".format(float(tot_rb)/tot_game))
        print("Average Assists/Game: {:.3f}".format(float(tot_ass)/tot_game))
        print("Average Blocks/Game: {:.3f}".format(float(tot_bl)/tot_game))
        print("Average Steals/Game: {:.3f}".format(float(tot_st)/tot_game))
        print("Average Points/Game: {:.3f}".format(float(tot_pt)/tot_game))
        print("="*50)


        print("\n"+"=" * 50)
        print("NBA Data for {}".format(player))
        if (len(results) == 1):
            print("Player {} was not on any NBA team\nbetween 2000 and 2018.".format(player))
        else:
            # Print NBA data that was found.            
            team, yr, pos = [], [], []
            tot_game, tot_fg, tot_fgatt, tot_thrp, tot_thrpatt, tot_rb = 0, 0, 0, 0, 0, 0
            tot_ass, tot_bl, tot_st, tot_pt = 0, 0, 0, 0

            for r in results[1]:
                if (r[0] not in team): team.append(r[0])
                if (r[1] not in yr): yr.append(r[1])
                if (r[2] not in pos): pos.append(r[2])

                tot_game += r[3]
                tot_fg += r[4]
                tot_fgatt += r[5]
                tot_thrp += r[6]
                tot_thrpatt += r[7]
                tot_rb += r[8]
                tot_ass += r[9]
                tot_bl += r[10]
                tot_st += r[11]
                tot_pt += r[12]

            print("Team(s): ",end='')
            print( *team, sep=', ', end='\n')
            print("Year(s): ", end='')
            print( *yr, sep=', ', end='\n')
            print("Position(s): ", end='')
            print(*pos, sep=' ', end='\n')
            print("Total Games Played: {}".format(tot_game))

            print("\nField Goal %: {:.2%}".format(float(tot_fg)/tot_fgatt))
            print("Three Point %: {:.2%}".format(float(tot_thrp)/tot_thrpatt))
            print("Average Rebounds/Game: {:.3f}".format(float(tot_rb)/tot_game))
            print("Average Assists/Game: {:.3f}".format(float(tot_ass)/tot_game))
            print("Average Blocks/Game: {:.3f}".format(float(tot_bl)/tot_game))
            print("Average Steals/Game: {:.3f}".format(float(tot_st)/tot_game))
            print("Average Points/Game: {:.3f}".format(float(tot_pt)/tot_game))
        print("="*50)
        
    time.sleep(2)


def nbaLookup():
    print("You selected NBA Player Lookup...")
    player = input("Who do you wish to look up? ==> ")
    results = nba_player_lookup(player)


    print("\n"+"=" * 50)
    print("NBA Data for {}".format(player))
    if (len(results) == 0):
        print("Player {} was not on any NBA team\nbetween 2000 and 2018.".format(player))
    else:
        # Print NBA data that was found.            
        team, yr, pos = [], [], []
        tot_game, tot_fg, tot_fgatt, tot_thrp, tot_thrpatt, tot_rb = 0, 0, 0, 0, 0, 0
        tot_ass, tot_bl, tot_st, tot_pt = 0, 0, 0, 0

        for r in results[0]:
            if (r[0] not in team): team.append(r[0])
            if (r[1] not in yr): yr.append(r[1])
            if (r[2] not in pos): pos.append(r[2])

            tot_game += r[3]
            tot_fg += r[4]
            tot_fgatt += r[5]
            tot_thrp += r[6]
            tot_thrpatt += r[7]
            tot_rb += r[8]
            tot_ass += r[9]
            tot_bl += r[10]
            tot_st += r[11]
            tot_pt += r[12]

        print("Team(s): ",end='')
        print( *team, sep=', ', end='\n')
        print("Year(s): ", end='')
        print( *yr, sep=', ', end='\n')
        print("Position(s): ", end='')
        print(*pos, sep=' ', end='\n')
        print("Total Games Played: {}".format(tot_game))

        print("\nField Goal %: {:.2%}".format(float(tot_fg)/tot_fgatt))
        print("Three Point %: {:.2%}".format(float(tot_thrp)/tot_thrpatt))
        print("Average Rebounds/Game: {:.3f}".format(float(tot_rb)/tot_game))
        print("Average Assists/Game: {:.3f}".format(float(tot_ass)/tot_game))
        print("Average Blocks/Game: {:.3f}".format(float(tot_bl)/tot_game))
        print("Average Steals/Game: {:.3f}".format(float(tot_st)/tot_game))
        print("Average Points/Game: {:.3f}".format(float(tot_pt)/tot_game))
        print("="*50)

        print("\n"+"=" * 50)
        print("NCAA Data for {}:".format(player))
        if (len(results) == 1):        
            print("Player {} was not on any NCAA team\nbetween 2008 and 2010.".format(player))
        else:
            # Print NCAA data that was found.
            school, yr, pos = [], [], [] 
            tot_game, tot_fg, tot_fgatt, tot_thrp, tot_thrpatt, tot_rb = 0, 0, 0, 0, 0, 0
            tot_ass, tot_bl, tot_st, tot_pt = 0, 0, 0, 0

            for r in results[1]:
                if (r[2] not in school): school.append(r[2])
                if (r[1] not in yr): yr.append(r[1])
                if (r[3] not in pos): pos.append(r[3])

                tot_game += r[4]
                tot_fg += r[5]
                tot_fgatt += r[6]
                tot_thrp += r[7]
                tot_thrpatt += r[8]
                tot_rb += r[9]
                tot_ass += r[10]
                tot_bl += r[11]
                tot_st += r[12]
                tot_pt += r[13]

            print("School(s): ",end='')
            print( *school, sep=', ', end='\n')
            print("Year(s): ", end='')
            print( *yr, sep=', ', end='\n')
            print("Position(s): ", end='')
            print(*pos, sep=' ', end='\n')
            print("Total Games Played: {}".format(tot_game))

            print("\nField Goal %: {:.2%}".format(float(tot_fg)/tot_fgatt))
            print("Three Point %: {:.2%}".format(float(tot_thrp)/tot_thrpatt))
            print("Average Rebounds/Game: {:.3f}".format(float(tot_rb)/tot_game))
            print("Average Assists/Game: {:.3f}".format(float(tot_ass)/tot_game))
            print("Average Blocks/Game: {:.3f}".format(float(tot_bl)/tot_game))
            print("Average Steals/Game: {:.3f}".format(float(tot_st)/tot_game))
            print("Average Points/Game: {:.3f}".format(float(tot_pt)/tot_game))
        print("="*50)
              
    time.sleep(2)



if __name__ == '__main__':
    
    intro = ( "=====================================================\n"
              "Welcome to the NBA/NCAA Analytics Tool.\n"
              "====================================================="
    )
    print(intro) 
    printHomeMenu()
    user_input = input('\n').strip().lower()

    while user_input != 'quit':
        redirectMenu(user_input)

        time.sleep(0.4)
        printHomeMenu()
        user_input = input('\n').strip().lower()
