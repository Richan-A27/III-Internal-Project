import serial
import mysql.connector
from datetime import datetime
import tkinter as tk

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqldatabase",
    database="students_db"
)
#create a cursor object
cursor = db.cursor()

# Open the serial port
ser = serial.Serial('COM4', 9600)  # Change 'COM4' to the appropriate port

# Function to mark attendance
def mark_attendance():
    # Read NFC tag data from the serial port
    tag_data = ser.readline().decode().strip()
    
    if tag_data.startswith("URK23CS"):  # Assuming tag data starts with "URK23CS"
        cursor.execute("SELECT * FROM students WHERE student_id = %s", (tag_data,))
        result = cursor.fetchone()

        if result:
            now = datetime.now().strftime("%H:%M:%S")  # Get current time
            cursor.execute("INSERT INTO attendance (student_id, date, time) VALUES (%s, NOW(), %s)", (tag_data, now))
            db.commit()
            status_label.config(text=f"Attendance marked for student {tag_data} at {now}")
        else:
            status_label.config(text=f"Student with ID {tag_data} not found in the database")

# Function to empty the attendance database
def clear_attendance():
    cursor.execute("TRUNCATE TABLE attendance;")
    status_label.config(text="Attendance cleared!")

# main window
window = tk.Tk()
window.title("Student Attendance System")
window.geometry("400x200")

# status label
status_label = tk.Label(window, text="Waiting for NFC tag data...", padx=10, pady=10)
status_label.pack()

# button to mark attendance
attendance_button = tk.Button(window, text="Mark Attendance", command=mark_attendance)
attendance_button.pack(pady=10)

# button to clear the attendance table
clear_attendance_button = tk.Button(window, text="Clear Attendance Data", command=clear_attendance)
clear_attendance_button.pack(pady=20)


# Close the serial port when the window is closed
def on_closing():
    ser.close()
    db.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the Tkinter event loop
window.mainloop()
