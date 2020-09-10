i = int(input("Please enter 1 or 0:\n"))
if i==1 or i==0:
    for i in [0,1] :
        if i==0 :
            a = int(input("Please enter a number:\n"))
            while a>=1 :
                print(a * "*",end="\n")
                a = a - 1
                continue
            break
        else :
            b = 1
            n = int(input("\nPlease enter a number:\n"))
            while b<=n :
                print(b * "*",end="\n")
                b = b + 1
                continue
            break
else :
    print("Please enter a correct number")






