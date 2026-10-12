#TUPLES similar to list except first brackert
names=("Roger","syd")# syntax to write tuple
names[0] #value at 0 index
names.index("Roger") # return the index value of the given element
names[-1]
len(names)# length
print("Roger" in names) #check the avail
names[0:2]
sorted(names) # sort the elements in ascending order cannot modify tuple
newTuple = names + ("Tina","Quincy")# add new to original tuple

# DICTONARY key value pair
dog ={ "name":"Roger", "age":22 ,"Race":"Indian"}
print(dog['name'])
dog['name'] = "syd"
print(dog)
print(dog.get("name")) # to get the value of the given key
print(dog.get("color", "brown"))
#output brown
# but if value is not present in the given array then give the value assign by it
print(dog.pop("name"))
print(dog)# to get the value after using pop func
print(dog.popitem())# to remove the last key value pair and get that item
print(dog)
print(dog.keys()) #return keys
print(dog.values())#return values
print(dog.items())# return all the items in a list
print(list(dog.items())) # to convert to list
dog["favourite_color"] = "blue"# method to insert key value pair
del dog['favourite_color']
dogCopy = dog.copy()
print(dog)
print(dog)
