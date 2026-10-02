try:
    with open("data.txt", "r", encoding="utf-8") as file:
        for ln in file:
            print(ln.strip())

except FileNotFoundError:
    print("Sir Your File is not found.")
except EOFError:
    print("Sir Your file is empty.")
finally:
    if 'file' in locals():
        file.close()