from flask import Flask, render_template, url_for, flash, redirect
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

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Log in unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", title="Register", form=form)

if __name__ == "__main__":
    app.run(debug=True)