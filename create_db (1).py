"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
import sqlite3 
import pandas 
from datetime import datetime
from pprint import pprint
from faker import Faker
fake = Faker("en_CA")
con = sqlite3.connect('social_network.db')
cur = con.cursor()


def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    populate_people_table()
    con.close()

def create_people_table():
    """Creates the people table in the database"""

    create_ppl_tbl_query = """
        CREATE TABLE IF NOT EXISTS people
        (
            id   INTEGER PRIMARY KEY,
            name        TEXT NOT NULL,
            email       TEXT NOT NULL,
            address     TEXT NOT NULL,
            city        TEXT NOT NULL,
            province    TEXT NOT NULL,
            bio         TEXT,
            age         INTEGER,
            created_at  DATETIME NOT NULL,
            updated_at  DATETIME NOT NULL
        );"""
 

    cur.execute(create_ppl_tbl_query)
    con.commit()

    # TODO: Create function body
    add_person_query = """
        INSERT INTO people
        (
            name,
            email,
            address,
            city,
            province,
            bio,
            age,
            created_at,
            updated_at
        )
        VALUES 
        (
            'Megha Mohan',
            'megha.mohan@whatever.net',
            '123 Fake St.','Fakesville',
            'Fake Prince Island',
            'Enjoys to imitate how other people are talking.',
            19,
            datetime.now(),
            datetime.now()
        );"""



    cur.execute (add_person_query)


    con.commit()


    cur.execute('SELECT * FROM people')
    all_people = cur.fetchall()
    pprint(all_people)

    con.commit()




def populate_people_table():
    """Populates the people table with 200 fake people"""
    
    for i in range(200):
        name = fake.name()
        email = fake.email()
        address = fake.address()
        city = fake.city()
        province = fake.province()
        bio = fake.sentences()
        age = fake.random_int(1, 100)
        created_at = datetime.now()
        updated_at = datetime.now()

        cur.execute("INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)VALUES (?,?,?,?,?,?,?,?,?)", (name, email, address, city, province, bio, age, created_at, updated_at))

        con.commit()

    cur.execute("SELECT * FROM people")
    all_people = cur.fetchall()
    dataframe = pandas.DataFrame(all_people, columns=['id', 'name', 'email', 'address', 'city', 'province', 'bio', 'age', 'created_at', 'updated_at'])
    dataframe.to_csv('people.csv')    


    # TODO: Create function body
    return

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()