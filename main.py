import APIinterface, random




previous = input("Enter a password: ")

for i in range(5):
    requirement = APIinterface.makeRequirement(previous)
    print(requirement)
    while (True):
        previous = input("Enter a password: ")
        result = APIinterface.check(previous,requirement)
        if "true" in result:
            break
        else: #For ease of reading, the else is here even though the break is above.
            print(APIinterface.roast(previous,requirement))

