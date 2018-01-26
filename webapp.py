
import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    return render_template('index.html')
  
@app.route('/response',methods=['GET','POST'])
def renderScore():
    session['q1'] = request.form['n1']
    session['q2'] = request.form['n2']
    session['q3'] = request.form['n3']
    session['q4'] = request.form['n4']
    session['q5'] = request.form['n5']
    return render_template('.html')
  
    
if __name__=="__main__":
    app.run(debug=False)
