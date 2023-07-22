from datetime import datetime
from view import view
from constants import place_border, border
from operations import ask_option
from file_handler import read_txt_file, update_data, write_invoice_txt


def rent(customer_name, bill, price_list):
    print("\nLets rent a costume")
    dictionary = read_txt_file()
    view()

    try:
        a = int(input("\nEnter the ID of the costume you want to rent: "))
    except:
        print("Please Enter a Valid ID.")
        rent(customer_name, bill, price_list)
    
    if a < 1 or a > len(dictionary):
        print("Error: Given ID doesn't exist")
        rent(customer_name, bill, price_list)  # again asks the user for option
        
    quantity = int(dictionary[a][3])

    if quantity == 0:
        place_border()
        print("Costume not available")
        place_border()
        rent(customer_name, bill, price_list)

    else:
        print("\nID is " + str(a))
        place_border()
        print("Costume renting available")
        place_border()

        try:
            quantity_by_user = int(input("\nHow many of them would you like to rent? "))
        except:
            print("Please enter a number, not characters!")
            rent(customer_name, bill, price_list)

        # get the price and product name from the ID
        price = float(dictionary[a][2].strip("$")) # get the price from dictionary, remove the $ sign and convert into float
        price = quantity_by_user * price
        product = dictionary[a][0]
        brand = dictionary[a][1]

        if quantity_by_user > quantity:
            print("\nWe don't have that many of the item, please check our stock and try again.")
            rent(customer_name, bill, price_list)

        else:
            quantity_update = quantity - quantity_by_user
            dictionary[a][3] = str(quantity_update) + "\n"  # update quantity in dictionary

            update_data(dictionary)

            print("Item successfully rented;")
            print("\nUpdated stocks:")
            view()

            print("The price of ", quantity_by_user, product, " is", price)

            bill.append(str(quantity_by_user))
            bill.append(brand)
            bill.append(product)
            bill.append("\t\t" + str(price) + "\n") # add the product details to the bill list

            price_list.append(price)
                
            again = input("\nDo you want to rent another costume as well?\n If yes enter 'y' else provide any other value: ")
            
            if again == "y":
                rent(customer_name, bill, price_list)
                        
            else:
                total_price = sum(price_list)
                bill.append("\n")        
                bill.append("The total price is:\t\t\t" + str(total_price) + "\n")
                bill.append(border + "\n")
                
                invoice = " ".join(bill)
                        
                print(invoice)

                write_invoice_txt(invoice, customer_name)


                

                

