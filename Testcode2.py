'''class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    
    def greet(self, gender="NA"):
        print(f"Hello, {self.name}! You are {self.age} years old is gender {gender}")
    


p1=person(20,"John")
p2=person(30,"Doe")

p1.greet(gender="Male")
p2.greet()'''



# dic={"name":"vibish", "age":24, "gender":"Male"}
# key=[key for key in dic]
# print(key)


# lis=[1,2,3,4]
# print(lis.count)


file=open("sample.txt", "r")
print(file.read())


