from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def home(username):
    users = {
        "Huy": {
            "name": "Nguyễn Quang Huy",
            "age": 29,
            "lover": True,
        },
        "Duc": {
            "name": "H.duc",
            "age": 23,
            "lover": False,
        }
    }

    return "Hello"+", "+ str(users[username])

if __name__ == '__main__':
  app.run(debug=True)