# Booleans
#done = True# need to be capital T
#done = False# need to be capital F for boolean values
done="Beau" # here the type is str and 
# 0 is considered false and rest other int are considered true
# String are always true if it is not empty , otherwise false
print(type(done)==bool)# to check if the given str is bool or not
if done:
    print("yes")
else:
    print("no")
book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])# returns if any of the given variable is true
read_any_book1 = all([book_1_read, book_2_read]) #returns if all the values are true
# Number Datatypes
#int  integer numbers
#float  decimal values
#complex  extension of real no + imaginary no
num= complex(2,3)
print(num.real, num.imag)# to call real and imag no returns as floats can you 'type' function to check the type
#BUILT-IN FUNCTIONS
abs((5.5)) #returns only positive no
print(round(5.49,1))# 1 is another parameter to round to nearest 1 decimal value
