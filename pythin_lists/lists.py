mylist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
newlist = []

print(mylist) #print list
print(mylist[:2]) #print the first index of the list
print(len(mylist)) #print length of the list
print(type(mylist))

mylist[1] = "orange"
mylist.insert(0,"peach")

mylist.extend(tropical)
print(mylist)

mylist.remove("papaya")
print("papaya removed")
print(mylist)

print("removed with index")
mylist.pop(3)
print(mylist)

#mylist.clear()
#print(mylist)

for x in mylist:
	print(x)

for x in mylist:
	if "a" in x:
		newlist.append(x)

print(newlist)

newlist.sort()
print(newlist)
