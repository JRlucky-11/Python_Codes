try:
    with open("Ai_Names.csv", "r", encoding="utf-8") as file:
        for ln in file.readlines():
            print(ln.strip())
    
except FileNotFoundError:
    print("Sir Your File is not found.")
except EOFError:
    print("Sir Your file is empty.")
finally:
    if 'file' in locals():
        file.close()

