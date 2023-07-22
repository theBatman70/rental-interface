from datetime import datetime

def read_txt_file():
    dictionary = {}  # dictionary

    file = open("data.txt")
    file_lines = file.readlines()  # store each line separately in the list file_lines

    for line in file_lines:  # loop for each line
        [key, costume_name, brand, price, quantity] = line.split(", ")  # split the values in the line and store in the variables
        dictionary[int(key)] = [costume_name, brand, price, quantity]  # update the dictionary with a new row

    file.close()

    return dictionary


def read_invoice(customer_name):
    name = customer_name.lower()
    file = open(name + ".txt")
    file_lines = file.readlines()  # store each line separately in the list file_lines
    
    line_with_date = file_lines[2]
    line_with_date = line_with_date.split()
    date_str = line_with_date[5]
    rent_date = datetime.strptime(date_str, '%Y-%m-%d').date()

    file.close()
    return rent_date


def update_data(dictionary):
    # Editing the text file with updated dictionary
    file = open("data.txt", "w")
    for key, value in dictionary.items():
        file.write('%s, %s, %s, %s, %s' % (key, value[0], value[1], value[2], value[3]))  # string formatting
        
    file.close()


def write_invoice_txt(invoice, customer_name):
    name = customer_name.lower()
    file = open(name + ".txt", "w")
    file.write(invoice)
    file.close()
