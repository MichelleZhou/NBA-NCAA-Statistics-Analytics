import psycopg2
import psycopg2.extras
import csv
import time

conn_str = "host='localhost' dbname='dbms_final_project' user='dbms_project_user'\
             password='dbms_password'"
conn = psycopg2.connect(conn_str,cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()


# Preprocessing of csv file to replace all dashes - with zeroes for easier inserts
def replaceDashesWithZeroes(infile, outfile, ncaa):
    with open(infile, 'r') as inf, open(outfile, 'w',newline='\n', encoding='utf-8') as outf:
        reader = csv.reader(inf, delimiter=',')
        writer = csv.writer(outf)

        for row in reader:
            row = [x.replace('-', '0') if x == '-' else x for x in row]
            # Convert height into inches for NCAA players.
            if (ncaa == 'y' and row[8] != '-'):
                r = row[8].split('-')
                if (len(r) > 1): row[8] = str(int(r[0])*12+ int(r[1]))
                else: row[8] = '0'

            # Convert height into inches for NBA players.
            elif (ncaa == 'n' and row[4] != '-'):
                r = row[4].split('-')
                if (len(r) > 1): row[4] = str(int(r[0])*12+int(r[1]))
                else: row[4] = '0'

            writer.writerow(row)

    inf.close()
    outf.close()



# Helper function to process NCAA data insertion. 
def processNCAA(infile, player_query, stats_query, y):
    fixedcsv = infile[:-4] + '_fixed.csv'
    replaceDashesWithZeroes(infile, fixedcsv, 'y')

    # Open fixed csv file to insert accordingly.
    with open(fixedcsv) as inf:
        reader = csv.reader(inf, delimiter=',')
        for row in reader:
            # Insert statement for ncaa_players table.

            # Format NCAA player names to match with NBA format (first last)
            r = row[3].split(', ')
            r.reverse()
            row[3] = ' '.join(r)
            cursor.execute(
                player_query,
                dict( id=row[4], yr=y, name=row[3], school=row[0], class_yr=row[5], height=row[8],
                      position=row[7] 
                )
            )

            # Insert statement for ncaa_stats table.
            cursor.execute(
                stats_query,
                dict( id=row[4], school=row[0], yr=y, games=row[9], fg=row[10], fg_a=row[11],
                      fg_p=row[12], tp=row[13], tp_a=row[14], tp_p=row[15], rb=row[19],
                      rb_pg=row[20],ass=row[21], ass_pg=row[22], bl=row[23], bl_pg=row[24],
                      st=row[25], st_pg=row[26], pts=row[27], pts_pg=row[28], turnovers=row[29]
                )
            )
        conn.commit()

    # Show data loading progress.
    inf.close()
    print("    Added data for {}...".format(y))


# Helper function to process NBA data insertion.
def processNBA(infile, query, option):
    fixedcsv = infile[:-4] + '_fixed.csv'
    replaceDashesWithZeroes(infile, fixedcsv, 'n')

    # Open fixed csv file to insert accordingly.
    with open(fixedcsv) as inf:
        reader = csv.reader(inf, delimiter=',')
        first = next(reader)    # Skip header row.
        for row in reader:
            # Insert into nba_players table only.
            if (option == 1):
                if (row[6] == ""):
                    row[6] = 'January 1, 0001'
                cursor.execute(
                    query,
                    dict( name=row[0], bd=row[6], height=row[4], pos=row[3], college=row[7] )
                )
            # Insert into nba_stats table only.
            else:
                if (row[1] >= '2000'):
                    # Some rows have asterisks after player names, removing them for clarity.
                    if '*' in row[2]: row[2] = row[2][:-1]
                    cursor.execute(
                        query,
                        # Replace empty cells (bc of zero division)
                        dict( name=row[2], yr=row[1], team=row[5], games=row[6], 
                              fg=row[31], fg_a=row[32], fg_p=row[33].replace("",'0'),
                              tp=row[34], tp_a=row[35], tp_p=row[36].replace("",'0'),
                              rb_p=row[15].replace("",'0'), ass_p=row[16].replace("",'0'),
                              st_p=row[17].replace("",'0'), bl_p=row[18].replace("",'0'),
                              pts=row[52], turn_p=row[19].replace("",'0')
                        )
                    )

        conn.commit()
    inf.close()


###################################################################################################
#
#    Main process to load data into the database. NCAA statistics from 2008-2010 are 
#    loaded. NBA statistics from 2000 to 2017 are subsequently inserted. 
def main():
    # Creating schema
    print("="*50)
    print("Creating schema...")
    cursor.execute(open("code/schema.sql", "r").read())
    print("Schema created!")
    print("="*50)


    print("Loading data...")

    ## NCAA data loading
    print("Inserting NCAA data...")
    ncaa_player_query = (
        "INSERT INTO ncaa_players(id, year, name, school, class_year, height, position)"
        "VALUES (%(id)s, %(yr)s, %(name)s, %(school)s, %(class_yr)s, %(height)s, %(position)s)"
        "ON CONFLICT DO NOTHING")
    
    ncaa_stats_query = (
        "INSERT INTO ncaa_stats(player_id, school, year, games_played, field_goals, fg_attempts,"
        "fg_percentage, three_pointers, tp_attempts,tp_percentage, rebounds, rb_pergame, assists,"
        "ass_pergame, blocks, bl_pergame, steals, st_pergame, pts, pts_pergame, turnovers)"
        
        "VALUES (%(id)s, %(school)s, %(yr)s, %(games)s, %(fg)s, %(fg_a)s, %(fg_p)s, %(tp)s," 
        "%(tp_a)s, %(tp_p)s, %(rb)s, %(rb_pg)s, %(ass)s, %(ass_pg)s, %(bl)s, %(bl_pg)s, %(st)s,"
        " %(st_pg)s, %(pts)s, %(pts_pg)s, %(turnovers)s)"
        "ON CONFLICT DO NOTHING")

    processNCAA('code/datasets/ncaa_players_2008.csv', ncaa_player_query, ncaa_stats_query, 2008)
    processNCAA('code/datasets/ncaa_players_2009.csv', ncaa_player_query, ncaa_stats_query, 2009)
    processNCAA('code/datasets/ncaa_players_2010.csv', ncaa_player_query, ncaa_stats_query, 2010)
    time.sleep(1)
    print("Insertion of NCAA data complete!")


    ## NBA data loading
    print("Inserting NBA data...")
    nba_player_query = (
        "INSERT INTO nba_players(name, birthdate, height, position, college)"
        "VALUES (%(name)s, %(bd)s, %(height)s, %(pos)s, %(college)s)"
        "ON CONFLICT DO NOTHING" )

    nba_stats_query = (
        "INSERT INTO nba_stats(player_name, year, team, games_played, field_goals, fg_attempts,"
        "fg_percentage, three_pointers, tp_attempts, tp_percentage, rb_percentage, ass_percentage,"
        "st_percentage, bl_percentage, points, turnover_percentage)"
        "VALUES (%(name)s, %(yr)s, %(team)s, %(games)s, %(fg)s, %(fg_a)s, %(fg_p)s, %(tp)s,"
        "%(tp_a)s, %(tp_p)s, %(rb_p)s, %(ass_p)s, %(st_p)s, %(bl_p)s, %(pts)s, %(turn_p)s)"
        "ON CONFLICT DO NOTHING" )

    processNBA('code/datasets/player_data.csv', nba_player_query, 1)
    print("    Added NBA player data...")
    processNBA('code/datasets/Seasons_Stats.csv', nba_stats_query, 2)
    print("    Added NBA season statistics...")
    time.sleep(1)
    print("Insertion of NBA data complete!")

  

if __name__ == "__main__":
    main()
    time.sleep(2)
    print("Finished loading data!")
    print("="*50)
