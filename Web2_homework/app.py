from flask import Flask,render_template,request
app = Flask(__name__)

bike_list = [
    {
        "model": "honda",
        "daily_fee": 10000,
        "image": "https://www.shannons.com.au/auctions/2016-shannons-sydney-winter-classic-auction/O5YDZ5PA1EIW4M44/",
        "year": 1990,
    }
]
@app.route('/')
def home():
    return render_template("menu_bike.html", bike = bike_list)

@app.route("/new_bike", methods = ["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("model.html")
    if request.method == "POST":
        form = request.form
        n = form["model"]
        m = form["daily_fee"]
        p = form["image"]
        q = form["year"]
        new_item = {
            "model": n,
            "daily_fee": m,
            "image": p,
            "year": q,
        }
        
        print(new_item)
if __name__ == '__main__':
  app.run(debug=True)