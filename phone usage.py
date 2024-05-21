# Lizzie Howe database assesment
# imports
import sqlite3

# constants and variables
DATABASE = "phone usage database.db"

# functions


def print_all():
    '''print all data'''
    db = sqlite3.connect("phone usage database.db")
    cursor = db.cursor()
    sql = "select * from phone usage database;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''

a      b      c
          ''')
    for phone in results:
        print(
            f"{phone[0]:10}"
            f"{phone[1]:10}"
            f"{phone[2]:10}"
        )
    # loop finished here
    db.close()

# main code


while True:
    user_input = input(
        """
    What would you like to do?
    1. Print all data
    9. Exit
"""
    )
    if user_input == "1":
        print_all()
    elif user_input == "9":
        break
    else:
        print("That is not an option\n")
