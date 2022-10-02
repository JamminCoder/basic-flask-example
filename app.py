from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def display_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def handle_form():
    # Extract username + email from the `form` dictionary of the request
    username = request.form["username"]
    email = request.form["email"]

    # Pass in the extracted username + email to the display_info template and return it
    return render_template("display_info.html", username=username, email=email)
