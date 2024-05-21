# Lizzie Howe database assesment
# imports
import sqlite3

# constants and variables
DATABASE = "phone_usage.db"

# functions


def print_all():
    '''print all data'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    sql = "select * from phone_usage_table;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''

#    Country             Avg screen time
          ''')
    for phone in results:
        print(
            f"{phone[0]:<5}"
            f"{phone[1]:<20}"
            f"{phone[2]:<10}"
        )
    # loop finished here
    db.close()


def print_all_countries():
    '''print all country data'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    sql = "select * from phone_usage_table;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''

#    Country             Avg screen time
          ''')
    for phone in results:
        print(
            f"{phone[0]:<5}"
            f"{phone[1]:<20}"
            f"{phone[2]:<10}"
        )
    # loop finished here
    db.close()


def take_user_input():
    '''add a user intput into the database'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS phone_usage
                    (
                    country TEXT
                    Average screen time INTEGER
                )''')

    country = input("enter your name:")
    avg_screen_time = int(input("enter your average screen time:"))
    cursor.execute(
        '''INSERT INTO phone_usage (country,
        avg_screen_time) VALUES (?, ?)''',
        (country, avg_screen_time))

    db.commit()
    db.close()
    print('''
            input accepted''')


# main code


while True:
    user_input = input(
        """
    What would you like to do?
    1. Print all data
    2. Print countries leaderboard
    3. Add a user input
    9. Exit
"""
    )
    if user_input == "1":
        print_all()
    elif user_input == "2":
        print_all_countries()
    elif user_input == "3":
        take_user_input()
    elif user_input == "9":
        break
    else:
        print("That is not an option\n")
