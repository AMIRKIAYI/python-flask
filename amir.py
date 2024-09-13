from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello, Hackers!</h1>"

@app.route('/<username>')

def user(username):
    return f"<h1>Hello, {username}! you must be a hero in this journey</h1>"

@app.route('/about')
def about():
    return "<h1>About us page is designed to give more details of our web</h1>"

if __name__== '__main__':
    app.run(port=5000,debug=True)  # run the app in debug mode


