# 1

# print ("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\n\sTwinkl0e, twinkle, little star,\n\tHow I wonder what you are")
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
# a= input("Enter Comma Separated Word: ").split(",")

# print(a)
# print(a)
# print(tuple(a))
# print(tuple(a))

#7

# a= input("Enter File Name: ")
# a= input("Enter File Name: ")
# print(a.split(".")[-1])
# print(a.split(".")[-1])

#8

# a=input("Enter Space Separeted Colour: ").split(" ")
# a=input("Enter Space Separeted Colour: ").split(" ")
# print("First Element: "+a[0]+"\n"+"Last Element: " + a[-1])
# print("First Element: "+a[0]+"\n"+"Last Element: " + a[-1])

#9

# a=(11, 12, 2014)
# a=(11, 12, 2014)
# print("Exam Date is : %i / %i / %i " % a )
# print("Exam Date is : %i / %i / %i " % a )

#10

# a=int(input("Enter n: "))
# a=int(input("Enter n: "))
# b= ("%i + %i%i + %i%i%i" % (a,a,a,a,a,a)).split("+")
# b= ("%i + %i%i + %i%i%i" % (a,a,a,a,a,a)).split("+")
# print(sum(int(ele) for ele in b))

#11

# print(abs.__doc__)

#12

# import calendar

# print(calendar.month(2024, 10))

#13

# print('''a string that you "don't" have to escape
# print('''a string that you "don't" have to escape
# This
# is a ....... multi-line
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
# a=int(input("Enter The Number: "))

# if a>=17:
# if a>=17:
#     print((a-17)*2)
#     print((a-17)*2)
# else:
#     print(17-a)
#     print(17-a)


#17
# def threetimes(k):
#     return k*3

# a=input("Enter 3 Items with spaces: ").split(" ")
# a=input("Enter 3 Items with spaces: ").split(" ")

# a= [int(a) for a in a]
# a= [int(a) for a in a]

# for i in a:
# for i in a:
#     for j in range(0, len(a)):
#     for j in range(0, len(a)):
#         if i==a[j]:
#             identical=True
#         else:
#             identical=False
#             break
        

# if identical==False:
#     print(sum(a))
#     print(sum(a))
# else:
#     b= list(map(threetimes, a))
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
# a=input("Enter the String: ")
# n=int(input("Enter Times: "))


# print(a*n)
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
# a=input("Enter the List items with spaces: ").split(" ")

# a=[int(a) for a in a]
# a=[int(a) for a in a]

# count = 0

# for i in a:
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
# vowels=("a", "e", "i", "o", "u")
# s=input("Enter the Char: ")
# print("Yes Vowel") if s in vowels else print("Not Vowel")


#25

# test_Data=range(1,10)
# sample_Data=int(input("Enter The Test Number: "))
# print(True) if sample_Data in test_Data else print(False)


#26

# char=input("Enter: ")
# Row_count=map(int, input("Enter the Row Count with space: ").split(" "))
# Row_count=list(Row_count)

# for i in Row_count:
#     print(char*i)


#27

# input_list=input("Enter the List: ").split(" ")

# string=""
# for i in input_list:
#     string+=i

# print(string)


#28

# numbers = [    
#     386, 462, 47, 237, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# for i in numbers:
#     if i != 237:
#         print(i) 
#     else: 
#         break 
        

#29

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print(color_list_1.difference(color_list_2))


#30


# def triangle(base: float = 0.0, height: float = 0.0) -> float:
#   if base < 0 or height < 0:
#       raise ValueError("Base and height must be non-negative values.")
#   return 0.5 * base * height


# while True:
#   try:
#     base = float(input("Enter the base of the triangle: "))
#     height = float(input("Enter the height of the triangle: "))
#     area = triangle(base, height)
#     if area is not None:
#       print(f"The area of the triangle is: {area:.2f}")
#   except ValueError as e:
#     print("Invalid input:", e)
#   except KeyboardInterrupt:
#     print("Exiting...")
#     break

#31


# import time

# # Start time
# start_time = time.time()

# # Input numbers
# a = int(input("Enter Number A: "))
# b = int(input("Enter Number B: "))

# # Find divisors of a
# divisor_of_a = []
# for i in range(2, a // 2 + 1):
#     if a % i == 0:
#         divisor_of_a.append(i)

# # Find divisors of b
# divisor_of_b = []
# for j in range(2, b // 2 + 1):
#     if b % j == 0:
#         divisor_of_b.append(j)

# # Find common divisors and get the maximum
# max_set = set(divisor_of_b).intersection(set(divisor_of_a))
# max_value = list(max_set).pop()

# # Print the result
# print(f"GCD: {max_value}")

# # End time
# end_time = time.time()

# # Print execution time
# print(f"Execution Time: {end_time - start_time} seconds")

#32

# Input numbers
# a = int(input("Enter Number A: "))
# b = int(input("Enter Number B: "))

# if a>b:
#     c=a
# else:
#     c=b

# while 1:
#     if (c%a==0) and (c%b==0):
#         lcm=c
#         break
#     else:
#         c+=1

# print(lcm)

#33

