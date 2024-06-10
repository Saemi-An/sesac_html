from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'name' : 'Saemi',
     'age' : 28,
     'phone' : '010-6299-6040'},
     {'name' : 'Saemi',
     'age' : 45,
     'phone' : '010-2222-2222'},
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

@app.route('/search')
def search():
    name_query = request.args.get('name')   # /search?q=python
    age_query = request.args.get('age') 
    result = None

    if name_query:
        for u in users:
            print("user dict: ", u)
            if u['name'].lower() == name_query.lower():
                result = u
        # users = [u for u in users if name_query.lower() in u['name'].lower()]

    if age_query:
        result = [u for u in users if age_query in u['age']]
    
    print(result)

    return jsonify(result)

# @app.route('/search_user')
# def serach_user():
#     user_name = request.args.get('name')
#     found_user = None
#     for u in users:
#         if u['name'] == user_name:
#             found_user = u
#             return jsonify(found_user)


if __name__ == "__main__":
    app.run(port=5005)