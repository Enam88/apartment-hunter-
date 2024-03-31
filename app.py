import os
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)