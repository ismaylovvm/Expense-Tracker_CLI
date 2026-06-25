import json
import os


DATA_FILE = "expens.json"



def get_database():

    if not os.path.exists(DATA_FILE):
        return []
    
    else:
        with open(DATA_FILE,"r","utf-8") as file:
            json.load(file)


def write_database(expenses):

    with open(DATA_FILE,"w","utf-8") as file:
        json.dump(expenses,file)




