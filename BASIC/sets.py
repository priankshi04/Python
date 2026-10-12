#sets like tuple but are not in ordered structure and are immutables
names={"roger","syd"} # uses curly braces like dict but dont have any key value pair
names2={"roger", "luna"}# sets cannot have duplicate items
intersect = names & names2# common element between them
print(intersect)
mod = names| names2 # union of two sets use this syntax '|'
print(mod)
dif = names-names2 # only set1 value would be the output after the common value is subtracted
print(dif)# like set in maths
sup= names >names2# check if one of the given set is a subset o each other
print(sup)
print(list(names))# to convert the given set into list
# can use the set conversion method to find the common values or intersect
# but as set doesnt allow duplicate values wont be optimal
