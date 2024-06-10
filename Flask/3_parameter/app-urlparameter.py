from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'name' : 'Saemi',
     'age' : 28,
     'phone' : '010-6299-6040'},
    {'name' : 'Song',
     'age' : 32,
     'phone' : '010-6666-6666'},
    {'name' : 'Sun-a',
     'age' : 29,
     'phone' : '010-1234-5678'}
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/user/<name>')
def search_user(name):
    user = None
    for u in users:
        if u['name'].lower() == name.lower():
            user = u
            break
        if str(u['age']) == name:
            user = u

    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error' : 'User not found'}), 404
    # 결과가 있을 때는 지금처럼(응답 및 200)
    # 결과가 없을 때는, 응답값에 404

if __name__ == "__main__":
    app.run(debug=True)