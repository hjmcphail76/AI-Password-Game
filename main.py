import APIinterface, random




previous = input("Enter a password: ")

for i in range(3):
    requirement = APIinterface.makeRequirement(previous)
    print(requirement)
    while (True):
        previous = input("Enter a password: ")
        checkPassword = "Check the following text: " + previous + "    .To see if it meets the following requirement: " + requirement +  "   . Return ONLY the words true or false."
        result = APIinterface.check(checkPassword)
        print(result)
        if result == "true":
            break
