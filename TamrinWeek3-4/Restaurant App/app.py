from routing import find_route
print()
print()
print()

print("""
            
            
            Programmer : Mohsen Marandy    |   git hub user: hiddenblood24
        """)

while True:
    print("""
            yeki az 2ta kar zir ra anjam bedeh:
                1. Admin-Restaurant ------------>  1  ro bezan
                2. User ------------------------>  2  ro bezan
        """)
    act = int(input("your selection: "))
    if act == 1:
        while True:
            print("""
                            yeki az 2ta kar zir ra anjam bedeh:
                                1. login-admin ------------>  1  ro bezan
                                2. register-admin --------->  2  ro bezan
                                3. exit()-admin ----------->  3  ro bezan
                        """)

            act = int(input("your selection: "))
            if act == 1:
                login_admin_func = find_route("login_admin")

                if login_admin_func:

                    name = input("name bezan: ")
                    uid = str(input("uid bezan: "))

                    login_admin_func(name, uid)
                else:
                    print("chenin routi nadarim")

            elif act ==2:
                register_admin_func = find_route("register_admin")

                if register_admin_func:

                    name = input("name bezan: ")
                    address = input("address bezan: ")
                    catagory = input('enter catagory restaurant: ')

                    print(register_admin_func(name,address,catagory))
                else:
                    print("chenin routi nadarim")

            elif act ==3:
                break




    elif act == 2:

        while True:
            print("""
                yeki az 2ta kar zir ra anjam bedeh:
                    1. login ------------>  1  ro bezan
                    2. register --------->  2  ro bezan
                    3. exit() ----------->  3  ro bezan
            """)
            act = int(input("your selection: "))
            if act == 1:
                login_func = find_route("login")

                if login_func:

                    email = input("emaileto bezan: ")
                    passw = input("passeto bezan: ")

                    login_func(email, passw)
                else:
                    print("chenin routi nadarim")
            elif act == 2:
                register_func = find_route("register")
                if register_func:
                    email = input("emaileto bezan: ")
                    print(register_func(email))
                else:
                    print("chenin routi nadarim")

            elif act == 3:
                break

            else:
                print("cheshato va kon. faghat 1 va 2")






    else:
        print('enter correct act[1 : Admin - 2: User ]')