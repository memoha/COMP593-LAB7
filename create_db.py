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
from datetime import datetime
from pprint import pprint
from faker import Faker
import random
fake = Faker("en_CA")
con = sqlite3.connect('social_network.db')
cur = con.cursur()
cur.execute('SELECT * FROM people')
all_people = cur.fetchall()
print(all_people)
con.commit()
con.close()

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""

create_ppl_tbl_query = """"
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
 );
"""
cur.execute(create_ppl_tbl_query)
con.commit()
con.close()
    # TODO: Create function body
add_person_query = """" 
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
 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""    
new_person = ('Megha Mohan',
 'megha.mohan@whatever.net',
 '123 Fake St.',
 'Fakesville',
 'Fake Prince Island',
 'Enjoys to imitate how other people are talking.',
 19,
 datetime.now(),
 datetime.now())

cur.execute(add_person_query, new_person)
con.commit()
con.close()


def populate_people_table():
    """Populates the people table with 200 fake people"""
    
    for _ in range(200):
        people = fake.administrative_unit()
        identification = fake.random_init(min=900000, max=100000000)
        print(f'The population of {people} is {identification}.')

        age = random.int(1,100)
        sqlite3.Cursor.execute("INSERT INTO people (people, identification, age)")

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