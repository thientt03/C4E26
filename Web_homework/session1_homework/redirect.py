import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/school/1')
def home():
    return redirect("http://techkids.vn/", code= 302, Response= None)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)