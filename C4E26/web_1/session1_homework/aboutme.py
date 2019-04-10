from flask import Flask
from flask import Flask
app = Flask(__name__)

@app.route('/about-me')
def me():
    me = {
        "Họ và tên": "Trần Khánh Thiện",
        "Sinh viên": "Trường ĐHKHTN-Khóa K62",
        "Sđt": "0974807782",
        "Sở thích": "đá bóng and code for fun",
    }
     
    return str(me)

if __name__ == '__main__':
  app.run(debug=True)