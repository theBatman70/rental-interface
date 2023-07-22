from file_handler import read_txt_file

def view():
    
    table = ""
    border = "-" * 100

    dictionary = read_txt_file()

    print("\nPlease take a look into our catalogue")
    print(border + "\nID \t Costume_Name \t\t\t Brand \t\t\t Price ($) \t Quantity" + "\n" + border)

    for key, value in dictionary.items():
        table = table + str(key) + " \t " + value[0] + " \t\t " + value[1] + " \t\t " + value[2] + " \t\t " + value[3]

    print(table)
    print(border)
