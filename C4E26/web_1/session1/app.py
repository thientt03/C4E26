from flask import Flask
app = Flask(__name__)

#đẩy vào json:
#bind route to view function
@app.route('/')
def home():#view function
    return"C4E26, hihi"

@app.route("/thien")
def clas():
    return"C4E26,...."

@app.route("/hi/<name>")
def sm(name):
    return"hi " + ", " +name

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    s = x + y
    return str(s)
mn = ["cơm", "phở", "bún"]
@app.route("/menu")
def menu():
    return str(mn)
@app.route("/food/<int:x>")
def food(x):
    return mn[x]

if __name__ == '__main__':
  app.run(debug=True)

