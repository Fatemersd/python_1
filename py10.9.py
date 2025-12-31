import random
print(" in the name of God ")

for i in range(3):
    username = input("Enter username : ")
    password = input("Enter password : ")
    print ("~"*25)
    if username == "rashidi" and password == "*11":
        break
    elif i == 2:
        print("access denied !!!!!!!")
        exit()
    else:
        print("The username or password is incorrect. Please try again.")
        print("!!"*10)

while True:
    print("option : \n 1_calculator \n 2_lottery \n 3_exit!!")
    option = input("please choose: ")
    if option == "1" or option == "calculator":
        num1 = float(input("enter number : "))
        num2 = float(input("enter number2 : "))
        print("Choose Operation: \n 1_+ 2_- 3_* 4_/ 5_** 6_// 7_% 8_Go back ")
        amalgar = input("enter operation: ")
        print("~" *25)

        if amalgar == "1" or amalgar ==  "+":
            print(f"{num1} + {num2} = {num1+num2}")
            print("~" * 25)
        elif amalgar == "2" or amalgar ==  "-":
            print(f"{num1} - {num2} = {num1-num2}")
            print("~" * 25)
        elif amalgar == "3" or amalgar ==  "*":
            print(f"{num1} * {num2} = {num1*num2}")
            print("~" * 25)
        elif amalgar == "4" or amalgar ==  "/":
            print(f"{num1} / {num2} = {num1/num2}")
            print("~" * 25)
        elif amalgar == "5" or amalgar ==  "**":
            print(f"{num1} ** {num2} = {num1**num2}")
            print("~" * 25)
        elif amalgar == "6" or amalgar ==  "//":
            print(f"{num1} // {num2} = {num1//num2}")
            print("~" * 25)
        elif amalgar == "7" or amalgar ==  "%":
            print(f"{num1} % {num2} = {num1%num2}")
            print("~" * 25)
        elif amalgar == "8" or amalgar ==  "Go back":
            print("~" * 25)
            continue

    elif option == "2" or option == "lottery":
        names = []
        i = 1
        print("exit \n start : start lottery \n delete : delete name of list \n list : show names list")
        while True:
            name = input(f"Enter  participant {i} name: ")
            print("~"*25)

            if name == "exit":
                exit()
            elif name == "start":
                break

            elif name == "delete":

                d_name = input("Enter the name you want to delete: ")

                try:

                    names.remove(d_name)

                    print(f" User {d_name} was deleted successfully.")
                    print("~" * 25)

                    i -= 1

                except:

                    print("User not exist")
                    print("~" * 25)

            elif name == "list":

                print(f"list: {names}")
                print("~" * 25)

            else:
                names.append(name)
                i +=1



        try:
            num_win =int(input("How many people should Win? "))
            random.shuffle(names)
            print(f"lottery Winners: ",random.sample(names , num_win))
            print("~" * 25)
        except:
            print("invalid selection")
            print("~" * 25)




    elif option == "3" or option == "exit":
        break

    else:
        print("input not found")
        print("~" * 25)
        continue
