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
    cursor.execute("SELECT * FROM projects")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()   

   

if __name__ == "__main__":
    # Connect to the database
    db = connect("projects")
    cursor = db.cursor()
    select_all_projects()
    db.close()




