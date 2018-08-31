from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/') # home page
def mainPage(): return render_template('main.html')

@app.route('/game') # game page
def gamePage(): return render_template('game.html')

@app.route('/credits') # credits page
def creditsPage(): return render_template('credits.html')

if __name__ == '__main__':
    app.run(port=5000,debug=False)