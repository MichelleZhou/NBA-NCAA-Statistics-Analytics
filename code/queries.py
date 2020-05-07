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
    query="SELECT * FROM ncaa_stats,ncaa_players WHERE ncaa_players.id=ncaa_stats.player_id AND ncaa_players.name='%s'" %name
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if(len(records))==0:
        resultofSearching.append("Can not find this player in the datasets")
        return resultofSearching
    else:
        resultofSearching.append(records)
    ret.append(resultofSearching)
    name.replace(',','')
    query="SELECT * From ncaa_players,ncaa_stats,nba_stats WHERE ncaa_players.id=ncaa_stats.player_id AND ncaa_players.name LIKE  nba_stats.player_name AND ncaa_players.name ILIKE '%s'"%name
    cursor.execute(query)
    records = cursor.fetchall()
    resultofEnteringNBA=[]
    if len(records)==0: 
        resultofEnteringNBA.append("This player was not on the nba team any time between 2000 and 2017") 
    else:
        resultofEnteringNBA.append(records)
    ret.append(resultofEnteringNBA)
    return ret
        


#NBA PLAYER LOOKUP
def nba_player_lookup(name):
    ret=[]
    query="SELECT *FROM nba_stats WHERE nba_stats.player_name='%s'" % name
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if(len(records))==0:
        resultofSearching.append("Can not find this player in the datasets")
    else:
        resultofSearching.append(records)
    ret.append(resultofSearching)
    query="SELECT * From nba_players,ncaa_players,ncaa_stats WHERE ncaa_players.id=ncaa_stats.player_id AND ncaa_players.name LIKE  nba_players.name AND nba_players.name ILIKE '%s' " %name
    cursor.execute(query)
    records = cursor.fetchall()
    resultofWasInNCAA=[]
    if len(records)==0: 
        resultofWasInNCAA.append("This player was not on the ncaa team any time between 2000 and 2017" )
    else:
        resultofWasInNCAA.append(records)
    ret.append(resultofWasInNCAA)
    return ret



#ANNUAL NCAA REVIEW
#Average height and height range
def annual_ncaa_height(year):

    query=" SELECT AVG(height),MAX(height),MIN(height) from ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND height != 0 AND ncaa_stats.year=%s GROUP BY ncaa_stats.year" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofHeight=[]
    if len(records)==0:
        resultofHeight.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofHeight.append(records)
    return resultofHeight
#top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
def annual_ncaa_top10_fg_attempt(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY fg_attempts DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching    

def annual_ncaa_top10_tp_attempt(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY tp_attempts DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching  
 
def annual_ncaa_top10_rebound(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY rebounds DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching      

def annual_ncaa_top10_games_played(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY games_played DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 

def annual_ncaa_top10_three_pointers(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY three_pointers DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 

def annual_ncaa_top10_assists(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY assists DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching  

def annual_ncaa_top10_blocks(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY blocks DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 

def annual_ncaa_top10_steals(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY steals DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching  

def annual_ncaa_top10_pts(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY pts DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_ncaa_top10_turnovers(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY turnovers DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching



#Top 10 players with highest % of attribute
def annual_ncaa_top10_fg_percentage(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY fg_percentage DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_ncaa_top10_tp_percentage(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY tp_percentage DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_ncaa_top10_rb_percentage(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY rb_percentage DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_ncaa_top10_ass_percentage(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY ass_percentage DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_ncaa_top10_st_percentage(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY st_percentage DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_ncaa_top10_bl_percentage(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY bl_percentage DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_ncaa_top10_pts_pergame(year):
    query="SELECT name FROM ncaa_stats,ncaa_players WHERE ncaa_stats.player_id=ncaa_players.id AND ncaa_stats.year=%s ORDER BY pts_pergame DESC LIMIT 10"%year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2008-2010]")  
    else:
        resultofSearching.append(records)
    return resultofSearching
#ANNUAL NBA REVIEW
#Average height and height range
def annual_nba_height(year):
    query="SELECT AVG(height),MAX(height),MIN(height)from nba_stats,nba_players WHERE nba_stats.player_name=nba_players.name AND nba_stats.year=%s GROUP BY nba_stats.year" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofHeight=[]
    if len(records)==0:
        resultofHeight.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofHeight.append(records)
    return resultofHeight
#top 10 players with highest # of fg, three pointers, free throws, rebound, assists, etc
def annual_nba_fg_attempts(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY fg_attempts DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_tp_attempts(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY tp_attempts DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_points(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY points DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_games_played(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY games_played DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_three_pointers(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY three_pointers DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 
#Top 10 players with highest % of attribute
def annual_nba_fg_percentage(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY fg_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_tp_percentage(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY tp_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_rb_percentage(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY rb_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_ass_percentage(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY  ass_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def annual_nba_st_percentage(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY st_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 

def annual_nba_bl_percentage(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY bl_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching 

def annual_nba_turnover_percentage(year):
    query="SELECT player_name FROM nba_stats AND nba_stats.year=%s ORDER BY turnover_percentage DESC LIMIT 10" %year
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    if len(records)==0:
        resultofSearching.append("The year asked is not in database usage[2000-2017]")  
    else:
        resultofSearching.append(records)
    return resultofSearching

def top10_college():
    query="SELECT college,COUNT(college) AS frequency FROM nba_players WHERE college ~ ' ' GROUP BY college ORDER BY COUNT(college)  DESC LIMIT 10"
    cursor.execute(query)
    records=cursor.fetchall()
    resultofSearching=[]
    resultofSearching.append(records)
    return resultofSearching
'''
if __name__=="__main__":
    print(nba_player_lookup('Keith Benson'))
    print(ncaa_player_lookup('Keith Benson'))
    print(top10_college())
    print( annual_ncaa_height(2008))
    print( annual_nba_height(2008))
'''