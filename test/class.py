#single inheritance
# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         self.area=self.length * self.breadth
#         print("the area is {} ".format(self.area))
#     def perimeter(self):
#         self.perimeter=2*(self.length + self.breadth)
#         print("the perimeter is {} ".format(self.perimeter))
# class square(rectangle):
#     def __init__(self, side):
#         super().__init__(side,side)
# s=square(12)
# s.area()
# s.perimeter()
# r=rectangle(10,12)
# r.area()
# r.perimeter()

#multiple inheritance
# class A:
#     def __init__(self,a):
#         self.a=a
#     def show(self):
#         print("this is A class {}".format(self.a))
# class B:
#     def __init__(self,b):
#         self.b=b
#     def show(self):
#         print("this is B class {}".format(self.b))
# class AB(A,B):
#     def __init__(self, a,b):
#         super(AB,self).__init__(a)
#         #super(AB,self).__init__(b)
#         #B(self).__init__(b)
#         B(b)
#     def show(self):
#         super(AB, self).show()
#         B(self).show()
#

# #operator overloading
# class A:
#     def __init__(self,a):
#         self.a=a
#     def __lt__(self, other):
#         if self.a<other.a:
#             return "object 1 is lesser "
#         else :
#             return "object 2 is lesser"
#     def __eq__(self, other):
#         if self.a==other.a:
#             return "they are equal"
#         else:
#             return "they are not equal"
# object1=A(56)
# object2=A(56)
# print(object1 < object2)
# print(object1 == object2)


