# Handling Dividing By Zero Error
x = 42 
y = 0
# Dividing X by Y
try:
    print(x/y)
except ZeroDivisionError as e:
    print("Cannot Divide By Zero")
else:
    print("Something Else Went Wrong")
finally:
    print("Yay, Success!")