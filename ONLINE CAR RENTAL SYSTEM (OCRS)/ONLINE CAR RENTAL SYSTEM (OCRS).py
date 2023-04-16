# MEMBER - 1
# MEMBER - 2


# create id
def get_next_id(id):
    file = open("id.txt", "r")
    nxtid = ""
    rec = file.readline().strip().split(":")
    ind = 0

    if id == "BOK":
        ind = 0
    elif id == "PAY":
        ind = 1
    nxtid = rec[ind]

    word = str(int(nxtid[3:]) + 1)
    if len(word) == 1:
        nxtid = id + "0000" + word
    elif len(word) == 2:
        nxtid = id + "0000" + word

    file.close()

    file = open("id.txt", "w")
    rec[ind] = nxtid
    file.write(":".join(rec))
    file.close()

    return nxtid


# user modify personal detail
def modify_personal_details(username):
    def select_data_to_modify():
        files = open("user_detail.txt", "r")
        print("Please select a information to modify:")
        print("1 - Username" + "\n" + "2 - Password" + "\n" + "3 - Telephone" + "\n")
        modify_choice = input("Choice:")
        if modify_choice == "1":
            new_user_name = input("Input new username:")
            modify_file = files.readlines()
            modify_file[line_number] = (
                    "{:<15} {:<15} {:<15} {:<5}".format(new_user_name, password, telephone, position) )
            files = open("user_detail.txt", "w")
            files.writelines(modify_file)
            files.close()
            print("Information successfully updated!")
            function_user(user_name)
        elif modify_choice == "2":
            check_password = input("Old password:")
            new_password = input("New password:")
            if check_password == password:
                modify_file = files.readlines()
                modify_file[line_number] = (
                        "{:<15} {:<15} {:<15} {:<5}".format(user_name, new_password, telephone, position))
                files = open("user_detail.txt", "w")
                files.writelines(modify_file)
                files.close()
                print("Information successfully updated!")
                function_user(user_name)
            else:
                print("Old password is invalid. Please retry!")
                select_data_to_modify()
        elif modify_choice == "3":
            new_telephone = input("Input new telephone:")
            modify_files = files.readlines()
            modify_files[line_number] = (
                    "{:<15} {:<15} {:<15} {:<5}".format(user_name, password, new_telephone, position) )
            files = open("user_detail.txt", "w")
            files.writelines(modify_files)
            files.close()
            print("Information successfully updated!")
            function_user(user_name)
        else:
            print("Invalid choice. Please retry!")
            select_data_to_modify()

    modify_personal_files = open("user_detail.txt", "r")
    admin_list = []
    for row in modify_personal_files:
        row = row.strip()
        line_list = row.split()
        admin_list.append(line_list)
    modify_personal_files.close()

    for number, row in enumerate(admin_list):
        if row[0] == username:
            user_name = row[0]
            password = row[1]
            telephone = row[2]
            position = row[3]
            line_number = number

    select_data_to_modify()


# user view payment history
def record_user_car_rental_history(username):
    file = open("payment.txt", "r")
    if username in file.read():
        x_file = open("payment.txt", "r")
        for line in x_file:
            if username in line:
                print("\nPayment history!!!")
                print(
                    "Payment ID    Book ID       Username      Bank          Account                   Pay      Date                 Time ")
                print(line)
        x_file.close()
    else:
        print("\nPlease do payment to view record!!!")
    file.close()

    file = open("booking.txt", "r")
    if username in file.read():
        x_file = open("booking.txt", "r")
        for line in x_file:
            if username in line:
                print("\nBooking history!!!")
                print(
                    "Book ID      Username     Car Plate       From Date       From Time       Until Date      Until Time      Day      Total Fee  ")
                print(line)
        x_file.close()
    else:
        print("\nPlease do booking to view record!!!")
    file.close()

    return function_user(username)


# user view available car
def user_car_available(username):
    # Open and read the car_detail.txt
    car_available_file = open("car_detail.txt", "r")
    content = car_available_file.readlines()
    car_available_file.close()

    # Display the record of car available for rent
    print("\n")
    print("{:<15} {:<15} {:<15} {:<10} {:<10}".format("Car Plate", "Brand", "Car Name", "Seat", "Color"))
    for line in content:
        if "Yes" in line:
            line = line.rstrip("\n")
            line = line.rstrip(" ")
            line = line.rstrip("Yes")
            print(line)

    function_user(username)


