from flask import Flask, render_template


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

if __name__ == '__main__':
    app.run(debug=True)