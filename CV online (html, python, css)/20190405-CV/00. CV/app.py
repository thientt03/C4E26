from flask import Flask,render_template, redirect, request,session,redirect
import user,dbuser,db
app = Flask(__name__)
app.config["SECRET_KEY"]="ailanguoiay"

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/interface')
def interface():
    
    return render_template("interface.html")

@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login2.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.find_by_username(username) == None or user.find_by_password(password) == None:
            return render_template("error.html")
        else:
            # user_id=user.find_by_username(str(username))["_id"]
            # _id=user.get_by_id(user_id)
            # session["key"]=_id
            session["token"]=username
            return redirect('/add')
@app.route("/signin",methods = ["GET","POST"])
def signin():
    if request.method=="GET":
        return render_template("signin.html")
    elif request.method=="POST":
        form=request.form
        u=form["username"]
        p=form["password"]
        if user.find_by_username(str(u))==None:

            new_user={
                "username": str(u),
                "password": str(p),
            }
            db.user_collection.insert_one(new_user)
            return render_template("home.html")
        elif user.find_by_username(str(u))!= None:
            return render_template("errorsign.html")
        if str(u)==None:
            return "kkk"
        
@app.route("/add", methods = ["GET","POST"])
def add():
    if "token" in session:   
        if request.method == "GET":
            cv=user.get_cv(session["token"])
            if cv == None:
                return render_template("interfaceform.html")
            else:
                # form = request.form
                img_file= cv["image"]
                cvtitle = cv["cvtitle"]
                fullname = cv["fullname"]
                nominee = cv["nominee"]
                dateofbirth = cv["dateofbirth"]
                sex = cv["sex"]
                numberphone = cv["numberphone"]
                addressemail = cv["addressemail"]
                address = cv["address"]
                website = cv["website"]
                awareness = cv["awareness"]
                hobby = cv["hobby"]
                schoolname = cv["schoolname"]
                startschool = cv["startschool"]
                endschool = cv["endschool"]
                majors = cv["majors"]
                describe = cv["describe"]
                companyname = cv["companyname"]
                startcompany = cv["startcompany"]
                endcompany = cv["endcompany"]
                locationcompany = cv["locationcompany"]
                jobdescription = cv["jobdescription"]
                prize = cv["prize"]
                timeprize = cv["timeprize"]
                softskill = cv["softskill"]
                namecertificate = cv["namecertificate"]
                typecertificate = cv["typecertificate"]
                diffirent = cv["diffirent"]
                _id_user=session["token"]
                # user_status = form["user_status"]
                # dbuser.infuser(cvtitle,fullname,nominee,dateofbirth,sex,numberphone,addressemail,address,website,awareness,hobby,skillname,schoolname,startschool,endschool,majors,describe,companyname,startcompany,endcompany,locationcompany,jobdescription,prize,timeprize,softskill,namecertificate,typecertificate,diffirent,_id_user)
                image = dbuser.search_image(img_file)
                # return render_template("interfaceout.html")
                return render_template("interfaceout.html",img_file=image,cvtitle = cvtitle, fullname = fullname, nominee = nominee, dateofbirth = dateofbirth,sex = sex, numberphone = numberphone, addressemail = addressemail, address = address, website = website, awareness = awareness, hobby = hobby, schoolname = schoolname, startschool = startschool, endschool = endschool, majors = majors, describe = describe, companyname = companyname, startcompany = startcompany, endcompany = endcompany, locationcompany = locationcompany, jobdescription = jobdescription, prize = prize, timeprize = timeprize,softskill = softskill, namecertificate = namecertificate, typecertificate = typecertificate, diffirent = diffirent)
        elif request.method == "POST":

            form = request.form
            img_file = form['base64']
            cvtitle = form["cvtitle"]
            fullname = form["fullname"]
            nominee = form["nominee"]
            dateofbirth = form["dateofbirth"]
            sex = form["sex"]
            numberphone = form["numberphone"]
            addressemail = form["addressemail"]
            address = form["address"]
            website = form["website"]
            awareness = form["awareness"]
            hobby = form["hobby"]
            schoolname = form["schoolname"]
            startschool = form["startschool"]
            endschool = form["endschool"]
            majors = form["majors"]
            describe = form["describe"]
            companyname = form["companyname"]
            startcompany = form["startcompany"]
            endcompany = form["endcompany"]
            locationcompany = form["locationcompany"]
            jobdescription = form["jobdescription"]
            prize = form["prize"]
            timeprize = form["timeprize"]
            softskill = form["softskill"]
            namecertificate = form["namecertificate"]
            typecertificate = form["typecertificate"]
            diffirent = form["diffirent"]
            _id_user=session["token"]
            # user_status = form["user_status"]
            dbuser.infuser(img_file,cvtitle,fullname,nominee,dateofbirth,sex,numberphone,addressemail,address,website,awareness,hobby,schoolname,startschool,endschool,majors,describe,companyname,startcompany,endcompany,locationcompany,jobdescription,prize,timeprize,softskill,namecertificate,typecertificate,diffirent,_id_user)
            image = dbuser.search_image(img_file)
            # return render_template("interfaceout.html")
            return render_template("interfaceout.html",img_file=image ,cvtitle = cvtitle, fullname = fullname, nominee = nominee, dateofbirth = dateofbirth,sex = sex, numberphone = numberphone, addressemail = addressemail, address = address, website = website, awareness = awareness, hobby = hobby, schoolname = schoolname, startschool = startschool, endschool = endschool, majors = majors, describe = describe, companyname = companyname, startcompany = startcompany, endcompany = endcompany, locationcompany = locationcompany, jobdescription = jobdescription, prize = prize, timeprize = timeprize,softskill = softskill, namecertificate = namecertificate, typecertificate = typecertificate, diffirent = diffirent)

    # def screen():
    #   return render_template("interface.html")

