
"""
   Basic python strings and printing
"""
number = "42"
hello = "hello"
print (hello)
capHello = hello.capitalize()
print(hello)

replaceHello = hello.replace("l", "z")
print(replaceHello)

isChar = hello.isalpha()
print(isChar)
isNum = number.isdigit()
print(isNum)

separateString = "example,of,csv".split(",")
print(separateString)

num1 = 5
num2 = 10
num3 = 15

stringNum1 = "45"
stringNum2 = "55"
stringNum3 = "65"


printNums = "The first number is {0}, second is {1}, and the third is {2}".format(stringNum1, stringNum2, stringNum3)
print(printNums)

testString = "This is a string that does stuff"
newString = "This is also a string that does stuff"

print("Enter a value")
userInput = input()
print("The user entered ", userInput)
print ("Hello World", num1, num2, num3)
print(testString + " " + newString)
