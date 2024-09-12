from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, Moon lover!</h1>"

@app.route('/<username>')
def user(username):
    return f"<h1>Profile for {username}</h1>"

@app.route('/about')
def about():
    return "<h1>About page</h1>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)

# from flask import Flask 
# app Flask(__name__)
# @app.route('/')
# def index():
#     return 'Hello, Moon lover!'
