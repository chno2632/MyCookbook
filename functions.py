def greet_user():
    print("Hello")
    print("Welcome")

def greet_user_by_name(name="user", greeting="Hello"):
    print(greeting + " " + name)


def cube(base_number):
    cubed_number = base_number * base_number * base_number
    return cubed_number


greet_user()
greet_user_by_name("What is yor name? " )
greet_user_by_name()
greet_user_by_name("Christer", "Welcome")
greet_user_by_name(input("What is your name: "),  "Welcome")
greet_user_by_name(greeting="Welcome", name="Christer")

eleven_cube = cube(11)
print(eleven_cube)