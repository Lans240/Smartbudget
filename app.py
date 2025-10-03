# app.py - минимальная структура Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'SmartBudget - Главная страница'

if __name__ == '__main__':
    app.run(debug=True)