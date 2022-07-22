import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def userInput():
    length = int(input("How long would you like your password to be?\n"))
    return length


def getUsername():
    userName = str(input("Please enter your desired username: "))
    return userName


def generatePassword(temp_length):
    random.shuffle(characters)  # shuffle characters
    password = []
    for i in range(temp_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password2 = ("".join(password))  # join is used to convert list into str through concatenation
    return password2


def createDictionary(name, password):
    firstDictionaryEver = {name: password}
    return firstDictionaryEver


def driver():
    print("\nHello! \nThis program will generate a password for you, of your chosen length!\n")

    Plength = userInput()
    finalPassword = generatePassword(Plength)
    finalName = getUsername()
    myDict = createDictionary(finalName, finalPassword)

    print(myDict)


if __name__ == '__main__':
    driver()

# thisdict = {
##  "brand": "Ford","ex:"ex"}
# print(thisdict["brand"])
