from flask import Flask, url_for, render_template, request
import pyrebase

config = {
    'apikey': 'AIzaSyBOuRNJdvdbb2x0qFWVHpZxbfiHS60EL5U',
    'authDomain': 'avoidthebugs-b6e6e.firebaseapp.com',
    'databaseUR'L: "https://avoidthebugs-b6e6e.firebaseio.com",
    'projectId': "avoidthebugs-b6e6e",
    'storageBucket': "avoidthebugs-b6e6e.appspot.com",
    'messagingSenderId': "704938442068"
}

app = Flask(__name__)

@app.route('/') # home page
def mainPage(): return render_template('main.html')

@app.route('/game') # game page
def gamePage(): return render_template('game.html')

@app.route('/credits') # credits page
def creditsPage(): return render_template('credits.html')

if __name__ == '__main__':
    app.run(port=5003,debug=False)