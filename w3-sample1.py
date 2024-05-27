# 1

# print ("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\n\sTwinkl0e, twinkle, little star,\n\tHow I wonder what you are")

# 2

# import sys
# print(sys.version)

# 3

# import datetime as dt

# print("Current Data and Time : \n" + dt.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))

#4
# import math
# r = 1.1
# print(math.pi*pow(r, 2))

#5

# fname= input("Enter Fname: ")
# lname= input("Enter lname: ")

# print(lname+ " " + fname)

#6

# a= input("Enter Comma Separated Word: ").split(",")

# print(a)
# print(tuple(a))

#7

# a= input("Enter File Name: ")
# print(a.split(".")[-1])

#8

# a=input("Enter Space Separeted Colour: ").split(" ")
# print("First Element: "+a[0]+"\n"+"Last Element: " + a[-1])

#9

# a=(11, 12, 2014)
# print("Exam Date is : %i / %i / %i " % a )

#10

# a=int(input("Enter n: "))
# b= ("%i + %i%i + %i%i%i" % (a,a,a,a,a,a)).split("+")
# print(sum(int(ele) for ele in b))