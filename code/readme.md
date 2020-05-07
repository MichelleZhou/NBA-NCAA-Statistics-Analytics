# Application overview

We decided to look into college and professional basketball data to get a better understanding of players' performance during college and whether past performance best predicts future performance. However, due to the limitations of our datasets (the source we found had 1 csv per year but we were only allowed to provide a total of 5 datasets), a lot of our queries were one-sided; i.e. players were either in the NBA or NCAA. However, of the 399 players who **did** get drafted into the NBA after their NCAA careers, we were able to see similar statistics as they moved from NCAA to NBA.  

### Members
- Yaoyu Cheng
- Ruilin Jin
- Winnie Lu
- Yiran Zheng
- Michelle Zhou
 

## Available functionality
- [x] NCAA Player lookup
	> Determines whether the specified player was on an NCAA team between the years of 2008 and 2010. If the specified player was on an NCAA team, a search is conducted through the database to see whether they were on an NBA team from 2000 until 2018. Player statistics are outputted for any reults found.
- [x] NBA Player lookup
    > Determines whether the specified player was on an NBA team any time between 2000 and 2018. Relevant statistics pertaining to the player's carrer shooting averages, rebound averages, and other relevant data are calculated and outputted. Again, if the player was also on an NCAA team between 2008 and 2010, those statistics are calculated for their college basketball career as well. 
- [x] Annual NCAA statistics review
    > Several functionalities are included in this menu to give a broader glimpse into some NCAA stats:
	- Average height of players for each year.
	- Best offensive and defensive players for a given year.
	- Best and worst overall players for a given year.
	- Highest scoring players for a given year.

- [x] Annual NBA statistics review
    > Several functionalities are included in this menu to give a broader glimpse into some NCAA stats:
	- Average height of players for each year.
	- Best offensive and defensive players for a given year.
	- Best and worst overall players for a given year.
	- Highest scoring players for a given year.


## Setting up the application

Because one of our datasets was found on Kaggle and wasn't compatible with the format of `retrieve_data.py`, we have hosted some of our datasets in this GitHub repository and linked them in the `datasets.txt` file. The files can be found in the `KaggleDatasets` folder.

Once the datasets have all been downloaded, simply run the following files in the following order:
1. `db_setup.sql`
2. `load_data.py`
3. `application.py`
