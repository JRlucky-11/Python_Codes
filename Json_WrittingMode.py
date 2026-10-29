import json

with open("Ex_Js_File.json", "w", encoding="utf-8") as file: # Open with Writting Mode.
    json.dump("Lucky", file, indent=4) # Dumping the data into the file with indentation of 4 spaces.