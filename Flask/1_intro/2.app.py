from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route("/user/<name>")   # <name>은 변수. 이 변수명과 함수의 인자를 매칭해서 내부에서 처리
def user(name):
    username = name
    return f"""
            <h1>User : {username}</h1>
            <p>Welcome, <b>{username}</b>.</br> Please enjoy our service</p>"""

@app.route("/user/<int:age>")
def userage(age):
    return f"<h1>Age: {age}</h1>"

@app.route("/user/<float:weight>")
def userweight(weight):
    return f"<h1>Weight: {weight}</h1>"

@app.route("/user/<name>/<int:age>")
def usernameage(name, age):
    return f"<h1>Hello, {name}, your age is {age}.</h1>"

@app.route("/user/<name>/<int:age>/<float:weight>")
def usernameageweight(name, age, weight):
    return f"""<h1>Hello, {name}</h1>
                <p> your age is {age}. Your weight is {weight}KG.</p>"""

if __name__ == "__main__":
    app.run(debug=True)