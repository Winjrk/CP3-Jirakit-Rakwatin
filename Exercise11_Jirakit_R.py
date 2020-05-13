n=int(input("Input Number : "))
for i in range(n):
    for x in range(2*n-1):
        if x < n - i - 1  :
            print(" ", end="")
        elif x > n+i-1 :
            print(" ", end="")
        else:
            print("x",end="")


    print()








