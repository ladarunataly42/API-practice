import csv

class Actions:

    def __init__(self):
        self.data = None

    def get_data():
        file = open('fci-breeds.csv', 'r')
        reader = csv.reader(file)
        json_list = []
        for row in reader:
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

