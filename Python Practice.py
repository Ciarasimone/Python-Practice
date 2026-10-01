height = 1.66
age = 27

# intro
print(f"Hello, my name is Ciara. I am 27 years old. I am 166 metres tall.")

# age in 5 years
future_age = age + 5
print(f"In 5 years, I will be {future_age} years old.")

# area of a rectangle multiplication
rect_length = 5.5
rect_width = 2
area = rect_length * rect_width
print(f"The area of a rectangle with length {rect_length} and width {rect_width} is {area}.")

# string repetition and division
divider = "-" * 40 # string rep 
print(divider)

half_height = height / 2
print(f"Half of my height is {half_height} meters") # division




# ~~~~~~~~~~ Part Two <3 ~~~~~~~~~~




# user to input 2 numbers and converts them from strings to floats
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# user chooses an operation to perform on the two numbers
operation = input("Choose an operation (+, -, *, /): ")

# perform the operation per user input then print result
if operation == "+":
result = num1 + num2
print(f"{num1} + {num2} is {result}.")

elif operation == "-":
result = num1 - num2
print(f"{num1} - {num2} is {result}.")

elif operation == "*":
result = num1 * num2
print(f"{num1} * {num2} is {result}.")

elif operation == "/":
if num2 != 0:
result = num1 / num2
print(f"{num1} / {num2} is {result}.")

else:
print("Dividing by zero is not allowed!!")

else:
print("Invalid operation. Please choose from +, -, *, or /.")




    # ~~~~~~~~ Part Three <3 ~~~~~~~~
	
# prompt user for a word
word = input("Enter a word, any word!: ")

# print length of word
word_length = len(word)
print(f"Length of your word: {word_length}")

# print word in all uppercase 
print(f"Your word... but in uppercase!: {word.upper()}")

# print word 3 times
print(f"Your word... but repeated 3 times!: {word * 3}")
