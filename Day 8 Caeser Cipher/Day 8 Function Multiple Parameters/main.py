def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#Main
name = input("Write your name: ")
location = input("What is your current location: ")
greet_with(location=location,name=name)
    