username = input()
password = input()
if username == "admin" and password == "1234":
    print("What do you want ?")
    print ("1. PS4")
    print("2. switch")
    print("3. Xbox")
    select = int(input())
    if select==1:
        print("PS4 price is 100")
    elif select==2:
        print("switch price is 50")
    elif select==3:
        print("Xbox price is 110")
    else :
        print("Error")