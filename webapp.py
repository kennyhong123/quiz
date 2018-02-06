import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

highscore = 0

@app.route('/')
def renderMain():
    return render_template('index.html')
	
@app.route('/retake')
def renderBack():
	session.clear()
	return render_template('index.html')
	
@app.route('/response',methods=['GET','POST'])
def renderScore():
	global highscore
	session['score']=0
	if request.form['n1']=="panda":
		session['score']+=1
	if request.form['n2']=="lion":
		session['score']+=1
	if request.form['n3']=="turtle":
		session['score']+=1
	if request.form['n4']=="zebra":
		session['score']+=1
	if request.form['n5']=="bear":
		session['score']+=1
	if highscore < session['score']:
		highscore = session['score']
	return render_template('score.html', hscore=highscore)
  
    
if __name__=="__main__":
    app.run(debug=False)
