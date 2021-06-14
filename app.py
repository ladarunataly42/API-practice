import json

from flask import Flask,request
from actions import Actions
app=Flask(__name__)


@app.route("/home")
def hello():
    return "Welcome!", 200

@app.route("/dog-list", methods=['GET','POST','DELETE'])
def dog_list():
    if request.method == 'GET':
        return {
            'result':Actions.get_data()
        },200

    elif request.method == 'POST':
        column_name=request.json
        return{
            'result':Actions.give_data(column_name['column_name'])
        },200


    elif request.method == 'DELETE':
        pass

if __name__ == '__main__':
    app.run()
