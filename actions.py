import csv
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
        json_Data=Actions.get_data()
        json_list=[]
        name=Actions.columns('name')
        column=Actions.columns(column_name)
        for col in json_Data:
            for i in range(len(name)):
                new_json = {
                    i+1: {
                        'name': name[i],
                        column_name: column[i]
                    }
                }
                json_list.append(new_json)
        return json_list

    def columns(y):
        file = open('fci-breeds.csv')
        df = pd.read_csv(file)
        rows=df.apply(lambda x: x.tolist())
        name=rows[y].tolist()
        return name

    def get_request(processor,key,value):
        column_id= Actions.columns('id')
        length=len(processor)
        i=0
        if i <= length:
             for j in column_id:
                str1 = ''.join(str(j))
                if value[0]==str1:
                    print(processor[i][str1][key])
                    processor[i][str1][key]=value[1]
                    print(processor[i][str1][key])
                i = i + 1
        return('Succes')


    def add_row(processor,key,value):

        column_id = Actions.columns('id')
        length=len(processor)
        new_index = (column_id[-1])+1
        str1 = ''.join(str(new_index))
        list1=['','name','section','provisional','country','url','image','pdf']
        main_list=[str1,'name','section','provisional','country','url','image','pdf']
        q=0
        for i in key:
            for j in main_list:
                if j==i:
                    index=main_list.index(j)
                    main_list[index]=value[q]
                    q=q+1
        for i in main_list:
            for j in list1:
                if i == j:
                    index=main_list.index(j)
                    main_list[index]=' '
        obj = Actions.create_json_obj(main_list)


        itter = 0
        if itter <= length:
            for w in  column_id:
                if w == new_index-1:
                    processor[itter][str1]=obj[str1]

                itter = itter + 1
        return processor

    def modify_row(processor, key, value):
        column_id = Actions.columns('id')
        length = len(processor)
        # str1 = ''.join(str(tl))
        list1 = ['', '', '', '', '', '', '', '']
        main_list= ['id', 'name', 'section', 'provisional', 'country', 'url', 'image', 'pdf']
        itter = 0
        for i in key:
            for j in main_list:
                if j == i:
                    index = main_list.index(j)
                    main_list[index] = value[itter]
                    itter = itter + 1
        for i in main_list:
            for j in list1:
                if i == j:
                    return ("ERROR!!", 400)
        obj = Actions.create_json_obj(main_list)

        itter2 = 0
        if itter2 <=length:
            for w in column_id:
                str1 = ''.join(str(w))
                if str1 == value[0]:
                    processor[itter2][str1] = obj[str1]

                itter2 = itter2 + 1
        return processor

    def delete_id(processor,value):
        id_columns = Actions.columns('id')

        if type(value[0]) is str:
            for i in id_columns:
                str_id = ''.join(str(i))
                if value[0] == str_id:
                    del processor[int(value[0])-1]
                    return 'SUCCES'

                elif value[0] not in processor[int(value[0])-1]:
                    return 'NOT IN'



        elif type(value[0]) is list:

            index=0
            for i in id_columns:
                str_id = ''.join(str(i))
                index=0

                if value[0][index] == str_id:
                    del processor[int(value[0][index])-1]
                    index=index+1
                    del processor[int(value[0][index])-2]
                if value[0][index] == str_id:

                    # del processor[int(value[0][index])-1]
                    # print(processor[int(value[0][index])-1])
                    if(index == len(value[0])-1):
                        break
                    else:
                        index=index+1



            return 'SUCCES'



