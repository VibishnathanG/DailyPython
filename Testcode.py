a= range(11,19)
# b=[x for x in a if x<5]
# print(b)

# if 5 in a:
#     print("Yes ")

# b = {10, 12, 13,4,1,6,3,0,1}
# c = {10, 12, 13,4,1,6,3,0,90}

# d = c.difference(b)
# d.add(80)
# print(d)

# dict={ "std1" : ["vibish",23],
#       "std2" : ["nathan", 22] }

# print(dict["std1"][1])

# for x in dict.items():
#     print(x)

# print(len(dict))


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily["child1"]["name"])

# c = 2
# d = 330
# print("A") if c > d else print("B")


# def hello(*args):
#     for x in args:
#         print(f"Hello {x}")

# hello("vibish", "sam", "tick")

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


#Lambda

# from functools import reduce

# t = reduce(lambda x, y : x+y, a )
# print(t)

# s = list(filter(lambda z : z <5 , a))
# print(s)

# u = list(map(lambda v : v+100, a))
# print(u)

#Class , Inheritance and Encapsulation examples

# class school:
#     def __init__(self, count, type):
#         self.count = count
#         self.type = type

#     def teacher(self):
#         return f"The Teacher count is {self.count} and type is {self.type}"
    
#     def student(Self):
#         return f"The Student count is {Self.count} and type is {Self.type}"
    

# s1=school(25, "permanent")
# s2=school(100, "Flex")

# print(s1.teacher())
# print(s2.student())


# class district(school):
#     def __init__(self, d, count, type) -> str:
#         self.d = d
#         super().__init__(count, type) #school.__init__(self,count, type) --> This also can be used
    
#     def pdist(self):
#         return f"The district of the school is {self.d}"
    
#     def teacher(self):   #Ploymorphism
#         return f"This Teacher Function is overritten by district sorry !!! "
    

# d1=district("salem", 50, "permanent")
# print(d1.pdist())
# print(d1.teacher())


# for i, j in enumerate(a):
#     print(f"the index is {i} and Value is {j}")



# def twoSum(nums, target):
#         num_to_index = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_to_index:
#                 return [num_to_index[complement], i]
#             num_to_index[num] = i
#         return []  # Return empty list if no such pair is found


# print(twoSum([2,8,11,7], 9))



#Eception Handling

# b=20
# try:
#     c= int(input("Enter: "))
#     d=b/c

# except ValueError:
#     print("C must be int")

# except ZeroDivisionError:
#     print("C shouldnt be 0")

# else:
#     print(d)

# finally:
#     print("Finally is executed")


# class nameisvibi(Exception):
#     def __init__(self, message="Sorry, the name 'vibi' is not allowed."):
#         super().__init__(message)
    
# def greet(name: str):
#     if not name.isalpha():
#         raise ValueError("Please enter a valid name only alphabets")
#     else:
#         print(f"Hi {name} welcome !!!")

#     if name=="vibi":
#         raise nameisvibi("Shit he is vibi")


# while True:
#     n=input("Enter Name: ")
#     try:
#         greet(n)

#     except ValueError as e:
#         print(e)

#     except nameisvibi as ee:
#         print(ee)

# try:
#     with open("/mnt/e/Study/Self/devops/Python/Git/python-for-devops/Test_script/sample.txt", "r") as file:
#         content= file.read()
# except IOError or FileNotFoundError:
#     print("Error not able to read")
# else:
#     print(content)

# Operator Overriding

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, o):
#         print(self.x + o.x ,self.y + o.y)
#         return Point(self.x + o.x, self.y + o.y)
    
#     def __str__(self) -> str:
#         return f"{self.x, self.y}"

# p1=Point(1,2)
# p2=Point(2,3)

# print(p1+p2)

# class test:
#     def __init__(self, x):
#         self.x = x

#     # def pri(self):
#     #     return test(x="HI VIbish")
    
#     def __str__(self, y) -> str:
#         return self.x+y


# aa=test("Jack")

# print(aa.__str__("timmy"))


# def fibonacci_sequence(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         yield a  # Yield the current Fibonacci number
#         a, b = b, a + b
#         count += 1

# # Using the generator to print the first 10 Fibonacci numbers
# fib_gen = fibonacci_sequence(10)
# for num in fib_gen:
#     print(num)


# try:
#     a=iter(a)
#     while True:
#         print(next(a))
    
# except StopIteration:
#     pass

