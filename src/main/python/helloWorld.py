from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello Worldyyyyy!"

@app.route("/<username>")
def hello_vathsan(username):
	return f"Hello {username}!"