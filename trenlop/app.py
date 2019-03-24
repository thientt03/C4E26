from flask import Flask,render_template,request, session,redirect
import food
app = Flask(__name__)
app.config["SECRET_KEY"] = "adfsietrngjwfnbl243r905647"

@app.route("/login", methods = ["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login_form.html")
  elif request.method == "POST":
    #login logic
    #1. lấy từ db
    username = request.form["username"]
    password = request.form["password"]
    if username != "admin": #check usre trong db
      return "No such user"
    elif password != "789852": ##check pass trong db
      return "Wrong pass"
    else:
      session["token"] = username
      return "OK"
    #2. Hash(bcrypt) vd: ilovemovie => aji3nb34sdvkkldsv
@app.route("/logout")
def logout():
  del session["token"]
  return redirect("/login")


@app.route("/food_list") #ALL => List/Master
def food_list():
    if "token" in session:
      #B1 GET ALL FOOD 1.Funton ? 2.Write funtion ?
      all_food = food.get({}) #lấy hết.
      #B2: render: ALL FOOD + html

      #B3: Return

      return render_template("food_list.html", f_list=all_food)
    else:
      return "Unauthentacated"
@app.route("/food/<id>")
def food_detail(id):
    f = food.get_by_id(id)
    return render_template("food_detail.html",food = f,user="Thiện")

@app.route("/add_food",methods = ["GET","POST"])
def add_food():
  if request.method == "GET":
    return render_template("food_form.html")
  elif request.method == "POST":
    form = request.form
    n = form["name"]
    p = form["price"]
    food.add_food(n,p)
    return "YES"

if __name__ == '__main__':
  app.run(debug=True)
