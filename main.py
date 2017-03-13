from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# print(r"http://localhost:5000/")    # r=print all characters within ""


@app.route('/')
def home():
    return render_template("index.html")
    
''' 
@app.route("/<user>")

def index(user=None):
    # return "Method used: %s" % request.method
    return render_template("user.html", user=user) 
'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Wrong username/password, please try again'
        else:
            return redirect(url_for('home'))    
    return render_template("login.html", error=error)


@app.route('/shop')
def shop():
    food = ["Beer", "Pizza", "Kethcup"]
    return render_template("shop.html", food=food) 


@app.route('/page01')
def page01():
    return "<h2>This is page 2</h2>"


'''@app.route('/profile/<username>')
def profile(username):
    return "Hello %s" % username
'''
'''
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)
'''

'''
@app.route('/post/<int:post_id>')
def post(post_id):
    return "The Post_ID is %s" % post_id
'''

if __name__ == "__main__":
    app.run(debug=True)
    # app.run()