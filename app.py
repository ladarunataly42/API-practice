from flask import Flask
app=Flask(__name__)

@app.route("/home")
def hello():
    return "Welcome!", 200

if __name__ == '__main__':
    app.run()