# user booking
def booking(username):
    # user booking car
    # store booking information
    def new_data(book_id, username, car_plate, f_date, f_time, u_date, u_time, day_r, total):
        file = open("booking.txt", "a")
        file.write("\n")
        file.write(
            "{:<12} {:<12} {:<15} {:<15} {:<15} {:<15} {:<15} {:<8} {:<8}".format(book_id, username, car_plate, f_date,
                                                                                  f_time, u_date, u_time, day_r, total))
        file.close()

    book_id = get_next_id("BOK")
    print("\nPlease remember your booking ID!!!")
    print("Your booking ID is:", book_id)

    # ensure car plate exist
    valid_car_plate = False
    while valid_car_plate == False:
        car_plate = input("\nEnter car plate:")

        z_file = open("car_detail.txt", "r")
        if car_plate in z_file.read():
            c_file = open("car_detail.txt", "r")
            for line in c_file:
                if car_plate in line:
                    if "Yes" in line:
                        valid_car_plate = True

                        x_file = open("car_detail.txt", "r")
                        content = x_file.readlines()
                        x_file.close()
                        line_number = ""
                        identify = ""
                        for number, line in enumerate(content):
                            if car_plate in line:
                                line_number = number
                                cnt = 0
                                while cnt < 65:
                                    search_str = content[number][cnt]
                                    identify = identify + search_str
                                    cnt = cnt + 1

                        w_file = open("car_detail.txt", "r")
                        modify = w_file.readlines()
                        modify[line_number] = ("{:<69} {:<10}".format(identify, "No") + "\n")
                        w_file = open("car_detail.txt", "w")
                        w_file.writelines(modify)
                        w_file.close()

                    elif "No" in line:
                        print("Car not avaliable !!!")
                        break
            c_file.close()

        else:
            print("Car not exist")
            valid_car_plate = False

        z_file.close()

    from datetime import datetime

    x = "\nInsert Date in format(DD/MM/YYYY)"
    y = "\nInsert Time in format(HH:MM)"

    # ensure date in specific format
    valid_f_date = False
    while valid_f_date == False:
        print(x)
        f_date = input("Enter date start rental car:")

        try:
            datetime.strptime(f_date, '%d/%m/%Y')
            valid_f_date = True

        except:
            print("\nDate format invalid !!!")

    # ensure date in specific format
    valid_u_date = False
    while valid_u_date == False:
        print(x)
        u_date = input("Enter date finish rental car:")

        try:
            datetime.strptime(u_date, '%d/%m/%Y')
            valid_u_date = True

        except:
            print("\nDate format invalid !!!")

    # ensure time in specific format
    valid_f_time = False
    while valid_f_time == False:
        print(y)
        f_time = input("Enter time start rental car:")

        try:
            datetime.strptime(f_time, '%H:%M')
            valid_f_time = True

        except:
            print("\nTime format invalid !!!")

    # ensure time in specific format
    valid_u_time = False
    while valid_u_time == False:
        print(y)
        u_time = input("Enter time finish rental car:")

        try:
            datetime.strptime(u_time, '%H:%M')
            valid_u_time = True

        except:
            print("\nTime format invalid !!!")

    # calculate day for car rent
    from_day = datetime.strptime(f_date, '%d/%m/%Y')
    until_day = datetime.strptime(u_date, '%d/%m/%Y')
    day = until_day - from_day
    day_r = day.days
    print("\nCar rent for ", day_r, " days")

    # calculate fee
    total = day_r * 10
    print("\nRental car fee = RM", total)

    print("\nBooking successful !!!")

    # collect information
    new_data(book_id, username, car_plate, f_date, f_time, u_date, u_time, day_r, total)

    return function_user(username)


