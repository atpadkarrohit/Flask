from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/pageone")
def pageone():
     return render_template("pageone.html")


@app.route("/pagetwo")
def pagetwo():
     return render_template("pagetwo.html")


if __name__ == '__main__' :
    app.run(host="0.0.0.0",port=5002)


