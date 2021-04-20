import sqlite3

conn = sqlite3.connect('Pets.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - Person
c.execute('''CREATE TABLE person(
            [id] INTEGER PRIMARYKEY,
            [first_name] TEXT,
            [last_name] TEXT,
            [age] INTEGER
            );''')
          
# Create table - PET
c.execute('''CREATE TABLE pet(
            [id] INTEGERPRIMARYKEY,
            [name] TEXT,
            [breed] TEXT,
            [age] INTEGER,
            [dead] INTEGER
            );''')
        
# Create table - DAILY_STATUS
c.execute('''CREATE TABLE person_pet(
            [person_id] INTEGER,
            [pet_id] INTEGER
          );''')
                 
conn.commit()
