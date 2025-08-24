import sqlite3

conn = sqlite3.connect('DORM_FRESH')

cur = conn.cursor()
# cur.execute("""-- Table1: Students
# CREATE TABLE Students (
#     student_id SERIAL PRIMARY KEY,   -- unique id
#     student_name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL,
#     room_no INT NOT NULL
# );""")

# cur.execute("""-- Table2: Staff
# CREATE TABLE Staff (
#     staff_id SERIAL PRIMARY KEY,
#     staff_name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL
# );""")

# cur.execute("""-- Table3: Rooms
# CREATE TABLE Rooms (
#     room_no INT PRIMARY KEY,
#     no_of_students INT DEFAULT 0,
#     student_list JSON
# );""")
            
# cur.execute("""INSERT INTO Rooms (room_no, no_of_students, student_list)
# VALUES (
#     101,
#     2,
#     '[{"name":"Alice","email":"alice@example.com"},
#       {"name":"Bob","email":"bob@example.com"}]'
# );""")

# cur.execute("""SELECT room_no, student_name, email
# FROM Students """)

# cur.execute("INSERT INTO Students VALUES ('25BEC0129', 'SAATHWIK DASARI', 'saathwik.dasari@vitstudent.ac.in', 420)")
# cur.execute("INSERT INTO Students VALUES ('25BCE0493', 'SHREERAM TA', 'shreeramta@gmail.vitstudent.ac.in', 420)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0131', 'SHREYASH', 'shreyash@vitstudent.ac.in', 420)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0001', 'Student1', 'student1@vitstudent.ac.in', 101)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0002', 'Student2', 'student2@vitstudent.ac.in', 101)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0003', 'Student3', 'student3@vitstudent.ac.in', 101)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0004', 'Student4', 'student4@vitstudent.ac.in', 102)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0005', 'Student5', 'student5@vitstudent.ac.in', 102)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0006', 'Student6', 'student6@vitstudent.ac.in', 102)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0007', 'Student7', 'student7@vitstudent.ac.in', 103)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0008', 'Student8', 'student8@vitstudent.ac.in', 103)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0009', 'Student9', 'student9@vitstudent.ac.in', 103)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0010', 'Student10', 'student10@vitstudent.ac.in', 104)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0011', 'Student11', 'student11@vitstudent.ac.in', 104)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0012', 'Student12', 'student12@vitstudent.ac.in', 104)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0013', 'Student13', 'student13@vitstudent.ac.in', 105)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0014', 'Student14', 'student14@vitstudent.ac.in', 105)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0015', 'Student15', 'student15@vitstudent.ac.in', 105)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0016', 'Student16', 'student16@vitstudent.ac.in', 106)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0017', 'Student17', 'student17@vitstudent.ac.in', 106)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0018', 'Student18', 'student18@vitstudent.ac.in', 106)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0019', 'Student19', 'student19@vitstudent.ac.in', 107)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0020', 'Student20', 'student20@vitstudent.ac.in', 107)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0021', 'Student21', 'student21@vitstudent.ac.in', 107)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0022', 'Student22', 'student22@vitstudent.ac.in', 108)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0023', 'Student23', 'student23@vitstudent.ac.in', 108)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0024', 'Student24', 'student24@vitstudent.ac.in', 108)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0025', 'Student25', 'student25@vitstudent.ac.in', 109)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0026', 'Student26', 'student26@vitstudent.ac.in', 109)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0027', 'Student27', 'student27@vitstudent.ac.in', 109)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0028', 'Student28', 'student28@vitstudent.ac.in', 110)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0029', 'Student29', 'student29@vitstudent.ac.in', 110)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0030', 'Student30', 'student30@vitstudent.ac.in', 110)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0031', 'Student31', 'student31@vitstudent.ac.in', 111)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0032', 'Student32', 'student32@vitstudent.ac.in', 111)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0033', 'Student33', 'student33@vitstudent.ac.in', 111)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0034', 'Student34', 'student34@vitstudent.ac.in', 112)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0035', 'Student35', 'student35@vitstudent.ac.in', 112)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0036', 'Student36', 'student36@vitstudent.ac.in', 112)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0037', 'Student37', 'student37@vitstudent.ac.in', 113)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0038', 'Student38', 'student38@vitstudent.ac.in', 113)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0039', 'Student39', 'student39@vitstudent.ac.in', 113)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0040', 'Student40', 'student40@vitstudent.ac.in', 114)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0041', 'Student41', 'student41@vitstudent.ac.in', 114)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0042', 'Student42', 'student42@vitstudent.ac.in', 114)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0043', 'Student43', 'student43@vitstudent.ac.in', 115)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0044', 'Student44', 'student44@vitstudent.ac.in', 115)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0045', 'Student45', 'student45@vitstudent.ac.in', 115)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0046', 'Student46', 'student46@vitstudent.ac.in', 116)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0047', 'Student47', 'student47@vitstudent.ac.in', 116)")
# cur.execute("INSERT INTO Students VALUES ('25BEC0048', 'Student48', 'student48@vitstudent.ac.in', 116)")

# conn.commit()

# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (1, 'Staff1', 'staff1@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (2, 'Staff2', 'staff2@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (3, 'Staff3', 'staff3@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (4, 'Staff4', 'staff4@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (5, 'Staff5', 'staff5@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (6, 'Staff6', 'staff6@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (7, 'Staff7', 'staff7@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (8, 'Staff8', 'staff8@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (9, 'Staff9', 'staff9@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (10, 'Staff10', 'staff10@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (11, 'Staff11', 'staff11@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (12, 'Staff12', 'staff12@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (13, 'Staff13', 'staff13@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (14, 'Staff14', 'staff14@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (15, 'Staff15', 'staff15@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (16, 'Staff16', 'staff16@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (17, 'Staff17', 'staff17@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (18, 'Staff18', 'staff18@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (19, 'Staff19', 'staff19@vitstudent.ac.in')")
# cur.execute("INSERT INTO Staff (staff_id, staff_name, email) VALUES (20, 'Staff20', 'staff20@vitstudent.ac.in')")

# conn.commit()

# cur.execute("DELETE FROM Rooms;")

# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (101, 3, '[{\"reg_no\": \"25BEC0001\", \"name\": \"Student1\", \"email\": \"student1@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0002\", \"name\": \"Student2\", \"email\": \"student2@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0003\", \"name\": \"Student3\", \"email\": \"student3@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (102, 3, '[{\"reg_no\": \"25BEC0004\", \"name\": \"Student4\", \"email\": \"student4@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0005\", \"name\": \"Student5\", \"email\": \"student5@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0006\", \"name\": \"Student6\", \"email\": \"student6@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (103, 3, '[{\"reg_no\": \"25BEC0007\", \"name\": \"Student7\", \"email\": \"student7@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0008\", \"name\": \"Student8\", \"email\": \"student8@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0009\", \"name\": \"Student9\", \"email\": \"student9@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (104, 3, '[{\"reg_no\": \"25BEC0010\", \"name\": \"Student10\", \"email\": \"student10@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0011\", \"name\": \"Student11\", \"email\": \"student11@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0012\", \"name\": \"Student12\", \"email\": \"student12@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (105, 3, '[{\"reg_no\": \"25BEC0013\", \"name\": \"Student13\", \"email\": \"student13@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0014\", \"name\": \"Student14\", \"email\": \"student14@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0015\", \"name\": \"Student15\", \"email\": \"student15@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (106, 3, '[{\"reg_no\": \"25BEC0016\", \"name\": \"Student16\", \"email\": \"student16@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0017\", \"name\": \"Student17\", \"email\": \"student17@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0018\", \"name\": \"Student18\", \"email\": \"student18@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (107, 3, '[{\"reg_no\": \"25BEC0019\", \"name\": \"Student19\", \"email\": \"student19@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0020\", \"name\": \"Student20\", \"email\": \"student20@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0021\", \"name\": \"Student21\", \"email\": \"student21@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (108, 3, '[{\"reg_no\": \"25BEC0022\", \"name\": \"Student22\", \"email\": \"student22@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0023\", \"name\": \"Student23\", \"email\": \"student23@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0024\", \"name\": \"Student24\", \"email\": \"student24@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (109, 3, '[{\"reg_no\": \"25BEC0025\", \"name\": \"Student25\", \"email\": \"student25@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0026\", \"name\": \"Student26\", \"email\": \"student26@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0027\", \"name\": \"Student27\", \"email\": \"student27@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (110, 3, '[{\"reg_no\": \"25BEC0028\", \"name\": \"Student28\", \"email\": \"student28@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0029\", \"name\": \"Student29\", \"email\": \"student29@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0030\", \"name\": \"Student30\", \"email\": \"student30@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (111, 3, '[{\"reg_no\": \"25BEC0031\", \"name\": \"Student31\", \"email\": \"student31@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0032\", \"name\": \"Student32\", \"email\": \"student32@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0033\", \"name\": \"Student33\", \"email\": \"student33@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (112, 3, '[{\"reg_no\": \"25BEC0034\", \"name\": \"Student34\", \"email\": \"student34@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0035\", \"name\": \"Student35\", \"email\": \"student35@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0036\", \"name\": \"Student36\", \"email\": \"student36@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (113, 3, '[{\"reg_no\": \"25BEC0037\", \"name\": \"Student37\", \"email\": \"student37@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0038\", \"name\": \"Student38\", \"email\": \"student38@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0039\", \"name\": \"Student39\", \"email\": \"student39@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (114, 3, '[{\"reg_no\": \"25BEC0040\", \"name\": \"Student40\", \"email\": \"student40@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0041\", \"name\": \"Student41\", \"email\": \"student41@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0042\", \"name\": \"Student42\", \"email\": \"student42@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (115, 3, '[{\"reg_no\": \"25BEC0043\", \"name\": \"Student43\", \"email\": \"student43@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0044\", \"name\": \"Student44\", \"email\": \"student44@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0045\", \"name\": \"Student45\", \"email\": \"student45@vitstudent.ac.in\"}]')")
# cur.execute("INSERT INTO Rooms (room_no, no_of_students, student_list) VALUES (116, 3, '[{\"reg_no\": \"25BEC0046\", \"name\": \"Student46\", \"email\": \"student46@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0047\", \"name\": \"Student47\", \"email\": \"student47@vitstudent.ac.in\"}, {\"reg_no\": \"25BEC0048\", \"name\": \"Student48\", \"email\": \"student48@vitstudent.ac.in\"}]')")

# conn.commit()

cur.execute("SELECT * FROM Students")

rows = cur.fetchall()
for r in rows:
    print(r)

cur.execute("SELECT * FROM Staff")
rows = cur.fetchall()
for r in rows:
    print(r)

cur.execute("SELECT * FROM Rooms")
rows = cur.fetchall()
for r in rows:
    print(r)