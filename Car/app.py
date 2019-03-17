from flask import Flask, render_template
import car
app = Flask(__name__)

@app.route('/car')
def food_list():
    # Get all food 1. Function ??, 2. Wirte Function??
    all_car = car.get({})
    # Render: food + html
    # Return
    return render_template("car_list.html", f_list = all_car)

@app.route("/car/<id>")
def car_detail(id):
    f = car.get_by_id(id)
    return f["producer"]

if __name__ == '__main__':
  app.run(debug=True)