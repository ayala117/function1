#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

# Example usage
obj = StringManipulator()
obj.getString()
obj.printString()
#hello-HELLO