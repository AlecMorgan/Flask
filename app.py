from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# Secret key protects user info against cross-site attacks, forgery attacks, modifying cookies, etc. 
app.config["SECRET_KEY"] = "d999e90ce8651b10174c53aed948f1ba"

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "September 29th 2019"
    },
    {
        "author": "Margaret Rouse",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "September 30th 2019"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Register", form=form)

if __name__ == "__main__":
    app.run(debug=True)