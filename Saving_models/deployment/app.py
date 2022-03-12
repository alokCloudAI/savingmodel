from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

#code business logib

@app.route('/')
def base():
    return render_template('home.html')

@app.route('/galary')
def galary():
    return render_template('galry.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Cart')
def Cart():
    return 'Welecome to Cart'


app.run(debug= True)
