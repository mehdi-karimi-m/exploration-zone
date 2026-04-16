import sqlite3
from datetime import datetime
from pprint import pprint

people = []
does_add_new_people = bool(input("Enter a to add new person or only press enter to show data: "))

while does_add_new_people:
    id = int(input("Id: "))
    first_name = input("Firstname: ")
    last_name = input("Lastname: ")
    age = int(input("Age: "))
    people.append(
        {
            "Id": id,
            "FirstName": first_name,
            "LastName": last_name,
            "Age": age,
            "InsertDate": str(datetime.now())
        }
    )
    if not bool(input("Enter c to continoue:")):
        break
    print("-" * 20)

with sqlite3.connect("db.sqllite3") as conn:
    # create_table_command = """CREATE TABLE 'People' (
    #     'Id' INTEGER,
    #     'FirstName' TEXT,
    #     'LastName' TEXT,
    #     'Age' INTEGER,
    #     'InsertDate' TEXT,
    #     PRIMARY KEY('Id')
    # )"""
    # conn.execute(create_table_command)
    insert_command = "INSERT INTO People VALUES (?, ?, ?, ?, ?)"
    for person in people:
        conn.execute(insert_command, tuple(person.values()))
    conn.commit()


print("*" * 30)

with sqlite3.connect("db.sqllite3") as sqllite_connection:
    select_command = "SELECT * FROM People"
    cursor = sqllite_connection.execute(select_command)
    all_data = cursor.fetchall()
    pprint(all_data)
