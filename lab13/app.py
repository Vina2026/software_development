"""
Neven Said
lab 13, Flask application
"""

from flask import Flask, render_template, redirect, url_for


""" create an object 'app' from the Flask module. 
    __ name__ set to __main__ if the script is running directly from the main file
"""
app = Flask(__name__)


# set the routing to the main page
# 'route' decorator is used to access to root URL

@app.route('/')
def index():
    name = "Neven Said"
    checkfruit = "Kiwi"
    fruits = ['apple', 'orange', 'grapes']
    return render_template('index.html', username=name, listfruits=fruits, checkfruit=checkfruit)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))


# set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug=True)    # to ensure debug mode is on

