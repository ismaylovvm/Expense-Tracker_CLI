import json
import os
import pandas as pd


DATA_FILE = "expens.json"



def get_database():

    if not os.path.exists(DATA_FILE):
        return []
    
    else:
        with open(DATA_FILE,"r",encoding="utf-8") as file:
            return json.load(file)


def write_database(expenses):

    with open(DATA_FILE,"w",encoding="utf-8") as file:
        json.dump(expenses,file,indent=5)


def json_to_csv(csv_file="expenses.csv"):

    if not os.path.exists(DATA_FILE):
        print("JSON dosyası bulunamadı.")
        return

    df = pd.read_json(DATA_FILE)
    df.to_csv(csv_file, index=False)

    print(f"{csv_file} başarıyla oluşturuldu.")