@app.route("/up", methods = ["GET","POST"])
def up():
    if request.method == "GET":
        return render_template("interfaceform.html")
    elif request.method == "POST":

            form = request.form
            img_file = form['base64']
            cvtitle = form["cvtitle"]
            fullname = form["fullname"]
            nominee = form["nominee"]
            dateofbirth = form["dateofbirth"]
            sex = form["sex"]
            numberphone = form["numberphone"]
            addressemail = form["addressemail"]
            address = form["address"]
            website = form["website"]
            awareness = form["awareness"]
            hobby = form["hobby"]
            schoolname = form["schoolname"]
            startschool = form["startschool"]
            endschool = form["endschool"]
            majors = form["majors"]
            describe = form["describe"]
            companyname = form["companyname"]
            startcompany = form["startcompany"]
            endcompany = form["endcompany"]
            locationcompany = form["locationcompany"]
            jobdescription = form["jobdescription"]
            prize = form["prize"]
            timeprize = form["timeprize"]
            softskill = form["softskill"]
            namecertificate = form["namecertificate"]
            typecertificate = form["typecertificate"]
            diffirent = form["diffirent"]
            _id_user=session["token"]
            # user_status = form["user_status"]
            dbuser.infuser(img_file,cvtitle,fullname,nominee,dateofbirth,sex,numberphone,addressemail,address,website,awareness,hobby,schoolname,startschool,endschool,majors,describe,companyname,startcompany,endcompany,locationcompany,jobdescription,prize,timeprize,softskill,namecertificate,typecertificate,diffirent,_id_user)
            image = dbuser.search_image(img_file)
            # return render_template("interfaceout.html")
            return render_template("interfaceout.html",img_file=image ,cvtitle = cvtitle, fullname = fullname, nominee = nominee, dateofbirth = dateofbirth,sex = sex, numberphone = numberphone, addressemail = addressemail, address = address, website = website, awareness = awareness, hobby = hobby, schoolname = schoolname, startschool = startschool, endschool = endschool, majors = majors, describe = describe, companyname = companyname, startcompany = startcompany, endcompany = endcompany, locationcompany = locationcompany, jobdescription = jobdescription, prize = prize, timeprize = timeprize,softskill = softskill, namecertificate = namecertificate, typecertificate = typecertificate, diffirent = diffirent)
    
def remov():
    dbuser.infuser_collection.drop()
if __name__ == '__main__':
  app.run(debug=True)