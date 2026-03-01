
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty '+ 'Days '+ 'Of '+'Python ')
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding '+ 'For ' + 'All' )
# Declare a variable named company and assign it to an initial value "Coding For All".
company= "Coding For All"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize().title().swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[:6])
    # Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
# Replace the word coding in the string 'Coding For All' to Python.
company=company.replace("Coding ","Python ")
print(company)
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
company=company.replace("Everyone","All")
print(company)
# Split the string 'Coding For All' using space as the separator (split()) .
company.split(' ')
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_list = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list.split(',')
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(len(company)-1)
print(company[len(company)-1])
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(company.split(' ')[0][0] + company.split(' ')[1][0] + company.split(' ')[2][0])
# i know its a for loop :) 
acronym = "".join(word[0] for word in company.split())
print(acronym)


# Create an acronym or an abbreviation for the name 'Coding For All'.
name='Coding For All'
print(name.split(' ')[0][0] + name.split(' ')[1][0] + name.split(' ')[2][0])


# Use index to determine the position of the first occurrence of C in Coding For All.
print(name.index("C"))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(name.index("F"))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(name.rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_pos = sentence.find("because")
print("First position:", first_pos)
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[first_pos:first_pos + len("because because because")]
print("Sliced phrase:", phrase)
# Does 'Coding For All' start with a substring Coding?
string = "Coding For All"
print("Starts with Coding:", string.startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
print("Ends with coding:", string.endswith("coding"))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
spaced_string = "   Coding For All      "
trimmed = spaced_string.strip()
print("Trimmed string:", trimmed)
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"

print("30DaysOfPython is identifier:", var1.isidentifier())
print("thirty_days_of_python is identifier:", var2.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined = " # ".join(libraries)
print("Joined libraries:", joined)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

print("I am enjoying this challenge.\nI just wonder what is next.")


# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2

print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))


# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144



a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

# 🎉 CONGRATULATIONS ! 🎉