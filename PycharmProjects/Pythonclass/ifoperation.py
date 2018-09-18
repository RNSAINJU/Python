a=(int)(input("Enter your favourite number:"))
print(a)
if (a<=3 and a>=0):
    if a==3:
        print("Your number is 3")
    elif a==2:
        print("Your number is 2")
    elif a==1:
        print("Your number is 1")
    else:
        print("YOur number is 0")
elif (a<=7 and a>=0):
    print("Your number is less than or equal to 7")
elif (a<=9 and a>=0):
    print("Your number is less than or equal to 9")
else:
    print("Unexpected input")