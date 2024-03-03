import csv
import psycopg2
import pandas as pd
import numpy as np



# Function to connect to the database
def create_database():

    conn = psycopg2.connect("host=127.0.0.1  dbname=postgres user=postgres password=Abas2320841")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    cur.execute("DROP DATABASE anime")
    cur.execute("CREATE DATABASE anime")

    conn.close()

    try:
        conn = psycopg2.connect("host=127.0.0.1  dbname=anime user=postgres password=Abas2320841")
    except psycopg2.Error as e:
        print("Error: Couldn't connect to the database")
        print(e)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    return conn, cur

# Function to read data from CSV file
def extract(filepath):

    df = pd.read_csv(filepath)
    return df


# Function to migrate data from source to target database
def create_table(conn, cur, table_create):
    
    # Create table in target database
    cur.execute(table_create)

def insert_table(conn, cur, data, insert_into_table):
    # Insert data into target database
    for i, row in data.iterrows():
        cur.execute(insert_into_table, list(row))
    # Commit changes 
    conn.commit()


# Main function
if __name__ == "__main__":
    source_file1 = 'anime.csv'
    source_file2= 'rating.csv'
    
    # creating tables
    conn, cur = create_database()
    
    create_anime_table = ('''CREATE TABLE IF NOT EXISTS anime (
                            id INT PRIMARY KEY,
                            name VARCHAR,
                            genre TEXT,
                            type VARCHAR,
                            episodes INT,
                            rating FLOAT,
                            members INT
                            )''')
    create_table(conn, cur, create_anime_table)

    create_rating_table = ('''CREATE TABLE IF NOT EXISTS rating (
                            user_id INT,
                            anime_id INT,
                            rating INT
                            )''')
    create_table(conn, cur, create_rating_table)

    # reading data from csv file 
    anime_data = extract(source_file1)
    # replacing unfinished animes episode number with 0
    anime_data['episodes'].replace('Unknown', 0,inplace=True )

    rating_data = extract(source_file2)

    
    insert_anime_rows = ("""INSERT INTO anime( 
                         id,
                         name, 
                         genre,
                         type,
                         episodes,
                         rating,
                         members)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)""")
    insert_table(conn, cur, anime_data, insert_anime_rows)  

    insert_rating_rows = ("""INSERT INTO rating(
                        user_id,
                        anime_id,
                        rating)
                        VALUES (%s, %s, %s)""")                   
    insert_table(conn, cur, rating_data, insert_rating_rows) 

    conn.close()
 

    