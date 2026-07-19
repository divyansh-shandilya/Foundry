import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, Response
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from PROJECTS.CS50.project.helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///data.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def home():
    user_id = session.get("user_id")

    if user_id:
        return redirect("/dashboard")

    return render_template("home.html")

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        svg_name = request.form.get("name")
        svg_code = request.form.get("svg")

        if not svg_name:
            return apology("please provide name")

        if not svg_code:
            return apology("please provide svg")

        if "<svg" not in svg_code or "</svg>" not in svg_code:
            return apology("Invalid SVG")

        db.execute("INSERT INTO svgs (user_id, name, svg_code) VALUES (?, ?, ?)",session["user_id"],svg_name,svg_code)

        return redirect("/")

    svgs = db.execute("SELECT * FROM svgs WHERE user_id = ? ORDER BY created_at DESC", session["user_id"])

    return render_template("list.html", svgs=svgs)

@app.route("/svg/<int:svg_id>")
@login_required
def view_svg(svg_id):
    rows = db.execute(
        "SELECT svg_code FROM svgs WHERE id = ? AND user_id = ?",
        svg_id,
        session["user_id"]
    )

    if not rows:
        return apology("SVG not found")

    svg_code = rows[0]["svg_code"].strip()

    return Response(svg_code, mimetype="image/svg+xml")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/delete/<int:svg_id>", methods=["POST"])
@login_required
def delete(svg_id):
    db.execute("DELETE FROM svgs WHERE id = ? AND user_id = ?",svg_id,session["user_id"])

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Must Provide Symbol")
        stk = lookup(symbol)
        if stk is None:
            return apology("Invalid Symbol")

        return render_template("result.html", stk_name=stk["name"], stk_price=stk["price"], stk_symbol=stk["symbol"])



@app.route("/list", methods=["GET", "POST"])
@login_required
def list():
    return redirect("/")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        confirmation = request.form.get("confirmation")
        if not name:
            return apology("Name Not Found")
        elif not password:
            return apology("Password Not Found")
        elif not email:
             return apology("Emaiil Not Found")
        elif not password == confirmation:
                        return apology("name Already Exists")


        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))

        # Ensure username exists and password is correct
        if len(rows) >= 1:
            return apology("Already Registered", 403)

        hashed_password = generate_password_hash(password)
        user_id = db.execute("INSERT INTO users (username, hash, email) VALUES (?,?,?)", name, hashed_password, email)
        session["user_id"] = user_id
        return redirect("/")

