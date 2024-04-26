from flask import Flask
app = Flask(__name__)


@app.route('/')
def web():
    return 'this is web by using python'


if __name__ == "__main__":
    app.run(debug=True)
