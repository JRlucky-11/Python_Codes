import json

with open("Ex_Js_File.json", "r", encoding="utf-8") as file: # File opem with Reading Mode.
    data = json.load(file)
print(data) # It prints the whole data in the json file.
print(data["Age"]) # It prints the value of the key "Age" in the json file.