# user payment
def payment(username):
    # store payment information
    def user_payment(pay_id, bid, username, bank, account, pay, date, time):
        x_file = open("payment.txt", "a")
        x_file.write("\n")
        x_file.write(
            "{:<13} {:<13} {:<13} {:<13} {:<25} {:<8} {:<20} {:<13}".format(pay_id, bid, username, bank, account, pay,
                                                                            date, time))
        x_file.close()

    bid = input("\nPlaese type your booking ID (BOK0000):")
    file = open("booking.txt", "r")
    if bid in file.read():
        w_file = open("booking.txt", "r")
        for line in w_file:
            if bid in line:
                print(
                    "\nBook ID      Username     Car Plate       From Date       From Time       Until Date      Until Time      Day      Total Fee")
                print(line)
        w_file.close()   
    else:
        print("\nBooking ID wrong or make a booking first!!!")
        return function_user(username)
    file.close()

    yes_no = input("\nThis is your booking record ???(Y/N):")
    if yes_no == "Y":
        pay_id = get_next_id("PAY")
        print("\nYour payment ID is:", pay_id)
    else:
        print("Please type the correct booking ID !!!")
        return function_user(username)

    # valid bank option
    valid_bank = False
    while valid_bank == False:
        print("\nA - CIMB Bank" + "\nB - Public Bank" + "\nC - RHB Bank\n")
        bank = input("Please select bank (A or B or C):")

        if bank == 'A':
            print("\nCIMB Bank")
            bank = "CIMB Bank"
            valid_bank = True

        elif bank == 'B':
            print("\nPublic Bank")
            bank = "Public Bank"
            valid_bank = True

        elif bank == 'C':
            print("\nRHB Bank")
            bank = "RHB Bank"
            valid_bank = True

        else:
            valid_bank = False

    # valid account
    valid_account = False
    while valid_account == False:
        account = input("\nPlease enter account number:")
        if len(account) > 18 or len(account) < 1:
            print("Account number too long or too short!!!")
            valid_account = False

        else:
            try:
                val = int(account)
                valid_account = True

            except:
                print("Please enter number only !!!")
                valid_account = False

    # valid pay
    valid_pay = False
    while valid_pay == False:
        pay = input("\nEnter fee to pay: RM ")

        try:
            val = int(pay)
            valid_pay = True

        except:
            print("Please enter number only !!!")
            valid_pay = False

    print("\nPayment success !!!")

    # show now date
    from datetime import datetime
    now = datetime.now()
    date = now.strftime("%d / %B / %Y")
    time = now.strftime("%H : %M : %S")

    print("\n", "Date: ", date, "\n\n", "Time: ", time)

    # collect information
    user_payment(pay_id, bid, username, bank, account, pay, date, time)

    return function_user(username)


# function user
def function_user(username):
    print("\nA - Modify personal detail")
    print("B - View personal booking and payment history")
    print("C - View detail car to be rented out")
    print("D - Book a car for specific duration")
    print("E - Do payment to confirm booking")
    print("F - Exit\n")
    user_function = input("Please enter (A or B or C or D or E or F):")

    if user_function == 'A':
        return modify_personal_details(username)

    elif user_function == 'B':
        return record_user_car_rental_history(username)

    elif user_function == 'C':
        return user_car_available(username)

    elif user_function == 'D':
        return booking(username)

    elif user_function == 'E':
        return payment(username)

    elif user_function == 'F':
        print("\nHave a nice day! Bye Bye.")

    else:
        return function_user(username)


# admin add car
def add_car():
    # Set a function to write into car_detail.txt and set format
    def add_car_details():
        add_car_file = open("car_detail.txt", "a")
        add_car_file.write(
            "{:<15} {:<15} {:<15} {:<10} {:<10} {:<10}".format(car_plate, brand, car_name, seat, color, ava))
        add_car_file.write("\n")
        add_car_file.close()

    # Let user input car plate
    print("Please enter car detail!")
    car_plate = input("Enter car plate:")
    car_plate = car_plate.rstrip(" ")
    # Check car plate duplicate or not
    files = open("car_detail.txt", "r")
    content = files.read()
    files.close()
    if car_plate not in content:
        # Continue input if car plate not duplicate
        brand = input("Enter brand:")
        car_name = input("Enter car name:")
        seat = input("Enter seat:")
        color = input("Enter color:")
        ava = input("Car available(Yes/No):")
        # Call add_car_details function
        add_car_details()
        print("New car successful added!")

    else:
        # Print if car plate duplicate
        print("Car plate duplicate!")

    function_admin()


