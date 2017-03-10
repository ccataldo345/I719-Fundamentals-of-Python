from flask import Flask, render_template

app = Flask(__name__)


#print(r"http://localhost:5000/")	#r=print all characters within ""
@app.route('/')
def index():
	return "Method used: %s" % request.method

@app.route('/method', methods=['GET', 'POST'])
def method():
	if request.method == 'POST':
		return "You are now using POST"
	else:
		return "You are now using GET"


@app.route('/page01')
def page01():
	return "<h2>This is page 2</h2>"


'''@app.route('/profile/<username>')
def profile(username):
	return "Hello %s" % username
'''
@app.route('/profile/<name>')
def profile(name):
	return render_template("profile.html", name=name)




@app.route('/post/<int:post_id>')
def post(post_id):
	return "The Post_ID is %s" % post_id


if __name__ == "__main__":
	app.run(debug=True)
