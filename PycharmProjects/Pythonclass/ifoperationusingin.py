a=(int)(input("Enter your favourite number:"))
print(a)
if (a in range (0,4)):
    if a==3:
        print("Your number is 3")
    elif a==2:
        print("Your number is 2")
    elif a==1:
        print("Your number is 1")
    else:
        print("YOur number is 0")
elif (a in range (4,8)):
    print("Your number is less than or equal to 7")
elif (a in range (8,10)):
    print("Your number is less than or equal to 9")
else:
    print("Unexpected input")

#This is a comment
