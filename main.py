import APIinterface, random

previous = input("Enter a password: ")

for i in range(10):
    requirement = APIinterface.makeRequirement(previous)
    print(APIinterface.roast(previous))
    print(requirement)
    while (True):
        previous = input("Enter a password: ")
        result = APIinterface.check(previous,requirement)
        if "true" in result:
            true = " "
            break
        print("TRY AGAIN:")

