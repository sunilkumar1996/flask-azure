from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return "It's Working from my Site on the server"

if __name__ == "__main__":
    app.run()