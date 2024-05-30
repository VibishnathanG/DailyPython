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

#19

# s=input("Enter your string: ")

# if s[0:2].upper()=="IS":
#     print(s)
# else:
#     print("is "+s)


#20

# a=input("Enter the String: ")
# n=int(input("Enter Times: "))


# print(a*n)

#21

# import random

# c=["Shit again", "Yep", "Yaar again "]

# def odd_or_even(n):
#     try:
#         if n%2 == 0:
#             return f"{random.choice(c)} the Number is Even"
#         elif n <0:
#             raise ValueError("The enter value is Negative")
#         else:
#             return "Entered Number is Odd"

#     except ValueError as error:
#         return error

# count=0
# while True:
#     count+=1
#     n=int(input("Enter The number: "))
#     if n==0:
#         print("Dont Enter Zero")
#     elif count==5:
#         break
#     else:
#         print(odd_or_even(n))


#22


# a=input("Enter the List items with spaces: ").split(" ")

# a=[int(a) for a in a]

# count = 0

# for i in a:
#     if i == 4:
#         count+=1
#     else:
#         continue

# print(count)


#23

# strg=input("Enter the String: ")
# n=int(input("Enter the Tines of Copy; "))

# if len(strg) <= 2:
#     print(strg*n)

# else:
#     print(strg[:2]*n)


# #24

# vowels=("a", "e", "i", "o", "u")
# s=input("Enter the Char: ")
# print("Yes Vowel") if s in vowels else print("Not Vowel")


#25

# test_Data=range(1,10)
# sample_Data=int(input("Enter The Test Number: "))
# print(True) if sample_Data in test_Data else print(False)