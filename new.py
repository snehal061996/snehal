from flask import Flask

app = Flask(__name__)

@app.route('/') # 127.0.0.1:5000
def welcome():
    return "Welcome To The Python Project"

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "Flask Web Devlopmecnt"



if __name__ == "__main__":
    app.run(debug=True)