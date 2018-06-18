from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            "title" : "Thơ Con Ếch",
            "content" : "Cau 1 Cau 2 Cau 3",
            "author" : "xxx",
            "gender" : 1
        },
        {
            "title" : "Thơ Con Coc",
            "content" : "Cau 4 Cau 5 Cau 6",
            "author" : "yyy",
            "gender" : 0
        },
        {
            "title" : "Thơ Con Chim",
            "content" : "Cau 7 Cau 8 Cau 9",
            "author" : "zzz",
            "gender" : 1
        }
    ]
    return render_template("index.html",posts = posts)

@app.route('/hello')
def say_hello():
    return 'Hello C4E18'

@app.route('/hi/<name>/<age>')
def say_hi(name,age):
    return "hi {0}, you're {1} years old".format(name,age)

@app.route('/sum/<int:numb1>/<int:numb2>')
def sum(numb1,numb2):
    return str(numb1 + numb2)
    


if __name__ == '__main__':
  app.run(debug=True)
 