# admin modify car detail
def modify_car_details():
    def search_exist():
        search = input("Enter a car plate to modify:")
        search = search.rstrip(" ")
        modify_files = open("car_detail.txt", "r")
        check_exist = modify_files.read()
        modify_files.close()
        if search != "":
            if search in check_exist:
                modify(search)
            else:
                print("Car plate not exist! Please retry!")
                search_exist()
        else:
            print("Please input a valid car plate!")
            search_exist()

    def modify(search):
        def select_to_modify():
            files = open("car_detail.txt", "r")
            print(
                "1 - Car Plate" + "\n" + "2 - Brand" + "\n" + "3 - Car Name" + "\n" + "4 - Seat" + "\n" + "5 - Color" + "\n")
            modify_choice = input("Please select a information to modify:")
            if modify_choice == "1":
                new_car_plate = input("Input new car plate:")
                modify_file = files.readlines()
                modify_file[line_number] = (
                        "{:<15} {:<15} {:<15} {:<10} {:<10} {:<10}".format(new_car_plate, brand, car_name, seat, color,
                                                                           ava) + "\n")
                files = open("car_detail.txt", "w")
                files.writelines(modify_file)
                files.close()
                print("Information successfully updated!")
                function_admin()

            elif modify_choice == "2":
                new_brand = input("Input new car brand:")
                modify_file = files.readlines()
                modify_file[line_number] = (
                        "{:<15} {:<15} {:<15} {:<10} {:<10} {:<10}".format(car_plate, new_brand, car_name, seat, color,
                                                                           ava) + "\n")
                files = open("car_detail.txt", "w")
                files.writelines(modify_file)
                files.close()
                print("Information successfully updated!")
                function_admin()

            elif modify_choice == "3":
                new_car_name = input("Input new car name:")
                modify_file = files.readlines()
                modify_file[line_number] = (
                        "{:<15} {:<15} {:<15} {:<10} {:<10} {:<10}".format(car_plate, brand, new_car_name, seat, color,
                                                                           ava) + "\n")
                files = open("car_detail.txt", "w")
                files.writelines(modify_file)
                files.close()
                print("Information successfully updated!")
                function_admin()

            elif modify_choice == "4":
                new_seat = input("Input new car seat:")
                modify_file = files.readlines()
                modify_file[line_number] = (
                        "{:<15} {:<15} {:<15} {:<10} {:<10} {:<10}".format(car_plate, brand, car_name, new_seat, color,
                                                                           ava) + "\n")
                files = open("car_detail.txt", "w")
                files.writelines(modify_file)
                files.close()
                print("Information successfully updated!")
                function_admin()

            elif modify_choice == "5":
                new_color = input("Input new car color:")
                modify_file = files.readlines()
                modify_file[line_number] = (
                        "{:<15} {:<15} {:<15} {:<10} {:<10} {:<10}".format(car_plate, brand, car_name, seat, new_color,
                                                                           ava) + "\n")
                files = open("car_detail.txt", "w")
                files.writelines(modify_file)
                files.close()
                print("Information successfully updated!")
                function_admin()

            else:
                select_to_modify()

        modify_car_files = open("car_detail.txt", "r")
        admin_list = []
        line_number = ""
        for row in modify_car_files:
            row = row.strip()
            line_list = row.split()
            admin_list.append(line_list)
        modify_car_files.close()

        for number, row in enumerate(admin_list):
            if row[0] == search:
                car_plate = row[0]
                brand = row[1]
                car_name = row[2]
                seat = row[3]
                color = row[4]
                ava = row[5]
                line_number = number
                select_to_modify()

    search_exist()


# Record - car rented out
def car_rented_out():
    # Open and read the car_detail.txt
    car_rented_out_file = open("car_detail.txt", "r")
    content = car_rented_out_file.readlines()
    car_rented_out_file.close()

    # Display the record of car rented out
    print("{:<15} {:<15} {:<15} {:<10} {:<10}".format("Car Plate", "Brand", "Car Name", "Seat", "Color"))
    for line in content:
        if "No" in line:
            line = line.rstrip("\n")
            line = line.rstrip(" ")
            line = line.rstrip("No")
            print(line)

    function_admin()


# Record - car available for rent
def car_available():
    # Open and read the car_detail.txt
    car_available_file = open("car_detail.txt", "r")
    content = car_available_file.readlines()
    car_available_file.close()

    # Display the record of car available for rent
    print("\n")
    print("{:<15} {:<15} {:<15} {:<10} {:<10}".format("Car Plate", "Brand", "Car Name", "Seat", "Color"))
    for line in content:
        if "Yes" in line:
            line = line.rstrip("\n")
            line = line.rstrip(" ")
            line = line.rstrip("Yes")
            print(line)

    function_admin()


# Record - all booking
def record_booking():
    # admin view all customer booking
    file = open("booking.txt", "r")
    all_booking = file.read()
    print("\n")
    print(all_booking)
    file.close()

    function_admin()


# Record (month) - customer payment
def record_payment_month():
    month = input("\nEnter month (June):")
    file = open("payment.txt", "r")
    if month in file.read():
        print("Month exist !!!")
        x_file = open("payment.txt", "r")
        for line in x_file:
            if month in line:
                print(
                    "\nPayment ID    Book ID       Username      Bank          Account                   Pay      Date                 Time ")
                print(line)
        x_file.close()

    else:
        print("No payment in this month!!!")
        record_payment_month()
    file.close()

    function_admin()


