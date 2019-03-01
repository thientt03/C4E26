from flask import Flask
app = Flask(__name__)
#x: cân nặng
#y: chiều cao
@app.route('/bmi/<int:x>/<int:y>')
def check(x,y):
    y = y/10
    BMI = x / (y*y)
    if BMI < 16:
        return "BMI < 16: Severely underweight"
    elif 16 <= BMI < 18.5:
        return "16 <= BMI < 18.5: Underweight"
    elif 18.5 <= BMI < 25: 
        return "18.5 <= BMI < 25: Normal"
    elif 25 <= BMI and BMI < 30: 
        return "25 <= BMI < 30: Overweight"
    elif BMI > 30: 
        return "BMI > 30: Obese"
# cách 2: thay các dấu so sánh bằng and :)))

    return str(check)

if __name__ == '__main__':
  app.run(debug=True)