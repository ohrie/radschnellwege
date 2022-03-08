# This script is originally coming from https://milovantomasevic.com/blog/stackoverflow/2021-04-21-convert-csv-to-json-file-in-python/ and was adapted

import csv 
import json
import time

column_mapping = {
    "ID": "id",
    "Abk\u00fcrzung": "ref",
    "Titel": "name",
    "von": "from",
    "bis": "to",
    "(Kurzbeschreibung)": "description",
    "Projektstand": "status",
    "Kosten": "cost",
    "Fertigstellung": "finished",
    "Auftraggeber": "authority",
}

column_removals = [
    "", "ID_qgis", "Partnerkommune", "Projektwebsite", "Beteiligungsverfahren",
    "Wiki-Update", "Quellen", "Bundesland", "Kontakt", "Linestring",
    "Trassenf\u00fchrung", "Foto", "L\u00e4nge"
]

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in list(csvReader):
            rowCopy = row
            for key in list(row):
                if key in column_removals:
                    del rowCopy[key] 
                if key in column_mapping:
                    rowCopy[column_mapping[key]] = rowCopy.pop(key)
            jsonArray.append(rowCopy)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'../data/list_rsv.csv'
jsonFilePath = r'../data/rsv_data.json'

start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()

print(f"Conversion completed in {finish - start:0.4f} seconds")