# Record (car plate) - customer booking
def record_booking_car_plate():
    # admin search specific record (car_plat)
    car_plate = input("\nEnter car plate:")
    file = open("booking.txt", "r")
    if car_plate in file.read():
        print("Car plate exist !!!")
        x_file = open("booking.txt", "r")
        for line in x_file:
            if car_plate in line:
                print(
                    "\nBook ID      Username     Car Plate       From Date       From Time       Until Date      Until Time      Day      Total Fee")
                print(line)
        x_file.close()

    else:
        print("Car plate not exist or car has not book by anyone !!!")
        record_booking_car_plate()
    file.close()

    function_admin()


# Record (bank) - customer payment
def record_payment_bank():
    # admin search specific bank (CIMB Bank / Public Bank / RHB Bank)
    bank = input("\nEnter bank name (CIMB Bank / Public Bank / RHB Bank):")
    file = open("payment.txt", "r")
    if bank in file.read():
        print("\nBank exist!!!")
        x_file = open("payment.txt", "r")
        for line in x_file:
            if bank in line:
                print(
                    "\nPayment ID    Book ID       Username      Bank          Account                   Pay      Date                 Time")
                print(line)
        x_file.close()

    else:
        print("Bank not exist!!!")
        record_payment_bank()
    file.close()

    function_admin()


# admin return rental car
def car_return():
    print("Input a car plate to returned!")
    search = input("Car plate:")
    car_return_file = open("car_detail.txt", "r")
    content = car_return_file.readlines()
    car_return_file.close()
    line_number = ""
    identify = ""
    for number, line in enumerate(content):
        if search in line:
            line_number = number
            cnt = 0
            while cnt < 65:
                search_str = content[number][cnt]
                identify = identify + search_str
                cnt = cnt + 1

    car_return_file = open("car_detail.txt", "r")
    modify = car_return_file.readlines()
    modify[line_number] = ("{:<69} {:<10}".format(identify, "Yes") + "\n")
    car_return_file = open("car_detail.txt", "w")
    car_return_file.writelines(modify)
    car_return_file.close()
    print("Car returned! Information updated successfully!")
    function_admin()


# admin register
def admin_register():
    admin_name = input("\nUsername:")
    admin_register_file = open("user_detail.txt", "r")
    register_check_content = admin_register_file.readlines()
    exist = ""
    for number, line in enumerate(register_check_content):
        if line != "":
            content1 = number
            cnt = 0
            search_exist = ""
            while cnt < 16:
                search_alp = register_check_content[content1][cnt]
                search_exist = search_exist + search_alp
                search_exist = search_exist.rstrip("\n")
                cnt = cnt + 1
            exist = exist + search_exist + "\n"

    if admin_name in exist:
        # Print if car plate duplicate
        print("Username duplicate!")
        admin_register()
    else:
        password = input("Password:")
        phone_number = input("Telephone:")
        admin_register_file = open("user_detail.txt", "r")
        register_check_content = admin_register_file.readlines()
        exist = ""
        for number, line in enumerate(register_check_content):
            if line != "":
                content1 = number
                cnt = 32
                search_exist = ""
                while cnt < 42:
                    search_alp = register_check_content[content1][cnt]
                    search_exist = search_exist + search_alp
                    search_exist = search_exist.rstrip("\n")
                    cnt = cnt + 1
                exist = exist + search_exist + "\n"

    admin_register_file.close()

    if phone_number in exist:
        print("Please choose another contact number !!!")
        admin_register()
    else:
        position = "Admin"
        admin_register_file = open("user_detail.txt", "a")
        admin_register_file.write("\n")
        admin_register_file.write("{:<15} {:<15} {:<15} {:<5}".format(admin_name, password, phone_number, position))
        admin_register_file.close()
        print("Admin successfully register!")

        function_admin()


