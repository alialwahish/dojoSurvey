from flask import Flask,render_template,redirect,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/process',methods=["POST"])
def process():
    servFrm=request.form
    print servFrm
    return render_template('result.html',servFrm=servFrm)
app.run(debug=True)