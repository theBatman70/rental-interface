from datetime import datetime, date
from file_handler import read_invoice, read_txt_file, write_invoice_txt, update_data
from view import view
from constants import border

def return_(customer_name, product_list):
    print("\nLets return a costume")
    dictionary = read_txt_file()
    view()

    try:
        a = int(input("\nEnter the ID of the costume you want to return: "))
    except:
        print("Please Enter a Valid ID.")
        return_(customer_name, product_list)

    if a < 1 or a > len(dictionary):
        print("Error: Given ID doesn't exist")
        return_(customer_name, product_list)  # again asks the user for option  

    try:
        quantity_by_user = int(input("\nHow many of them would you like to return? "))
    except:
        print("Please enter a number, not characters!")
        return_(customer_name, product_list)   

    # get the quantity from the stock
    quantity = int(dictionary[a][3])
    
    quantity_update = quantity + quantity_by_user
    dictionary[a][3] = str(quantity_update) + "\n"  # update quantity in dictionary

    update_data(dictionary)

    # get the product name and brand from the ID
    product = dictionary[a][0]
    brand = dictionary[a][1]
    
    # get the return date and rent date    
    return_date = date.today()
    rent_date = read_invoice(customer_name)
    
    charge_amount_per_day = 2 # late charge amount

    # calculate after how many days the costume is returned
    delta = return_date - rent_date # difference of date in delta object
    days = delta.days # getting the value in days

    if days > 5:
        print("\nReturned after " + str(delta.days) + " days")
        late_days = days - 5
        late_fee = late_days * charge_amount_per_day
    else:
        late_fee = 0

    product_list.append(brand + " " + product)

    again = input("\nDo you want to rent another costume as well?\n If yes enter 'y' else provide any other value: ")
            
    if again == "y":
        return_(customer_name, product_list)
                        
    else:
        products = ", ".join(product_list)
        invoice = f'\n{border}\nName of the Customer: {customer_name} \nProduct(s): {products} \nDate and time of return: {datetime.now()} \nLate fine: {late_fee} $ \n{border}'
        print(invoice)
        name = customer_name + " Return"
        write_invoice_txt(invoice, name)
