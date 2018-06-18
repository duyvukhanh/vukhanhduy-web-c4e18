from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def aboutme(): 
    return "Name : Vu Khanh Duy | Work : Student at EPU | Hobbies : Football"

@app.route('/school')
def school():
    return redirect("http://techkids.vn")

# ex1 : without render_template
# @app.route('/bmi/<int:weight>/<int:height>')
# def bmii(weight,height):
#     result = ""
#     bmi = weight/((height/100)**2)
#     if bmi < 16:
#         result = "Your BMI:" + str(bmi) + " | Severely underweight"
#     if 16 <= bmi < 18.5:
#         result = "Your BMI:"+str(bmi)+" | Underweight"
#     if 18.5 <= bmi < 25:
#         result = "Your BMI:"+str(bmi)+" | Normal"
#     if 25 <= bmi < 30:
#         result = "Your BMI:"+str(bmi)+" | Overweight"
#     else:
#         result = "Your BMI:"+str(bmi)+" | Obese"
#     return result

# ex1 : with render_template
@app.route('/bmi/<int:weight>/<int:height>')
def bmii(weight,height):
    result = ""
    bmi = weight/((height/100)**2)
    if bmi < 16:
        result = "Severely underweight"
    if 16 <= bmi < 18.5:
        result = "Underweight"
    if 18.5 <= bmi < 25:
        result = "Normal"
    if 25 <= bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return render_template("ex1.html",bmi = bmi,result = result)

@app.route('/user/<username>')
def xxx(username):
    users = {
        "quy" : {
            "name" : "Đinh Công Quý",
            "age" : 21,
            "hobbies" : "Chơi púp pê"
        },
        "tuananh" : {
            "name" : "Nguyễn Tuấn Anh",
            "age" : 23,
            "hobbies" : "Fap"
        },
        "duy" : {
            "name" : "Vũ Khánh Duy",
            "age" : 22,
            "hobbies" : "Em gái Hà"
        }
    }
    return render_template("ex2.html",users=users,username = username)

if __name__ == '__main__':
  app.run(debug=True)
 
