import csv
import json
import pandas as pd

class Actions:

    def __init__(self):
        self.data = None

    def get_data():
        file = open('fci-breeds.csv', 'r')
        reader = csv.reader(file)
        json_list = []
        first = True

        for row in reader:
            if first:
                pass
                first=False
            else:
                json_obj = Actions.create_json_obj(row)
                json_list.append(json_obj)
        return json_list


    def create_json_obj(array):
        return {
            array[0]:{
                'id': array[1],
                'name': array[2],
                'provisional': array[3],
                'country': array[4],
                'url': array[5],
                'image': array[6],
                'pdf': array[7]
            }
        }



    def give_data(column_name):
        jsonData=Actions.get_data()
        jsonlist=[]
        name=Actions.columns('name')
        column=Actions.columns(column_name)
        for col in jsonData:
            for i in range(len(name)):
                new_json = {
                    i+1: {
                        'name': name[i],
                        column_name: column[i]
                    }
                }
                jsonlist.append(new_json)
        return jsonlist

    def columns(y):
        file = open('fci-breeds.csv')
        df = pd.read_csv(file)
        rows=df.apply(lambda x: x.tolist())
        name=rows[y].tolist()
        return name

    def get_request(column_name):
        json=Actions.get_data()














