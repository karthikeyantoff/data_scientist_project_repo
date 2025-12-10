# class main:
#     name=""
#     def party(self):
#         print("party")
#     def drinks(self):
#         print("drinks")
# obj1=main()
# obj2=main()

# obj1.party()
# obj2.drinks()
# obj1.name="karthi"
# print(obj1.name)
# in below the funcdition you print this type using cons
# self.name
# the self key word is used to refere a curent object

# class phone:
#     def __init__(self,brand,price,chartype):
#         self.brand=brand
#         self.price=price
#         self.chartype=chartype
#     def printt(self):
#         print(self.brand)
#         print(self.price)
#         print(self.chartype)
# obj=phone("mi","1000","c type")
# obj.printt()

# class phone:
#     chartype="c type"
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def printt(self):
#         print(self.brand)
#         print(self.price)
#         print(self.chartype)
# phone.chartype="b type"
# obj=phone("mi","1000")
# obj.printt()

# class phone:
#     chartype="c type"
#     def __init__(self):
#         self.price=0
#         self.brand=""
#     def setprice(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def printt(self):
#         print(self.brand)
#         print(self.price)
        
#     @classmethod
#     def changechartype(cls):
#         cls.chartype="b type"
#         print(cls.chartype)
        
#     @staticmethod
#     def info():
#         print("static method")

# obj=phone()
# obj.setprice("samsung",2000)
# phone.changechartype()
# obj.printt()
# obj.info()

# 1. Define a function that accepts one parameter
#    (we can call the parameter 'my_list')
def print_my_list(my_list):
    for i in my_list:
        for j in my_list:
            if i+j==5:
                return my_list[i,j]

d=[1,2,3]
ans=print_my_list(d)
print(ans)