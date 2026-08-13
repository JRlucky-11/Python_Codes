def yourorder(name, *discount, **items):
    print("\n" + "=" * 40)
    print("-------------[ FINAL BILL ]-------------")
    print("\n" + "=" * 40)
    print("|> Customer Name: ", name)
    print("-" * 40)

    total_price = 0
    
    print("\tItems: ")
    for key, value in items.items():
        print(f"\t  - {key} : Rs.{value}")
        total_price += value
        
    print("-" * 40)
    print(f"\tSub Total     : Rs.{total_price}")

    total_discount = sum(discount)
    print("\tDiscount Applied: ")
    for d in discount:
        print(f"\t  - {d}% Off")
    
    discount_amount = (total_price * total_discount) / 100
    final_amount = total_price - discount_amount

    print("-" * 40)
    print(f"\tDiscount Amt  : -Rs.{discount_amount}")
    print(f"\tTotal Payable :  Rs.{final_amount}")
    print("="*40)

customer_name = input("|> Enter customer name: ")
discount = int(input("|> Enter discount % : "))

print("")
item_size = int(input("|> How many items you entered?-> "))

item_dict = {}
for i in range(item_size):
    item_name = input(f"\t|>> Enter {i+1} Item Name: ")
    item_price = int(input(f"\t\t>>> Enter {i+1} Item Price: "))
    item_dict[item_name] = item_price

yourorder(customer_name, discount, **item_dict)