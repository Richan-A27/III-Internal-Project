import mysql.connector

# MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysqldatabase',
    database='students_db'
)
cursor = conn.cursor()

student_data = [
    ("URK23CS0001", "Bruce Wanye", "brucewayne@karunya.edu.in" ),
    ("URK23CS0002", "Hermione", "hermione@karunya.edu.in" ),
    ("URK23CS0004", "Louis", "louis@karunya.edu.in" ),
    ("URK23CS0004", "Alex Harry", "alexharry@karunya.edu.in" ),
    ("URK23CS0005", "Chadler", "chadler@karunya.edu.in")
]

#insert student data into the students table
for student in student_data:
    cursor.execute("""
        INSERT INTO students (student_id,name, email)
        VALUES (%s, %s, %s)
    """, student)

#commit changes
conn.commit()
cursor.close()
conn.close()
