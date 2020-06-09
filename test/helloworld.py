#Iterators in python
# my_list=[1,2,3,4,5,6]
# iter_obj=iter(my_list)
# while True:
#     try:
#         element=next(iter_obj)
#         print(element)
#         pass
#     except StopIteration:
#         break

#Generators in python
# def my_gen(n):
#     n=n+1
#     print("This is the first iteration")
#     yield n
#
#     n = n + 10
#     print("This is the second iteration")
#     yield n
#
#     n = n + 100
#     print("This is the third iteration")
#     yield n
# for i in my_gen(10):
#     print(i)


#generator comprehension

# my_list=[1,2,3,4,5,6]
# a=(x**2 for x in my_list)
# print("generator comprehension")
# for i in range(0,6):
#     print(next(a),end=" ")

#DECORATOR
# def make_pretty(func):
#     def inner():
#         print("Am decorated..")
#
#     return  inner
# @make_pretty
# def ordinary():
#     print("Am ordinary..")
# ordinary()
#
# #Divide by zero
# def smart_divide(func):
#     def inner(a,b):
#         print("division of {} By {}".format(a,b))
#         if b==0:
#             print("Division not possible")
#         else:
#             return func(a,b)
#     return inner
# @smart_divide
# def divide(a,b):
#     print(a/b)
# divide(2,0)

#list comprehensions

even_number=[x for x in range(10) if x % 2 == 0]
print(even_number)

#DC
print({x:x*x for x in range(10)})