from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/'); # home page
def mainPage():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(port=5000,debug=false)