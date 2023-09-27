print(10 > 9)
print( 10 ==9)
print(10 < 9)


a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    
#Evaluate values and variables

print(bool("Hello"))
print(bool(20))

x = 120
y = "Something"
print(bool(x))
print(bool(y))

# function can return boolean
def myFunction():
    return True

print(myFunction())

if myFunction():
    print("Yes!")
else:
    print("No!")    