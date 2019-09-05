from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<username>", methods=['GET'])
def index(username):
    return "Hello, %s!" % username

if __name__ == "__main__":
    app.run(host='localhost', port=4567)