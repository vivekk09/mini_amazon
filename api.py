from flask import Flask,render_template,request,redirect,url_for,session

app = Flask(__name__)
app.secret_key='hello'


@app.route('/')

def home():
	return render_template('home.html',title='home')

@app.route('/about')

def about():
	return render_template('about.html',title='about')

@app.route('/contact')

def contact():
	return render_template('contact.html',title='contact')


@app.route('/login',methods=['GET','POST'])
def login():

	if request.method=='POST':

		users={
		'user1':'123',
		'user2':'234',
		'user3':'1234',
		'user4':'2345'
		}

		username= request.form['username']
		password= request.form['password']

		if username not in users:
			return "user doesn't exist. Go back and enter a valid username"

		if users[username]!=password:
			return "password doesn't match. Go back and re-enter the password"


		session['username']=username

		return redirect(url_for('home'))

	return redirect(url_for('home'))

@app.route('/logout')
def logout():

	session.clear()
	return redirect(url_for('home'))


app.run(debug=True)