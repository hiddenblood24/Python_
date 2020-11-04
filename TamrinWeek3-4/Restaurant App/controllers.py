from models import User, ConcreteFood1, ConcreteFood2, ConcreteFood3, Restaurant



users = []
restaurants = []





def register_admin(name,address,catagory):
    for restaurant in restaurants:
        if restaurant.name == name:
            print("dobare kalak !! boorooo ")
            return
    restaurant = Restaurant(name,address,catagory)
    restaurants.append(restaurant)
    return f"your pass: {restaurant.uid} savesh kon"


def authenticate_admin(name, uid):
    for restaurant in restaurants:
        if restaurant.name == name:

            if str(restaurant.uid) == str(uid):

                return True
    return False
def login_admin(name,uid):
    valid_user = authenticate_admin(name, uid)

    if valid_user:
        print("welcome!", name)


        while True:
            print("""
                          yeki az 3ta kar zir ra anjam bedeh:
                                4. add_food ------------------------->  4  ro bezan
                                5. show_menu & rate & category ------>  5  ro bezan
                                6. exit().while --------------------->  6  ro bezan
                                    """)
            act = int(input('your selection: '))
            if act == 4:
                for restaurant in restaurants:
                    if restaurant.name == name:
                        # add food
                        name_food = str(input("enter Food name: "))
                        count_food = int(input("enter Food count: "))
                        restaurant.add_food(food=name_food , count=count_food)





            elif act == 5:
                for restaurant in restaurants:
                    if restaurant.name ==name:
                        # show menu & rate
                        print('daily menu : ',restaurant.daily_menu)
                        print()
                        print('rate restaurant : ',restaurant.rate)
                        print()
                        print('Category: ',restaurant.catagory)

            elif act == 6:
                break



            else:
                print('Wrong number!! choose between [ 4 - 6 ]')






    return None




def register(email):
    for user in users:
        if user.email == email:
            print("bache zerang!! khodeti. ma hamchin useri darim. boro login kon")
            return
    user = User(email)
    users.append(user)
    return f"your pass: {user.passw} savesh kon"


def authenticate(email, passw):
    for user in users:
        if user.email == email:
            if str(user.passw) == str(passw):
                return user
    return False


def login(email, passw):
    valid_user = authenticate(email, passw)
    if valid_user:
        print("welcome!",email)


        while True:
            print("""
                            yeki az 6ta kar zir ra anjam bedeh:
                                3. edit_pass -------------->  3  ro bezan
                                4. edit_profile ----------->  4  ro bezan
                                5. show_profile ----------->  5  ro bezan
                                6. buy_food --------------->  6  ro bezan
                                7. rate_food -------------->  8  ro bezan
                                8. exit().while ----------->  9  ro bezan
                        """)



            act = int(input('your selection: '))

            if act == 3:
                for user in users:
                    if user.email == email:
                        newpassww = input('enter a new password : ')
                        user.edit_passw(passw, newpassww)
                        print('new password is : ', user.passw)

            elif act == 4:
                for user in users:
                    if user.email ==email:
                        name_user, address_user = str(input('enter name  , address : ')).split()

                        age_user = str(input('enter age : '))

                        user.edit_profile(name=name_user, address=address_user, age=age_user)

            elif act == 5:
                for user in users:
                    if user.email == email:
                        print('User : ', user.email)
                        print('Address : ', user.address)
                        print('Name : ', user.name)
                        print('Age : ', user.age)

            elif act == 6:
                for user in users:
                    if user.email == email:
                        name_food = str(input("enter name of food: "))
                        count_food = int(input("enter count of food: "))
                        name_category = str(input('enter catagory: '))
                        # name_res = str(input("enter name restaurant: "))
                        kharid(name_food1=name_food,count_food1=count_food,category=name_category)



            elif act == 7:
                for user in users:
                    if user.email == email:
                        name_res = input("enter name restaurant: ")
                        rate = int(input("rate the Restaurant: "))
                        name_category = input('enter catagory: ')
                        rate_restaurant(name_res,rate,name_category)




            elif act ==8:
                break



    print("yechizi ro eshteb zadi")
    return None


def kharid(name_food1,count_food1,category):
    for restaurant in restaurants:
        for i in range(len(restaurant.daily_menu)):

            if restaurant.daily_menu[i][0] == name_food1 and restaurant.catagory==category:
                restaurant.sell_food(name_food1,count_food1)
                print('nosh jan')
                break
    else:
        print('yaft nashod')




def rate_restaurant(name_restaurant,rate,category):
    for restaurant in restaurants:
        if restaurant.name == name_restaurant and restaurant.catagory == category:

            restaurant.rate = restaurant.rate + rate