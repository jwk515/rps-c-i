from flask import Flask

app = Flask(__name__)


# when someone visits the home page "/" in the browser,
# this function will be called
# and the return value will be displayed in the browser
@app.route('/')
def home():
    return "Welcome to the Rock Paper Scissors Game!"



if __name__ == "__main__":

    app.run(debug=True)
