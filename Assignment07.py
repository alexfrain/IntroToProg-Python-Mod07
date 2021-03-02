# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Exception Handling and Pickling (Weekly spending)
# ChangeLog (Who,When,What):
# Alex Frain,2.27.2021,Created Script
# ---------------------------------------------------------------------------- #

import pickle

# Data---------
file_name_str = 'WeeklyTotal.dat'
purchase_dic = {}
weekly_purchase = []
stored_list = []
item_str = ''
cost_flt = 0
total_flt = 0
choice = ''

# Main -----
# Demonstration of Exception Handling
while True:

    try:
        item_str = input("Enter item purchased this week: ")
        if item_str.isnumeric():
            raise Exception("You entered a number instead of an item.\n")
        elif item_str == '':
            print("You didn't enter an item.")
            continue
        cost_flt = float(input("Enter cost of item: $"))

    except ValueError as e:
        print("You didn't enter a number for cost")
        print("Error: ", e, type(e), e.__doc__,"\n")
    except Exception as e:
        print("Error: ", e, type(e), e.__doc__,"\n")

    else:
        purchase_dic = {"Item": item_str, "Cost": cost_flt}
        weekly_purchase.append(purchase_dic)
        print(weekly_purchase)
        total_flt += cost_flt

        choice = input("Press 'Q' to quit or any other key to continue: ")
        print()
        if choice.lower() == 'q':
            break

print(f"You're final spend total for the week is $", total_flt)
stored_list = [weekly_purchase, total_flt]

# Pickle Time - save data to file
print("Pickling the data\n")
file_obj = open(file_name_str, 'wb')
pickle.dump(stored_list, file_obj)
file_obj.close()
print("Pickling complete\n")

# Unpickle - read data from file
print("Unpickling the file\n")
file_obj = open(file_name_str, 'rb')
data = pickle.load(file_obj)
file_obj.close()
print("Unpickling complete.\nThis is the data from the file:", data)
