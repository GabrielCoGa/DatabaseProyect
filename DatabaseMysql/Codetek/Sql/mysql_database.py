#https://youtu.be/eGwuHtRaFrM?si=My8W_O-x9ekQSePA

import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(
            host='localhost',
            user='root',
            password='',
            database=db_name)
    except mysql.Error as e:
        print(f"Error connecting to MySQL: {e}")

def select_all_projects():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM projects")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()  

def add_new_project_dupla():
    cursor = db.cursor()
    project_data = ("Clean house", "Clean by room")
    cursor.execute("INSERT INTO projects(title, description) VALUES (%s, %s)", project_data)

    project_id = cursor.lastrowid

    tasks_data = [
        (project_id, "Clean kitchen"),
        (project_id, "Clean living room")
    ]
    cursor.executemany('''INSERT INTO tasks (project_id, description)
                        VALUES (%s, %s)''', tasks_data)
    db.commit()

def add_new_project():
    name = input("Enter project name: ")
    description = input("Enter project description: ")
    add_new_project_param(name, description) 

def add_new_project_param(name, description):
    cursor = db.cursor()
    sql = "INSERT INTO projects (name, description) VALUES (%s, %s)"
    val = (name, description)
    cursor.execute(sql, val)
    db.commit()
    print(f"Project '{name}' added successfully.")   

if __name__ == "__main__":
    # Connect to the database
    db = connect("projects")
    #cursor = db.cursor() una vez usado el cursor se cierra, por eso se vuelve a crear cada vez que se necesita
    #select_all_projects()
    add_new_project_dupla()
    db.close()




