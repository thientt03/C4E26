from flask import Flask,render_template, redirect, request
import user
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.find_by_username(username) == None:
            return render_template("interface.html")
        elif user.find_by_password(password) == None:
            return render_template("interface.html")
        else:
            return render_template("interfaceform.html")
# def screen():
#   return render_template("interface.html")
    

if __name__ == '__main__':
  app.run(debug=True)