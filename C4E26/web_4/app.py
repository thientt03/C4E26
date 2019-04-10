from flask import *
import car
app = Flask(__name__)

@app.route('/car')
def food_list():
    # Get all food 1. Function ??, 2. Wirte Function??
    all_car = car.get({})
    # Render: food + html
    # Return
    return render_template("car_list.html", all_car = all_car)

@app.route("/car/<id>")
def car_detail(id):
    f = car.get_by_id(id)
    return render_template("car_detail.html")

@app.route("/add_car")
def add_car():
  if request.method == "GET":
    return render_template("car_form.html")
  elif request.method == "POST":
    form = request.form
    n = form["producer"]
    m = form["price"]
    p = form["color"]
    car.add_car(n,m,p)
    
    
    

if __name__ == '__main__':
  app.run(debug=True)