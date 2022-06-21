from mymodule import person1 #renamed module
import platform

age = person1["age"]
country = person1["country"]
name = person1["name"]

x = platform.system()
#y = dir(platform)
#w = platform.__version__

print ("hello my name is",name ,"I am ", age, "years old and born in ", country)

print (x)
#print (y)
#print (w)

