# Basic Flask usage example

###### Helpful documentation:
- [Flask Quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/#)
- [Routing in Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing)
- [Flask Requests](https://flask.palletsprojects.com/en/2.2.x/quickstart/#accessing-request-data)
- [Using HTML Templates in Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates)

## To see example
```
pip install flask
```

Then if on Linux run:
```
export FLASK_ENV=development
```

If on Windows run:
```
set FLASK_ENV=development
```

#### Then start the server

```
flask --app app run
```

You will then see a message printed similar to this:
```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

Then open the `index.html` file in a web browser, and click the buttons to send GET and POST requests to the server. Also check the browser console to see the output.
### Note: You may need to change the `SERVER_URL` variable in `index.html` to match the port that your Flask app is running on.