d={"name":"risla","age":23,"class":"MCA"}
n=input("Enter a key to check : ")
if n in d.keys():
   print(" Key found")
else:
    print("key not found")
print(d.items())
for dict_key,dict_value in d.items():
    print(str(dict_key)+"->"+str(dict_value))
m={"mark":30}
d.update(m)

print(d)