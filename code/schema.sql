-- Project Schema

DROP SCHEMA IF EXISTS basketball;
CREATE SCHEMA basketball;

DROP TABLE IF EXISTS ncaa_players CASCADE;
DROP TABLE IF EXISTS ncaa_stats CASCADE;
DROP TABLE IF EXISTS nba_players CASCADE;
DROP TABLE IF EXISTS nba_stats CASCADE;

CREATE TABLE ncaa_players(
	id	           				INTEGER UNIQUE,
	year        	    	    INTEGER,
	name 		    	    	VARCHAR(255),
	school         				VARCHAR(255),
	class_year          		VARCHAR(3),
	height              		INTEGER,
	position            		VARCHAR(10),

	PRIMARY KEY(id, year)
);

CREATE TABLE ncaa_stats(
	player_id                   INTEGER REFERENCES ncaa_players(id),
	school		               	VARCHAR(255),
	year                        INTEGER,
	games_played				INTEGER,

	field_goals                 INTEGER,
	fg_attempts        			INTEGER,
	fg_percentage      			FLOAT,
	three_pointers              INTEGER,
	tp_attempts       			INTEGER,
	tp_percentage     			FLOAT,
	rebounds                    INTEGER,
	rb_pergame           		FLOAT,
	assists                     INTEGER,
	ass_pergame            		FLOAT,
	blocks                      INTEGER,
	bl_pergame             		FLOAT,
	steals                      INTEGER,
	st_pergame             		FLOAT,
	pts                      	INTEGER,
	pts_pergame             	FLOAT,
	turnovers                   INTEGER,

	PRIMARY KEY(player_id, year)
);

CREATE TABLE nba_players(
	name     					VARCHAR(255) UNIQUE,
	birthdate       			DATE,
	height          			INTEGER,
	position        			VARCHAR(40),
	college         			VARCHAR(255),

	PRIMARY KEY(name, birthdate)
);

CREATE TABLE nba_stats(
	player_name                	VARCHAR(255),
	year                        INTEGER,
	team                        VARCHAR(40),
	games_played                INTEGER,

	field_goals                 INTEGER,
	fg_attempts            		INTEGER,
	fg_percentage          		FLOAT,
	three_pointers             	INTEGER,
	tp_attempts           		INTEGER,
	tp_percentage         		FLOAT,
	rb_percentage        		FLOAT,
	ass_percentage            	FLOAT,
	st_percentage            	FLOAT,
	bl_percentage           	FLOAT,
	points                      INTEGER,
	turnover_percentage         FLOAT,

	PRIMARY KEY(player_name, team)
);