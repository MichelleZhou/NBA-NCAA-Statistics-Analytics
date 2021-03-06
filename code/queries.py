"""
queries.py contain functionalities
"""
import psycopg2
import psycopg2.extras

conn_str = "host='localhost' dbname='dbms_final_project' user='dbms_project_user'\
             password='dbms_password'"
conn = psycopg2.connect(conn_str,cursor_factory=psycopg2.extras.DictCursor)
cursor = conn.cursor()

#NCAA PLAYER LOOKUP
def ncaa_player_lookup(name):
    ret=[]
    query="SELECT ncaa_players.name,ncaa_players.year, ncaa_players.school, ncaa_players.position, ncaa_stats.games_played, ncaa_stats.field_goals, ncaa_stats.fg_attempts, ncaa_stats.three_pointers, ncaa_stats.tp_attempts, ncaa_stats.rebounds, ncaa_stats.assists, ncaa_stats.blocks, ncaa_stats.steals, ncaa_stats.pts "\
          "FROM ncaa_stats,ncaa_players "\
          "WHERE ncaa_players.id=ncaa_stats.player_id AND ncaa_players.name ILIKE'%s'" % name
    cursor.execute(query)
    records=cursor.fetchall()
    if (len(records)==0): return ret
    else: ret.append(records)

    query="SELECT nba_stats.team, nba_stats.year, nba_players.position, nba_stats.games_played, nba_stats.field_goals,nba_stats.fg_attempts, nba_stats.three_pointers, nba_stats.tp_attempts, nba_stats.rb_percentage, nba_stats.ass_percentage, nba_stats.st_percentage, nba_stats.bl_percentage, nba_stats.points "\
          "From ncaa_players,ncaa_stats,nba_stats, nba_players "\
          "WHERE ncaa_players.id=ncaa_stats.player_id AND "\
          "nba_players.name = nba_stats.player_name AND "\
          "ncaa_players.name LIKE  nba_stats.player_name "\
          "AND ncaa_players.name ILIKE '%s'" % name
    cursor.execute(query)
    records = cursor.fetchall()
    if (len(records)!=0): ret.append(records)
    return ret
        


#NBA PLAYER LOOKUP
def nba_player_lookup(name):
    ret=[]
    query="SELECT nba_stats.team, nba_stats.year, nba_players.position, nba_stats.games_played, nba_stats.field_goals,nba_stats.fg_attempts, nba_stats.three_pointers, nba_stats.tp_attempts, nba_stats.rb_percentage, nba_stats.ass_percentage, nba_stats.st_percentage, nba_stats.bl_percentage, nba_stats.points "\
          "FROM nba_stats, nba_players "\
          "WHERE nba_stats.player_name = nba_players.name AND "\
          "nba_stats.player_name ILIKE '%s'" % name
    cursor.execute(query)
    records=cursor.fetchall()
    if(len(records))==0: return ret
    else: ret.append(records)
    
    query="SELECT ncaa_players.name,ncaa_players.year, ncaa_players.school, ncaa_players.position, ncaa_stats.games_played, ncaa_stats.field_goals, ncaa_stats.fg_attempts, ncaa_stats.three_pointers, ncaa_stats.tp_attempts, ncaa_stats.rebounds, ncaa_stats.assists, ncaa_stats.blocks, ncaa_stats.steals, ncaa_stats.pts "\
          "From nba_players,ncaa_players,ncaa_stats "\
          "WHERE ncaa_players.id=ncaa_stats.player_id AND "\
          "ncaa_players.name = nba_players.name AND "\
          "nba_players.name ILIKE '%s' " %name
    cursor.execute(query)
    records = cursor.fetchall()
    if len(records) !=0: ret.append(records)
    return ret



#ANNUAL NCAA REVIEW

def annual_ncaa_height(year):
    query=" SELECT AVG(height),MAX(height),MIN(height) from ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND height != 0 AND ncaa_stats.year=%s GROUP BY ncaa_stats.year" %year
    cursor.execute(query)
    records=cursor.fetchall()
    return records


def annual_ncaa_top10_offense(year):
    query = "SELECT name, CAST(field_goals+three_pointers+turnovers AS FLOAT)/games_played AS rating "\
            "FROM ncaa_stats, ncaa_players "\
            "WHERE ncaa_stats.player_id=ncaa_players.id AND "\
            "games_played != 0 AND "\
            "ncaa_stats.year = %s ORDER BY rating DESC LIMIT 10" % year
    cursor.execute(query)
    records=cursor.fetchall()
    return records

