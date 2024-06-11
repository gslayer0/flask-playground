from flask import Flask, render_template
import requests

app = Flask(__name__)

# Generate custom decorator

def decoratorFactory(route):
    def myDecorator(func):
        def wrapper(*args, **kwargs):
            print("user mengakses route: " + route)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return myDecorator
        


@app.route("/")
@decoratorFactory("/")
def index():
    return render_template("index.html")

app.run(host="0.0.0.0", port=80)