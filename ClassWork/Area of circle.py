# SIMPLE FUNCTION
def simple_area():
    pi = 22 / 7
    for i in range(1, 11):
        radius = int(input(f"Enter radius of the circle {i}: "))
        area=pi*radius**2
        print(f"Area of the circle using simple function is: {area}")

simple_area()
print("\n\n")
# SIMPLE return type FUNCTION
def simple_return_area():
    pi = 22 / 7
    radius = int(input(f"Enter radius of the circle: "))
    area = pi * radius ** 2
    return area

for i in range(1, 11):
    print(f"Area of circle using return type function is: {simple_return_area()}")
print("\n\n")

# PARAMETERIZED FUNCTION

def param_area(r):
    pi=22/7
    area=pi*r**2
    print(f"Area of the circle using parameterized function is: {area}")

for i in range(1, 11):
    radius = int(input(f"Enter radius of the circle {i}: "))
    param_area(radius)
print("\n\n")
#PARAMETERIZED WITH RETURN TYPE FUNCTION
def param_return_area(r):
    pi=22/7
    return pi*r**2

for i in range (1,11):
    radius=int(input(f"Enter radius of the circle {i}: "))
    print(f"Area of the circle using return type parameterized function is: {param_return_area(radius)}")
print("\n\n")