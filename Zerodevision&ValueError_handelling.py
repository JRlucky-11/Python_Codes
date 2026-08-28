print("="*60)
a = int(input("|> Enter a number: "))

while True:
    try:
        b = int(input("|> Enter another number: "))
        result = a / b
        break
    except ZeroDivisionError as ze:
        print("\t|>> Error: Cannot divide by Zero! Please try again.")
        print("\t|>> ", ze)
    except ValueError as ve:
        print("\t|>> Error: Invalid input! Please enter number only.")
        print("\t|>> ", ve)
    except Exception as e:
        print("\t|>> An unexpected error occurred.")
        print("\t|>> ", e)
    finally:
        print("\t|>> Division attempt finished.")

print("-" * 50)
print("|> Result: ", result)
print("=" * 60)