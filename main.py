from flask import Flask, redirect, render_template, url_for
from admin.second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")


@app.route("/")
def users():
    return "<h1>Test</h1>"


if __name__=="__main__":
    app.run(debug=True)