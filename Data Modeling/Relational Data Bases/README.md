# Udacity Data Engineering Nanodegree 

## Problem description and disscussion 

Based on the problem posed by the company, which is to know which songs users listen to, it is essential to have a structured and easy to use database in order to be able to carry out analytical processes of the information. 

From this, the purpose of this tool is to provide an efficient solution for queries to be carried out by data analysts and thus be able to make future decisions that positively impact the user experience in the company.  With the database designed in a denormalized star schema, queries can be carried out with high efficiency on each of the users and songs present in the application. 

To run the scripts the following steps must be followed: 

1. Install the following libraries :
* numpy
* pandas
* psycopg2 
* glob 
* os 

2. Run create_tables.py . This script will create the database and its corresponding tables to develop the project. 

python create_tables.py 

3. Run etl.py . With this script the data is loaded to each of the tables according to the columns that were defined in the sql_queries.py file. 

python etl.py 


In addition to these files there is the sql_queries file where the database tables were created. Finally we have the file test.ipynb through which you can check that the records are being inserted correctly in each of the database tables. 

Start schema :
 * Fact table : songplays 
* Dimensional tables : users , songs, artists and time 

Based on this schema it is possible for the company to make aggregations at different levels either at the level of the user, artist, songs in order to obtain valuable information about the behavior of users within the application, where in my opinion, one of the key points is the time that each user takes within the application. Knowing this metric, decisions can be made in the future in order to increase user engagement. 

