from enum import Enum
#ENUMS
# readable names that are bound to a constant value
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE.value) # state.active returns the same statement but state.active value return the active value assigned to it
# cannot be reassigned
print(State(1))# it gonna return state.active
print(State['ACTIVE'])# gonna print state.active
# only way to create a constant so nobody can assign a value to that
print(list(State)) # to see the constant value assigned to the class State
print(len(State)) # to print the length
# INPUT FUNCTIONS
age=input("What is your age? :")
print("your age is "+age) # to get input from the user
# CONTROL STATEMENT
condition = True
if condition == False:
    print("The condition")# indentation should be same for same block
    print("was true")# condition runs a particular block that is kept inside it , runs for if condn
#print("outside if ")# always gonna print as it is outside the loop * if you want to print smething outside the loops need to write at the end not in between otherwise the else wont run
else:
    print("The condition")
    print("was false")
