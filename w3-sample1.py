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

#11

# print(abs.__doc__)

#12

# import calendar

# print(calendar.month(2024, 10))

#13

# print('''a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example''')

#14

# from datetime import date

# f_Date=date(2014, 7, 2)
# l_date=date(2014, 7, 11)

# print(abs((f_Date-l_date).days))

#15

# r=6

# print((4.0/3.0)*(3.1415926535897931)*(r**3))


#16

# a=int(input("Enter The Number: "))

# if a>=17:
#     print((a-17)*2)
# else:
#     print(17-a)


#17
# def threetimes(k):
#     return k*3

# a=input("Enter 3 Items with spaces: ").split(" ")

# a= [int(a) for a in a]

# for i in a:
#     for j in range(0, len(a)):
#         if i==a[j]:
#             identical=True
#         else:
#             identical=False
#             break
        

# if identical==False:
#     print(sum(a))
# else:
#     b= list(map(threetimes, a))
#     print(sum(b))

#18

# n=int(input("Enter : "))
# print(True if abs(n-1000)<=100 or abs(n-2000)<=100 else False)