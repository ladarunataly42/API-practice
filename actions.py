import csv
import json
from pprint import pprint

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
                'name': array[1],
                'section': array[2],
                'provisional':array[3],
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

    def get_request(processor,key,value):
        a = Actions.columns('id')
        k=len(processor)
        i=0
        if i <= k:
             for j in a:
                str1 = ''.join(str(j))
                if value[0]==str1:
                    print(processor[i][str1][key])
                    processor[i][str1][key]=value[1]
                    print(processor[i][str1][key])
                i = i + 1
        return('Succes')


    def add_row(processor,key,value):

        a = Actions.columns('id')
        k=len(processor)
        tl = (a[-1])+1
        str1 = ''.join(str(tl))
        list1=['','name','section','provisional','country','url','image','pdf']
        list=[str1,'name','section','provisional','country','url','image','pdf']
        q=0
        for i in key:
            for j in list:
                if j==i:
                    index=list.index(j)
                    list[index]=value[q]
                    q=q+1
        for i in list:
            for j in list1:
                if i == j:
                    index=list.index(j)
                    list[index]=' '
        obj = Actions.create_json_obj(list)


        z = 0
        if z <= k:
            for w in a:
                if w == tl-1:

                    processor[z][str1]=obj[str1]

                z = z + 1
        return processor

    def modify_row(processor, key, value):
        a = Actions.columns('id')
        k = len(processor)
        # str1 = ''.join(str(tl))
        list1 = ['', '', '', '', '', '', '', '']
        list = ['id', 'name', 'section', 'provisional', 'country', 'url', 'image', 'pdf']
        q = 0
        for i in key:
            for j in list:
                if j == i:
                    index = list.index(j)
                    list[index] = value[q]
                    q = q + 1
        for i in list:
            for j in list1:
                if i == j:
                    return ("ERROR!!", 400)
        obj = Actions.create_json_obj(list)

        z = 0
        if z <= k:
            for w in a:
                str1 = ''.join(str(w))
                if str1 == value[0]:
                    processor[z][str1] = obj[str1]

                z = z + 1
        return processor

    def delete_id(key,value):
        print(key,value)

