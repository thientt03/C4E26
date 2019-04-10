from flask import Flask,render_template,request
app = Flask(__name__)

items = [
    {
        "name": "Cơm rang",
        "price": 25000,
    }, 
    {
        "name": "Phở bò",
        "price": 30000,
    }, 
    {
        "name": "xôi",
        "price": 10000,
    },
    ]


@app.route('/')
def menu():
    return render_template("menu.html", item_list = items, user = "Thiện" )

@app.route("/food/<int:i>") #1 => detail
def food(i):
    f = items[i]
    return render_template("food_detail.html", item = f)

@app.route('/add_food', methods = ["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("food_form.html")
    elif request.method == "POST":
        form = request.form
        n = form["name"]
        p = form["price"]
        new_item = {
            "name": n,
            "price": p,
        }
        items.append(new_item)
        return "chúc mừng"+ n + " " + str(p)
if __name__ == '__main__':
  app.run(debug=True)