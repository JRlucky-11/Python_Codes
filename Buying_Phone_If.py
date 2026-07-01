print("\n\t__Welcome_to_My_Oppo_Store!__(Oppo Store)__")
print("============================================================")
name = input("\n|> Hello! What is your name?-> ")
print("|> Nice to meet you", name, ".")

print("\n|> Aap Kounsa Phone Kharidna Chahte Ho? (Which phone do you want to buy?)")

print("\n|> Our available Phone Models are: ")
print("|> 1. Oppo A16")
print("|> 2. Oppo A17")
print("|> 3. Oppo A18")
print("|> 4. Oppo A19")
print("|> 5. Oppo A20")
print("|> 6. Oppo A21")
print("|> 7. Oppo F21 Series")
print("|> 8. Oppo F23 Series")
print("|> 9. Oppo F27 Series")
print("|> 10. Oppo F29 Series")
print("|> 11. Oppo F33 Series")
print("|> 12. Oppo Reno 11 Series")
print("|> 13. Oppo Reno 12 Series")
print("|> 14. Oppo Reno 13 Series")
print("|> 15. Oppo Reno 14 Series")
print("|> 16. Oppo Reno 15 Series")
print("|> 17. Oppo Reno 16 Series")
print("|> 18. Oppo Find X7 Series")
print("|> 19. Oppo Find X8 Series")
print("|> 20. Oppo Find X9 Series")

print("\n|> Please enter the Phone Model Number: ")
choice = int(input("|-> "))

phone_name = ""
base_price = 0

if choice == 1:
    print("|>> You have selected Oppo A16.")
    phone_name = "Oppo A16"
    base_price = 12000
elif choice == 2:
    print("|>> You have selected Oppo A17.")
    phone_name = "Oppo A17"
    base_price = 14000
elif choice == 3:
    print("|>> You have selected Oppo A18.")
    phone_name = "Oppo A18"
    base_price = 15000
elif choice == 4:
    print("|>> You have selected Oppo A19.")
    phone_name = "Oppo A19"
    base_price = 16500
elif choice == 5:
    print("|>> You have selected Oppo A20.")
    phone_name = "Oppo A20"
    base_price = 18000
elif choice == 6:
    print("|>> You have selected Oppo A21.")
    phone_name = "Oppo A21"
    base_price = 19500
elif choice == 7:
    print("|>> You have selected Oppo F21 Series.")
    phone_name = "Oppo F21 Series"
    base_price = 22000
elif choice == 8:
    print("|>> You have selected Oppo F23 Series.")  
    phone_name = "Oppo F23 Series"
    base_price = 25000
elif choice == 9:
    print("|>> You have selected Oppo F27 Series.")
    phone_name = "Oppo F27 Series"
    base_price = 28000
elif choice == 10:
    print("|>> You have selected Oppo F29 Series.")
    phone_name = "Oppo F29 Series"
    base_price = 32000
elif choice == 11:
    print("|>> You have selected Oppo F33 Series.")
    phone_name = "Oppo F33 Series"
    base_price = 35000
elif choice == 12:
    print("|>> You have selected Oppo Reno 11 Series.")
    phone_name = "Oppo Reno 11 Series"
    base_price = 38000
elif choice == 13:
    print("|>> You have selected Oppo Reno 12 Series.")
    phone_name = "Oppo Reno 12 Series"
    base_price = 42000
elif choice == 14:
    print("|>> You have selected Oppo Reno 13 Series.")
    phone_name = "Oppo Reno 13 Series"
    base_price = 45000
elif choice == 15:
    print("|>> You have selected Oppo Reno 14 Series.")
    phone_name = "Oppo Reno 14 Series"
    base_price = 48000
elif choice == 16:
    print("|>> You have selected Oppo Reno 15 Series.")
    phone_name = "Oppo Reno 15 Series"
    base_price = 52000
elif choice == 17:
    print("|>> You have selected Oppo Reno 16 Series.")
    phone_name = "Oppo Reno 16 Series"
    base_price = 55000
elif choice == 18:
    print("|>> You have selected Oppo Find X7 Series.")
    phone_name = "Oppo Find X7 Series"
    base_price = 65000
elif choice == 19:
    print("|>> You have selected Oppo Find X8 Series.")
    phone_name = "Oppo Find X8 Series"
    base_price = 75000
elif choice == 20:
    print("|>> You have selected Oppo Find X9 Series.")
    phone_name = "Oppo Find X9 Series"
    base_price = 85000
else:
    print("|> Invalid choice. Please Run the Program Again & Select Correct Option.")

if choice >= 1 and choice <= 20:
    number = int(input("\n|> What is your Mobile Number: "))

    gst_amount = base_price * 0.18           # 18% GST calculation
    total_bill = base_price + gst_amount     # Final Amount

    print("\n=============================================")
    print("          $$$ OPPO STORE INVOICE $$$          ")
    print("=============================================")
    print(" Customer Name : ", name)
    print(" Phone Number  : ", number)
    print("---------------------------------------------")
    print(" Item Selected : ", phone_name)
    print(" Base Price    :  Rs.", base_price)
    print(" GST (18%)     :  Rs.", gst_amount)
    print("---------------------------------------------")
    print(" TOTAL AMOUNT  :  Rs.", total_bill)
    print("=============================================")

    print("\nThank You for Buying Phone from Our Store. Visit Again!\n")