def annual_ncaa_top10_defense(year):
    query = "SELECT name, CAST(rebounds+assists+blocks+steals AS FLOAT)/games_played AS rating "\
            "FROM ncaa_stats, ncaa_players "\
            "WHERE ncaa_stats.player_id=ncaa_players.id AND "\
            "games_played != 0 AND "\
            "ncaa_stats.year = %s ORDER BY rating DESC LIMIT 10" % year
    cursor.execute(query)
    records=cursor.fetchall()
    return records


def annual_ncaa_top10(year):
    query = "SELECT name, ( CAST(rebounds+assists+blocks+steals AS FLOAT)/games_played + CAST(field_goals+three_pointers+turnovers AS FLOAT)/games_played ) AS rating "\
            "FROM ncaa_stats, ncaa_players "\
            "WHERE ncaa_stats.player_id=ncaa_players.id AND "\
            "games_played != 0 AND "\
            "ncaa_stats.year = %s ORDER BY rating DESC LIMIT 10" % year
    cursor.execute(query)
    records=cursor.fetchall()
    return records


def annual_ncaa_worst10(year):
    query = "SELECT name, ( CAST(rebounds+assists+blocks+steals AS FLOAT)/games_played + CAST(field_goals+three_pointers+turnovers AS FLOAT)/games_played ) AS rating "\
            "FROM ncaa_stats, ncaa_players "\
            "WHERE ncaa_stats.player_id=ncaa_players.id AND "\
            "games_played != 0 AND "\
            "ncaa_stats.year = %s ORDER BY rating LIMIT 10" % year
    cursor.execute(query)
    records=cursor.fetchall()
    return records


def annual_ncaa_top10_pts(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY pts DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    return records


#ANNUAL NBA REVIEW

def annual_nba_top10_offense(year):
    query = "SELECT player_name, CAST(field_goals+three_pointers AS FLOAT)/games_played AS rating FROM nba_stats WHERE year = %s ORDER BY rating DESC LIMIT 10" % year
    cursor.execute(query)
    records=cursor.fetchall()
    return records

def annual_nba_top10_defense(year):
    query = "select player_name, CAST(rb_percentage/100 + ass_percentage/100 + bl_percentage + st_percentage AS FLOAT)/games_played AS rating FROM nba_stats WHERE year = %s ORDER BY rating DESC LIMIT 10" % year
    cursor.execute(query)
    records=cursor.fetchall()
    return records    

def annual_nba_top10(year):
    query = "select player_name, CAST(rb_percentage/100 + ass_percentage/100 + bl_percentage + st_percentage + field_goals + three_pointers AS FLOAT)/games_played AS rating FROM nba_stats WHERE year = %s ORDER BY rating DESC LIMIT 10" % year
    cursor.execute(query)
    records=cursor.fetchall()
    return records

def annual_nba_worst10(year):
    query = "select player_name, CAST(rb_percentage/100 + ass_percentage/100 + bl_percentage + st_percentage + field_goals + three_pointers AS FLOAT)/games_played AS rating FROM nba_stats WHERE year = %s ORDER BY rating LIMIT 10" % year
    cursor.execute(query)
    records=cursor.fetchall()
    return records

def annual_nba_top10_pts(year):
    query="SELECT player_name from nba_stats WHERE year = %s ORDER BY points LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    return records


#Average height and height range
def annual_nba_height(year):
    query="SELECT AVG(height),MAX(height),MIN(height)from nba_stats,nba_players WHERE nba_stats.player_name=nba_players.name AND nba_stats.year=%s GROUP BY nba_stats.year" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofHeight=[]
    if len(records)==0:
        resultofHeight.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofHeight.append(records)
    return resultofHeight

#top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
def annual_nba_fg_attempts(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY fg_attempts DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_tp_attempts(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY tp_attempts DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_points(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY points DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_games_played(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY games_played DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_three_pointers(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY three_pointers DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 

#Top 10 players with highest % of attribute
def annual_nba_fg_percentage(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY fg_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_tp_percentage(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY tp_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_rb_percentage(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY rb_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_ass_percentage(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY  ass_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_st_percentage(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY st_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 

def annual_nba_bl_percentage(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY bl_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 

def annual_nba_turnover_percentage(year):
    query="SELECT player_name FROM nba_stats WHERE nba_stats.year=%s ORDER BY turnover_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2018]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

## INTERESTING STATS

def top10_college(amt):
    query="SELECT college,COUNT(college) AS frequency FROM nba_players WHERE college ~ ' ' GROUP BY college ORDER BY COUNT(college)  DESC LIMIT %s" %amt
    cursor.execute(query)
    records=cursor.fetchall()
    return records
