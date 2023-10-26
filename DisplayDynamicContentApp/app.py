from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    name = request.args.get('name')
    return f"Welcome {name}!"

if __name__ == '__main__' :
    app.run(host="0.0.0.0",port=5002)
 

