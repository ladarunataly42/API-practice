from flask import Flask,request
from actions import Actions
app=Flask(__name__)


@app.route("/home")
def hello():
    return "Welcome!", 200

@app.route("/dog-list", methods=['GET','POST','DELETE'])
def dog_list():
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass


    elif request.method == 'DELETE':
        pass

if __name__ == '__main__':
    app.run()