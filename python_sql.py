import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysqldatabase',
    database='students_db'
)
cursor = conn.cursor()

# Sample student data
student_data = [
    ("URK23CS1086", "Richan Abraham J.R", "richanabraham", "72 3D A3 51"),
    ("URK23CS0000", "Jane Smith", "jane.smith@example.com", "A8 B3 1F 12")
]

# Insert student data into the students table
for student in student_data:
    cursor.execute("""
        INSERT INTO students (student_id, student_name, student_email, uid)
        VALUES (%s, %s, %s, %s)
    """, student)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()
