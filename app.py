import re
from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/',methods=['POST' , 'GET'])
def home():
    return render_template('home.html')
@app.route('/results',methods=['POST'])
def results():
        var1 = request.form.get('regrex')
        var2 = request.form.get('text')
        m =[]
        m = re.findall(var1, var2)
        return render_template('results.html',m=m,var1=var1,var2=var2)
if __name__ =="__main__":
    app.run(debug=True)
