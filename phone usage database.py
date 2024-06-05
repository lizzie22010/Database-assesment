# Lizzie Howe database assesment
# imports
import sqlite3

# constants and variables
DATABASE = "phone_usage.db"
current_user = None

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


def login():
    '''ask for username and/or create new user id'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    username_ask = input("Enter username: ")
    username_lower = username_ask.lower()
    user = cursor.execute(
                '''SELECT * FROM user
                    WHERE name = ?''',
                (username_lower,)).fetchone()
    print(user)
    if user is None:
        cursor.execute(
                '''INSERT INTO user (
             name) VALUES (?)''',
                (username_ask,))
        db.commit()
        current_user = (cursor.lastrowid)
        print(current_user)
        print('No existing user found; new user created successfully')
    else:
        current_user = user
    avg_screen_time = int(input("Enter your average screen time in minutes: "))
    cursor.execute(
        '''INSERT INTO entries (user_id
    usage) VALUES (?, ?)''',
        (current_user, avg_screen_time))

    # if # username exists
    #     # ask screen time
    #     # insert into entries table with user id
    #     # print "screen time _ has been added to user _"
    # if # username doesn't exist
    #     # create new user id with the name
    #     # print "no existing user found; new user created successfully"
    #     # ask screen time
    #     # insert into entries table with user id
    #     # print "screen time _ has been added to user _"

    db.commit()
    db.close()


def check_existing_user():
    '''check if user already exists'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    user_check = input("Do you already have a username? y/n ")
    if user_check == "n":
        name = input("Enter your name to create a new user: ")
        cursor.execute(
                '''INSERT INTO user (
             name) VALUES (?)''',
                (name,))
    elif user_check == "y":
        name = input("What is your username? ")
    else:
        print("That is not an option")

    db.commit()
    db.close()
    print('''
            username input''')


def take_user_input():
    '''add a user intput into the database'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    avg_screen_time = int(input("Enter your average screen time in minutes: "))
    cursor.execute(
        '''INSERT INTO entries (
        usage) VALUES (?,)''',
        (avg_screen_time))

    db.commit()
    db.close()
    print('''
            input accepted''')


def print_users():
    '''print all of the users with their user id'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    cursor.execute(
        '''SELECT * FROM user ''',)
    results = cursor.fetchall()
    print('''

ID   Username
          ''')
    for user in results:
        print(
            f"{user[0]:<5}"
            f"{user[1]:<20}"
        )  # unfinished
    db.commit()
    db.close()


# main code
while True:
    user_input = input(
        """
    What would you like to do?
    1. Print all data
    2. Print countries leaderboard
    3. Print users with user id
    4. Add an input
    9. Exit
"""
    )
    if user_input == "1":
        print_all()
    elif user_input == "2":
        print_all_countries()
    elif user_input == "3":
        print_users()
    elif user_input == "4":
        login()
    elif user_input == "9":
        break
    else:
        print("That is not an option\n")
