from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def getData():
    if request.method == 'POST':
        userinput = request.form['userinput']
        return render_template('home.html',userinput=userinput)
    return render_template('index.html')
    

if __name__ == '__main__' :
    app.run(host="0.0.0.0",port=5002)
 

