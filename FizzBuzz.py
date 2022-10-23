def fizz_buss(ans=0):
    ans = int(input("Write a number: \n"))
    if (ans % 3 == 0)&(ans % 5 !=0):
        print("fizz")
    elif (ans % 5 == 0)&(ans % 3 !=0):
        print("buzz")
    elif (ans % 3 == 0)&(ans % 5 ==0):
        print("fizz buzz")
    return print(ans)
fizz_buss()