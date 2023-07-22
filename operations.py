from constants import place_border, border
from datetime import datetime
from file_handler import write_invoice_txt, read_invoice

def create_bill(name):
    bill = [] # Declare a list named bill
    bill_title = "Items rented by: " + name + " on " + str(datetime.now()) + "\n" 
    bill.append("\n " + border + "\n")
    bill.append(bill_title)
    bill.append(border + "\n\n")
    return bill

def ask_option():
    
    from return_ import return_
    from rent import rent
    from view import view

    # present the options to the user
    print(
        "\nWhat would you like to do :\n1. View Costumes Available \t (V) \n2. Rent a Costume \t\t (R) \n3. Return a "
        "Costume \t\t (B) \n4. Exit \t\t\t (X)")

    # input for the option
    try:
        choice = input("\nEnter your desired option : ")
    except:
        print("Please Enter a Valid Option.")
        ask_option()

    # when user chooses 1
    if choice == "1" or choice.lower() == "v":
        view()
        ask_option()

    # when user chooses 2
    elif choice == "2" or choice.lower() == "r":
        name = ask_name()
        price_list = []
        bill = create_bill(name)
        rent(name, bill, price_list)
        ask_option()

    # when user chooses 3
    elif choice == "3" or choice.lower() == "b":
        try: 
            name = ask_name()
            # check if given username's rent bill is there or not
            date = read_invoice(name) 
        except:
            print("User not found")
            ask_option()
        product_list = []
        return_(name, product_list)
        ask_option()

    # when user chooses 4
    elif choice == "4" or choice.lower() == "x":
        print("\n\t\tThank you for using the application\n")
        quit()
        # then the program ends

    # when user enters any other number except 1, 2 or 3
    else:
        place_border()
        print("\tInvalid input!!\nPlease select the values as per the provided options")
        place_border()
        ask_option()
        

def greet():
    # greetings
    place_border()
    print("\t\tWelcome to our Costume Rental Service")
    place_border()


def ask_name():
    customer_name = input("\nPlease enter your name, sir: ")
    return customer_name
