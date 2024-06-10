from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, my Flask server</h1>"

@app.route("/user/")
@app.route("/user/<name>")   # <name>은 변수. 이 변수명과 함수의 인자를 매칭해서 내부에서 처리
def user(name=None):
    username = name
    return f"""
            <h1>User : {username}</h1>
            <p>Welcome, <b>{username}</b>.</br> Please enjoy our service</p>"""

@app.route("/admin")
def admin():
    return "<h1>Admin</h1>"

if __name__ == "__main__":
    app.run(port=5000, debug=True)   # debug=True - 개발환경에서만 사용!