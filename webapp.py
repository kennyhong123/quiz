
import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    return render_template('index.html')
	
@app.route('/retake')
def renderBack():
	session.clear()
	return render_template('index.html')
	
@app.route('/response',methods=['GET','POST'])
def renderScore():
	return render_template('score.html')
  
    
if __name__=="__main__":
    app.run(debug=False)
