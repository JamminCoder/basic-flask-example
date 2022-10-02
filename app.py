from flask import Flask, request
import flask


app = Flask(__name__)


"""
These are examples of using Flask as an API 
from an external app not hosted on the same server.
"""

@app.route("/api/get")
def api():
    # The data you want to send back to the client
    res_data = {
        "user": "john",
        "email": "johndoe@gmail.com",
        "phone": "+1 234-5678-9012"
    }

    # Create a response using the your data
    res = flask.make_response(res_data)

    res.headers["Access-Control-Allow-Origin"] = "*" # This is needed to allow outside requests to access this resource

    # Send the response back to the client
    return res


@app.route("/api/post", methods=["POST"])
def api_submit():
    # Extract the "name" and "email" values from the posted data
    name = request.form["name"]
    email = request.form["email"]
    
    # The data to send back to the client
    res_data = f"Successfully posted name: { name }, email: { email }"

    # Create the response using your data
    res = flask.make_response(res_data)

    res.headers["Access-Control-Allow-Origin"] = "*"

    # Send response back to client
    return res