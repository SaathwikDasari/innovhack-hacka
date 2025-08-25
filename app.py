from flask import Flask,jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/stafflog')
def stalog():
    return render_template('staffLogin.html')

@app.route('/stulogin')
def stulog():
    return render_template('stuLogin.html')

@app.route('/studash')
def studash():
    return render_template('snt_dashboard.html')

@app.route('/stadash')
def stadash():
    return render_template('staffdash.html')

@app.route('/staffdash2')
def stdash2():
    return render_template('staffdash2.html')

@app.route('/api/students')
def get_students():
    conn = sqlite3.connect('DORM_FRESH')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()
    
    students_list = [dict(row) for row in students]
    conn.close()
    
    return jsonify(students_list)

if __name__ == '__main__':
    app.run(debug=True)
