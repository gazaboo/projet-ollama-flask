from flask import Flask

# __name__ : double underscore variables (dunders)
app = Flask(__name__) 

@app.route("/")
def hello_world():
    return "<p>Hello, Campus !</p>"

@app.route("/campus")
def hello_campus():
    return "<p>Demo</p>"

app.run(debug=True, port=5001)

