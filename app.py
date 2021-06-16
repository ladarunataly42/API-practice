import json

from flask import Flask,request
from actions import Actions
app=Flask(__name__)
processor=Actions.get_data()

@app.route("/home")
def hello():
    return "Welcome!", 200

@app.route("/dog-list", methods=['GET','POST'])
def dog_list():
    if request.method == 'GET':
        return {
            'result':processor
        },200

    elif request.method == 'POST':
        column_name=request.json
        return{
            'result':Actions.give_data(column_name['column_name'])
        },200



@app.route("/update-dog-list", methods=['PATCH','POST','PUT'])
def update_dog_list():
    if request.method == 'PATCH':
        data=request.json
        value=list(data.values())
        key=list(data.keys())

        return{
            'result':Actions.get_request(processor,key[1], value)
        }


    elif request.method == 'POST':
        data=request.json
        value=list(data.values())
        key=list(data.keys())
        return {
            'result': Actions.add_row(processor,key,value)
        }

    elif request.method == 'PUT':
        data = request.json
        value = list(data.values())
        key = list(data.keys())
        return {
            'result': Actions.modify_row(processor, key, value)
        }

if __name__ == '__main__':
    app.run()


