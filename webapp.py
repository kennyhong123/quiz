
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
    session['q1'] = request.form['a1']
    session['q2'] = request.form['a2']
    session['q3'] = request.form['a3']
    session['q4'] = request.form['a4']
    return render_template('.html')
  
    
if __name__=="__main__":
    app.run(debug=False)
