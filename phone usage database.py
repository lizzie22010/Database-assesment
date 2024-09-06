# Lizzie Howe database assesment
# imports
import sqlite3

# constants and variables
DATABASE = "phone_usage.db"
current_user = None
first_run = True

# functions


def print_all():
    '''print all data'''
    db = sqlite3.connect("phone_usage.db")  # add in entries to this function
    cursor = db.cursor()
    sql = "select * from phone_usage_table;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop through all the results
    print('''

#    Country             Avg screen time
          ''')
    for phone in results:
        duration = phone[2]
        hours = duration // 60
        minutes = duration % 60
        time = f"{hours} hrs   {minutes:<3} mins"
        print(
            f"{phone[0]:<5}"
            f"{phone[1]:<20}"
            f"{time}"
        )
    # loop finished here
    cursor.execute(
        '''SELECT entries.id, user.name, entries.usage FROM entries
    JOIN user ON entries.user_id = user.id ''',)
    results = cursor.fetchall()
    print('''

     Username       Screen time
        ''')
    for phone in results:
        duration = phone[2]
        hours = duration // 60
        minutes = duration % 60
        time = f"{hours} hrs   {minutes:<3} mins"
        print(
            f"{phone[0]:<5}"
            f"{phone[1]:<20}"
            f"{time}"

        )
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
        duration = phone[2]
        hours = duration // 60
        minutes = duration % 60
        time = f"{hours} hrs   {minutes:<3} mins"
        print(
            f"{phone[0]:<5}"
            f"{phone[1]:<20}"
            f"{time}"
        )
    # loop finished here
    db.close()


def login():
    '''ask for username and/or create new user id'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    
    while True:
        username_ask = input("\nEnter username: ")
        if username_ask == "":
            print("\nNo input entered. Please try again")
        if username_ask.isdigit():
            print("\nInput cannot be a number. Please try again.")
        else:
            username_lower = username_ask.lower()
            user = cursor.execute(
                '''SELECT * FROM user
                    WHERE name = ?''',
                (username_lower,)).fetchone()
            break
    if user is None:
        cursor.execute(
                '''INSERT INTO user (
             name) VALUES (?)''',
                (username_ask,))
        db.commit()
        current_user = (cursor.lastrowid)
        if user == "":
            print("Try again")
        print('\nNew account created\n')
    else:
        current_user = user[0]
        print('\nLogin successful\n')
    while True:
        try:
            avg_screen_time = int(input("Enter your screen time in minutes: "))
            cursor.execute(
                '''INSERT INTO entries (usage, user_id) VALUES (?, ?)''',
                (avg_screen_time, current_user))
            print('''
        Screen time  * {time} minutes *  has been added to user  * {user} *'''
                .format(time=avg_screen_time, user=username_ask))
            break
        except:
            print("\nThat is not an integer, please try again\n")



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


def check_existing_user():  # inactive
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


def average_user():
    '''Find the average screen time for a user'''
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    username_ask = input("\nEnter username: ")
    username_lower = username_ask.lower()
    user = cursor.execute(
                '''SELECT * FROM user
                    WHERE name = ?''',
                (username_lower,)).fetchone()
    user_id = user[0]
    if user_id is None:
        print('That username is not in my database.')
    else:

        cursor.execute(
            '''SELECT AVG(usage) FROM entries
    WHERE user_id = ?''',
            (user_id,))
        results = cursor.fetchone()
        results = results[0]
        hours = results // 60
        hours = int(round(hours, 2))
        minutes = results % 60
        minutes = int(round(minutes, 2))
        time = f"{hours} hrs   {minutes} mins" 
        print(time)
    db.commit()
    db.close()


def print_user_entries():  # working here 07/06
    db = sqlite3.connect("phone_usage.db")
    cursor = db.cursor()
    cursor.execute(
        '''SELECT entries.id, user.name, entries.usage FROM entries
    JOIN user ON entries.user_id = user.id ''',)
    results = cursor.fetchall()
    print('''

     Username       Screen time
        ''')
    for phone in results:
        duration = phone[2]
        hours = duration // 60
        minutes = duration % 60
        time = f"{hours} hrs   {minutes:<3} mins"
        print(
            f"{phone[0]:<5}"
            f"{phone[1]:<20}"
            f"{time}"

        )
    db.commit()
    db.close()


# main code
while True:
    if not first_run:
        user_input = input("\nPress ENTER to continue")
    else:
        user_input = ''
        first_run = False

    if user_input == '':
        user_input = input(
            """
What would you like to do?
1. Print all data
2. Print countries leaderboard
3. Print user entries
4. Print users
5. Add an input
6. Find user average
0. Exit
"""
        )
        if user_input == "1":
            print_all()
        elif user_input == "2":
            print_all_countries()
        elif user_input == "3":
            print_user_entries()
        elif user_input == "4":
            print_users()
        elif user_input == "5":
            login()
        elif user_input == "6":
            try: 
                average_user()
            except:
                print('That username is not in my database.')
        elif user_input == "0":
            break
        else:
            print("\nThat is not an option")
    else:
        print("Incorrect input")
