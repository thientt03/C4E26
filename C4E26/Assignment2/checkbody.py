print("chuyển đổi từ cm sang m")
height = float(input("Nhập chiều cao : "))
weight = float(input("Nhập cân nặng : "))
BMI = float( weight/(height*height))

if BMI < 16:
    print("Severely underweight ")
elif 16 <= BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")
