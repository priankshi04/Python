#Objects
age = 48
print(age.real) # real part
print(age.imag)# imag part
print(age.bit_length())# return the bit length use to represnt the no
items=[1,2]
items.append(3)
items.pop()
print(id(items))
# if object provides content to change its value then it is mutable otherwise immutable
# int, tuple, str,bool, float, frozenset - immutable list,dict, set - mutables
age1=8
age= age1 +1 # will create a whole new object
print(age)
print(age1)

# Loops
#while and for loop
condition = True # infinite loop
while condition == True:
    print("The condition is true")
    condition = False

count = 0
while count<10:
    print("The condition is true")
    count += 1
print("After the loop")

items=[1,2,3,4] # can we do names
for index,item in enumerate((items)): # return index and item
    print(index,item)# prints in every new line so updating to enumerate

items1=[1,2,3,4]
for item in items1:
    if item == 2:
        continue# gonna skip 2
    elif item == 3:
        break # gonna break the loop
    print(item)
