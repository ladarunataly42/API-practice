import csv

class Actions:

    def __init__(self):
        self.data = None




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

