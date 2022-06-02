# # Simple Function
#
# def greet():
#    print("Hello")
#    print("How do you do? ")
#    print("Isn't the weather nice today? ")
#
# greet()
#
# # Function that allows for input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}? ")
#
# greet_with_name("WALTER")

# #Position arguments
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What it is like in {location}?")
#
# greet_with("Jack Bauer", "Newhere")

#Keyword arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What it is like in {location}?")

greet_with(location="London", name="Jack Bauer")
