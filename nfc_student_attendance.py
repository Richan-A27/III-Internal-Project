import serial
import mysql.connector
from mysql.connector import pooling
from datetime import date

# Replace 'COM3' with the correct serial port of your Arduino
ser = serial.Serial('COM4', 9600)

# Initialize MySQL connection pool
dbconfig = {
    "host": "localhost",
    "user": "root",
    "password": "mysqldatabase",
    "database": "students_db",
    "pool_size": 5,
    "pool_name": "attendance_pool"
}
conn_pool = pooling.MySQLConnectionPool(**dbconfig)

# Read NFC tag data from Arduino via serial communication
def read_nfc_tag():
    tag_data = ser.readline().decode().strip()
    return tag_data

# Read NFC tag data, retrieve student info, and mark attendance
def process_nfc_tag():
    try:
        uid = read_nfc_tag()
        if uid:
            conn = conn_pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT student_id, student_name, student_email FROM students WHERE uid = %s"
            cursor.execute(query, (uid,))
            student_data = cursor.fetchone()
            cursor.close()
            if student_data:
                student_id, student_name, student_email = student_data.values()
                print(f"Student: {student_name} (ID: {student_id}, Email: {student_email})")
                cursor = conn.cursor()
                insert_query = "INSERT INTO attendance (student_id, session_date) VALUES (%s, %s)"
                cursor.execute(insert_query, (student_id, date.today()))
                conn.commit()
                cursor.close()
            else:
                print("Student not registered.")
            conn.close()
    except Exception as e:
        print(f"Error processing NFC tag: {e}")

# Main process
while True:
    process_nfc_tag()
