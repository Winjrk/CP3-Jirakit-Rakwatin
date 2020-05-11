username = input()
password = input()
if username == "admin" and password == "1234":
    ps4 = 100
    switch = 50
    xbox = 110
    print("What do you want ?")
    print ("1. PS4 is 100")
    print("2. switch is 50")
    print("3. Xbox is 110")
    select = int(input())
    if select==1:
        many=int(input("how many?"))
        print("PS4 price is",many*ps4)
    elif select==2:
        many1=int(input("how many?"))
        print("switch price is",many1*switch)
    elif select==3:
        many2 =int(input("how many?"))
        print("Xbox price is",many2*xbox)
    else :
        print("Error")