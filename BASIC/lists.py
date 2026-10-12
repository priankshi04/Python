#LISTS
dogs=["roger","Syd", True] # can contain any heterogeneous values
print("roger" in dogs)
# reference items using indexes
print(dogs[2])
dogs[2]="Beau"
dogs.append("judah")
dogs.extend(["judah",5])# to combine 2 list together
dogs+= ["Judah", 5]# another method to add list dont forget square brackets
print(dogs)
# index method
print(dogs[-1])# returns True as -1 begins from the end
print(dogs[2:4]) # starts from index 2 ends before 4
print(dogs[-2:])# starts from 2nd last element and goes to the first
print(dogs[:3])# begin from 1st and stop before 3rd index
print(len(dogs))# length of the list
dogs.remove("judah")# remove the first judah
print(dogs)
dogs.insert(0,"Niko")
dogs[1:1]=["Test1","Test2"]
print(dogs)
dogs.sort()
print(dogs)
# sorted function
#list compression
nums = [1,2,3,4,5]
nums_power_2 =[n**2 for n in nums]# simple method instead of using for loop
print(nums_power_2)
