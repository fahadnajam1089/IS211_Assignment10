import sqlite3

person = [(1,'James','Smith',41),
          (2,'Diana','Greene',23),
          (3,'Sara','White',27),
          (4,'William','Gibson',23)]

pet = [(1,'Rusty','Dalmation',4,1),
       (2,'Bella','AlaskanMalamute',3,0),
       (3,'Max','CockerSpaniel',1,0),
       (4,'Rocky','Beagle',7,0),
       (5,'Rufus','CockerSpaniel',1,0),
       (6,'Spot','Bloodhound',2,1)]


person_pet = [(1,1),(1,2),(2,3),(2,4),(3,5),(4,6)]


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def person_insert(conn, task):
    sql = ''' INSERT INTO person(id,first_name,last_name,age)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def pet_insert(conn, task):
    sql = ''' INSERT INTO pet(id,name,breed,age,dead)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def person_pet_insert(conn, task):
    sql = ''' INSERT INTO person_pet(person_id,pet_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


conn = create_connection("Pets.db")

for data in person:
    person_insert(conn,data)

for data in pet:
    pet_insert(conn,data)

for data in person_pet:
    person_pet_insert(conn,data)
