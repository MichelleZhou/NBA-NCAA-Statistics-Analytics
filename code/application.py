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
    elif (user_input == '3'): annualNCAA()
    elif (user_input == '4'): annualNBA()
    elif (user_input == '5'):
        print("You selected Something Fun!")
    else:
        print("Please check your selection: {}".format(user_input))

def printNCAAMenu():
    #Annual NCAA Menu
    print("Which of the following annual NCAA statistics would you\nbe interested in seeing?\n")
    print("Enter a number to get started.")
    print("1. Average, minimum and maximum height")
    print("2. Top 10 offensive players of the year")
    print("3. Top 10 defensive players of the year")
    print("4. Top 10 overall players of the year")
    print("5. Highest scorers of the year")
    print("6. Worst overall players of the year")

def printNBAMenu():
    #Annual NBA Menu
    print("Which of the following annual NBA statistics would you\nbe interested in seeing?\n")
    print("Enter a number to get started.")
    print("1. Average, minimum and maximum height")
    print("2. Top 10 offensive players of the year")
    print("3. Top 10 defensive players of the year")
    print("4. Top 10 overall players of the year")
    print("5. Highest scorers of the year")
    print("6. Worst overall players of the year")



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
                tot_bl += r[11]
                tot_st += r[10]
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
            tot_bl += r[11]
            tot_st += r[10]
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


def annualNCAA():
    printNCAAMenu()
    user_input = input('\n').strip().lower()
    
    while(True):
        # Returns average, maximum, and minimum height of players for inputted year.
        if (user_input == '1'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2008', '2009', '2010']):
                yr = input("Enter a valid year (2008 - 2010) ==> ").strip()

            results = annual_ncaa_height(yr)
            print("="*50)
            print("Average height: {:.3f}".format(results[0][0]))
            print("Maximum height: {:.3f}".format(results[0][1]))
            print("Minimum height: {:.3f}".format(results[0][2]))
            print("="*50)
            time.sleep(1)
            return
        
        # Return best offensive players for inputted year.
        elif (user_input =='2'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2008', '2009', '2010']):
                yr = input("Enter a valid year (2008 - 2010) ==> ").strip()

            results = annual_ncaa_top10_offense(yr)
            print("="*50)
            print("Best offensive players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return
        
        # Return best defensive players for inputted year.
        elif (user_input == '3'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2008', '2009', '2010']):
                yr = input("Enter a valid year (2008 - 2010) ==> ").strip()
            
            results = annual_ncaa_top10_defense(yr)
            print("="*50)
            print("Best defensive players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return
        
        # Return best overall players for inputted year.
        elif (user_input =='4'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2008', '2009', '2010']):
                yr = input("Enter a valid year (2008 - 2010) ==> ").strip()
            
            results = annual_ncaa_top10(yr)
            print("="*50)
            print("Best overall players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return

        # Return highest scorers for inputted year.
        elif (user_input == '5'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2008', '2009', '2010']):
                yr = input("Enter a valid year (2008 - 2010) ==> ").strip()
            
            results = annual_ncaa_top10_pts(yr)
            print("="*50)
            print("Highest scoring players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return

        # Return worst overall players for inputted year.
        elif (user_input == '6'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2008', '2009', '2010']):
                yr = input("Enter a valid year (2008 - 2010) ==> ").strip()
            
            results = annual_ncaa_worst10(yr)
            print("="*50)
            print("Worst overall players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return

        else:
            print("Please check your selection: {}".format(user_input))
            printNCAAMenu()
            user_input = input('\n').strip()


def annualNBA():
    printNBAMenu()
    user_input = input('\n').strip().lower()

    while(True):
        # Returns average, maximum, and minimum height of players for inputted year.
        if (user_input == '1'):
            yr = input("Enter a valid year (2000 - 2018) ==> ")
            while (yr not in ['2000', '2001', '2002', '2003', '2004', '2005', '2006','2007', '2008', '2009', '2010'
            '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018']):
                yr = input("Enter a valid year (2000 - 2018) ==> ").strip()

            results = annual_nba_height(yr)
            print("="*50)
            print("Average height: {:.3f}".format(results[0][0][0]))
            print("Maximum height: {:.3f}".format(results[0][0][2]))
            print("Minimum height: {:.3f}".format(results[0][0][1]))
            print("="*50)
            time.sleep(1)
            return  

        # Return best offensive players for inputted year.
        elif (user_input =='2'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2000', '2001', '2002', '2003', '2004', '2005', '2006','2007', '2008', '2009', '2010'
            '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018']):
                yr = input("Enter a valid year (2000 - 2018) ==> ").strip()
                
            results = annual_nba_top10_offense(yr)
            print("="*50)
            print("Best offensive players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return

        elif (user_input == '3'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2000', '2001', '2002', '2003', '2004', '2005', '2006','2007', '2008', '2009', '2010'
            '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018']):
                yr = input("Enter a valid year (2000 - 2018) ==> ").strip()

            results = annual_nba_top10_defense(yr)
            print("="*50)
            print("Best defensive players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return
        # Return best overall players for inputted year.
        elif (user_input =='4'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2000', '2001', '2002', '2003', '2004', '2005', '2006','2007', '2008', '2009', '2010'
            '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018']):
                yr = input("Enter a valid year (2000 - 2018) ==> ").strip()
            
            results = annual_nba_top10(yr)
            print("="*50)
            print("Best overall players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return

        # Return highest scorers for inputted year.
        elif (user_input == '5'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2000', '2001', '2002', '2003', '2004', '2005', '2006','2007', '2008', '2009', '2010'
            '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018']):
                yr = input("Enter a valid year (2000 - 2018) ==> ").strip()

            results = annual_nba_top10_pts(yr)
            print("="*50)
            print("Highest scoring players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return

        # Return worst overall players for inputted year.
        elif (user_input == '6'):
            yr = input("Enter a valid year ==> ").strip()
            while (yr not in ['2000', '2001', '2002', '2003', '2004', '2005', '2006','2007', '2008', '2009', '2010'
            '2011', '2012', '2013', '2014', '2015', '2016','2017', '2018']):
                yr = input("Enter a valid year (2000 - 2018) ==> ").strip()
            
            results = annual_nba_worst10(yr)
            print("="*50)
            print("Worst overall players of {}".format(yr))
            i = 1
            for r in results: 
                print("{}. {}".format(i, r[0]))
                i+= 1
            print("="*50)
            time.sleep(1)
            return
    

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

