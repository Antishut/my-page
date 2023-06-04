from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def authenticate():
    username = request.form.get("username")
    password = request.form.get("password")

    # Add your authentication logic here
    if username == "admin" and password == "password":
        return "Login successful"
    else:
        return "Login failed"

if __name__ == "__main__":
    app.run()








