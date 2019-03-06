from flask import Flask, render_template, request
app = Flask(__name__)

gara = [
    {
        "producer": "Suzuki",
        "price": 1,
        "color": "black",
    },
    {
        "producer": "Mercedes",
        "price": 5,
        "color": "white",
    },
    {
        "producer": "Ferarri",
        "price": 10,
        "color": "black",
    },
]
@app.route('/')
def home():
    return render_template("menu_oto.html", gara_list = gara, user = "Thiện")

@app.route("/oto/<int:i>", methods = ["GET", "POST"])
def oto(i):
    f = gara[i]
    if request.method == "GET":
        return render_template("form_oto.html",item = f)
    elif request.method == "POST":
        form = request.form
        n = form["producer"]
        m = form["price"]
        p = form["color"]
        oto_list = {
            "producer": n,
            "price": m,
            "color": p,
        }
        return "chúc mừng Thiện đã mua thành công"+ str(oto_list)
if __name__ == '__main__':
  app.run(debug=True)