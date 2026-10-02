try:
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write("> Hello sir, I am Friday. \n")
        file.write("> I can help you in your Weapon System.\n")
        file.write("> Hello sir, I am EDITH.\n")
        file.write("> I can help you in security systems.\n")

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