# Function Admin
def function_admin():
    print("\nA - Add cars to be rented out")
    print("B - Modify car Detail")
    print("C - Record : Car rented out ")
    print("D - Record : Car available for rent")
    print("E - Record (all) : Customer booking")
    print("F - Specific Record (month) : Customer payment")
    print("G - Specific Record (car plate) : Customer booking")
    print("H - Specific Record (bank) : Customer payment")
    print("I - Return rental car")
    print("J - Register admin")
    print("K - Exit\n")
    admin_function = input("Please enter (A or B or C or D or E or F or G or H or I or J or K):")

    if admin_function == 'A':
        add_car()

    elif admin_function == 'B':
        modify_car_details()

    elif admin_function == 'C':
        car_rented_out()

    elif admin_function == 'D':
        car_available()

    elif admin_function == 'E':
        record_booking()

    elif admin_function == 'F':
        record_payment_month()

    elif admin_function == 'G':
        record_booking_car_plate()

    elif admin_function == 'H':
        record_payment_bank()

    elif admin_function == 'I':
        car_return()

    elif admin_function == 'J':
        admin_register()

    elif admin_function == 'K':
        print("\nHave a nice day! Bye Bye.")

    else:
        function_admin()


# determine admin or user
def choose_function(position, username):
    if position == "Admin":
        function_admin()
    else:
        return function_user(username)


# login
def login():
    print("Please login !!!")
    username = input("\nUsername:")
    password = input("Password:")
    login_file = open("user_detail.txt", "r")
    admin_list = []
    for row in login_file:
        row = row.strip()
        line_list = row.split()
        admin_list.append(line_list)
    login_file.close()

    cnt = 0
    ind = -1
    while cnt < len(admin_list):
        if username == admin_list[cnt][0] and password == admin_list[cnt][1]:
            ind = cnt
            break
        cnt = cnt + 1

    if ind >= 0:
        return choose_function(admin_list[cnt][3], username)
    else:
        print("Username or password is incorrect. Please retry!")
        lo_re()


# user register
def user_register_main():
    # Set a function to write into car_detail.txt and set format
    def user_register():
        files = open("user_detail.txt", "a")
        files.write("\n")
        files.write("{:<15} {:<15} {:<15} {:<5}".format(user_name, password, phone_number, position))
        files.close()

    print("Please register !!!")
    user_name = input("\nEnter username:")
    user_register_file = open("user_detail.txt", "r")
    register_check_content = user_register_file.readlines()
    exist = ""
    for number, line in enumerate(register_check_content):
        if line != "":
            content1 = number
            cnt = 0
            search_exist = ""
            while cnt < 16:
                search_alp = register_check_content[content1][cnt]
                search_exist = search_exist + search_alp
                search_exist = search_exist.rstrip("\n")
                cnt = cnt + 1
            exist = exist + search_exist + "\n"
    user_register_file.close()

    if user_name in exist:
        # Print if car plate duplicate
        print("Username duplicate!")
        user_register_main()
    else:
        # Continue input if car plate not duplicate
        password = input("Enter password:")

        phone_number = input("Enter contact number:")

        user_register_file = open("user_detail.txt", "r")
        register_check_content = user_register_file.readlines()
        exist = ""
        for number, line in enumerate(register_check_content):
            if line != "":
                content1 = number
                cnt = 32
                search_exist = ""
                while cnt < 42:
                    search_alp = register_check_content[content1][cnt]
                    search_exist = search_exist + search_alp
                    search_exist = search_exist.rstrip("\n")
                    cnt = cnt + 1
                exist = exist + search_exist + "\n"

            user_register_file.close()

        if phone_number in exist:
            print("Please choose another contact number !!!")
            user_register_main()

        position = "User"

        # Call add_car_details function
        user_register()
        print("Register successful!")
        function_user(user_name)

    login()


# welcome
print("Welcome to Online Car Rental System!")
file = open("car_detail.txt", "r")
first = file.readline()
second = file.readline()
third = file.readline()
fourth = file.readline()

first = first.rstrip("\n" + " " + "Car Available")
second = second.rstrip("\n" + " " + "Yes" + "No")
third = third.rstrip("\n" + " " + "Yes" + "No")
fourth = fourth.rstrip("\n" + " " + "Yes" + "No")
file.close()

print(first + "\n" + second + "\n" + third + "\n" + fourth)


def lo_re():
    # login or register
    l_r = False
    while l_r == False:
        print(
            "\nLeave or More details please login or register:" + "\n" + "L - Login" + "\n" + "R - Register" + "\n" + "Q - Leave")
        Login_Register = input("Choice:")
        if Login_Register == "L" or Login_Register == "l":
            login()
            l_r = True
        elif Login_Register == "R" or Login_Register == "r":
            user_register_main()
            l_r = True
        elif Login_Register == "Q" or Login_Register == "q":
            print("\nHave a nice day! Bye Bye.")
            l_r = True
        else:
            print("Please retry!")
            l_r = False

lo_re()
