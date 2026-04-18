
import random
from datetime import datetime

#this is the date and time

now = datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%I:%M %p")

# this is the bill no.

bill_no = (f"BILL-{random.randint(1000, 9999)}")


items = []       # this is the final list in which the items will be stored.

def add_item() :  
    item_name = input("Enter the item name : ")
    item_quantity = int(input(f"Enter the quantity of {item_name} here : "))
    item_price = int(input("Enter the item price : "))
    total = item_price * item_quantity
    
    item = [item_name, item_quantity, item_price, total]
    
    items.append(item)

def view_bill() :
    
    subtotal = 0
    
    print("\n--------------CURRENT BILL--------------")
    print("Item      Quantity      Price      Total")
    print("----------------------------------------")
    
    for i in range (len(items)) :
        
        item_name = items[i][0]
        item_quantity = items[i][1]
        item_price = items[i][2]
        total = items[i][3]
        subtotal = subtotal + total
        
        print(f"{item_name : <10}      {item_quantity : <5}      {item_price : <5}      {total : < 5}")

    print("----------------------------------------")
    
    print(f"Subtotal : {subtotal}")
  
    
def final_bill() : 
    
    print("===============FINAL BILL===============\n")
    
    print(f"Customer's name : {customer_name}")
    print(f"Bill No. : {bill_no}")
    print(f"Date : {date}")
    print(f"Time : {time}")
    
    print("------------------------------------------")
    print("Item      Quantity      Price      Total")
    print("------------------------------------------")
    
    subtotal = 0
  
    
    for i in range(len(items)) : 
        
        item_name = items[i][0]
        item_quantity = items[i][1]
        item_price = items[i][2]
        total = items[i][3]
        subtotal = subtotal + total
        
        print(f"{item_name : <10}      {item_quantity : <5}      {item_price : <5}      {total : < 5}")

    print("------------------------------------------")
    print(f"Subtotal : {subtotal}")
    
    gst = subtotal * (5/100)
    discount = subtotal * 6/100
    final_amount = subtotal + gst - discount
    
    print(f"GST (5%) : {gst}")
    print(f"Discount (6%) : {discount}")
    print(f"Final total : {final_amount}")


print("\n------------WELCOME TO OUR SHOP------------\n")

customer_name = input("Enter the customer's name : ")

while True : 
    print("\n----------MENU----------\n")
    
    print("1. Add Item")
    print("2. View Current Bill")
    print("3. Generate Final Bill")
    print("4. Exit")
   
    choice = int(input("Enter your choice here : "))
    
    if choice == 1 : 
        while True : 
            print("1. Add Item")
            print("2. Back")
            
            add_choice = int(input("Enter your choice here : "))

            if add_choice == 1 :
                add_item()
                
                print("\nYour item added sucessfully!\n") 
                
            elif add_choice == 2 : 
                break


    elif choice == 2 : 
        if items == [] : 
            print("\nNo items added yet!")

        else : 
            view_bill()

    elif choice == 3 : 
        if items == [] : 
            print("\nNo items added yet!")

        else : 
            final_bill()
            break
    
    elif choice == 4 : 
        print("Exiting program...")
        break        
