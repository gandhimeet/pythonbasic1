# Python Basic Exercises Repository

Welcome to the Python Basic Exercises repository! This repository contains a collection of Python Basic exercises to help you practice and improve your Python programming skills. Each exercise is designed to cover fundamental concepts and features of the Python programming language.

## Table of Contents

1. [Introduction](#introduction)
2. [Exercises](#exercises)
3. [How to Use](#how-to-use)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction

This repository hosts a variety of Python Basic exercises that cover topics such as variables, data types, loops, conditionals, functions, and more. Whether you're a beginner looking to learn Python or an experienced developer wanting to brush up on your skills, these exercises can be a great resource.

## Exercises

The exercises are organized into different categories based on the concepts they cover. Here's an overview of the categories and some example exercises:
## Program 1
**Write a Python program to print the following string in a specific format (see the output).**

Sample String : 

"Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

 
### Code Explanation
-The first line of the string starts with "Twinkle, twinkle, little star," followed by a newline character \n.

-The second line starts with a tab character \t, followed by "How I wonder what you are!" and another newline character \n.

-The third and fourth lines have two tabs \t\t before the phrases "Up above the world so high," and "Like a diamond in the sky." They are followed by newline characters \n.

-The fifth line starts with "Twinkle, twinkle, little star," and ends with a newline character \n.

-The sixth line is similar to the second line, starting with a tab character \t, followed by "How I wonder what you are."

## Program 2
**Write a Python program to find out what version of Python you are using.**

### Code Explanation
-The first line imports the sys module, which is a built-in module in Python that provides access to system-specific parameters and functions.

-The sys.version attribute contains a string that represents the version of Python, including details like the release version, build information, and compiler used to build Python.

-The elenenth line prints another string, "Python Version INFO," to the console to indicate the type of information being displayed next.

-The sys.version_info attribute contains a tuple of integers representing the major, minor, micro, release level, and serial of the Python interpreter.

## Program 3
**Write a Python program to display the current date and time.

Sample Output :

Current date and time :
2014-07-05 14:34:14**

Output:

Current date and time:2014-07-05 14:34:14

### Code Explanation
-The first line imports the datetime module, which provides classes and methods for working with dates and times.

-The second line uses the now() method from the datetime module to retrieve the current date and time and stores it in the now variable. This gives you the current date and time as a datetime object.

-The strftime() method is used to format the now datetime object into a string with a specific format. The format string "%Y-%m-%d %H:%M:%S" is used to specify how the date and time should be displayed

-%Y: Year with century as a decimal number (e.g., 2023).
 
 %m: Month as a zero-padded decimal number (01, 02, ..., 12).

 %d: Day of the month as a zero-padded decimal number (01, 02, ..., 31).

 %H: Hour (24-hour clock) as a zero-padded decimal number (00, 01, ..., 23).
 
 %M: Minute as a zero-padded decimal number (00, 01, ..., 59).
 
 %S: Second as a zero-padded decimal number (00, 01, ..., 59)

## Program 4
**Write a Python program that calculates the area of a circle based on the radius entered by the user.

Sample Output :

r = 1.1
Area = 3.8013271108436504**

### Code Explanation:
-The first line of code importing the pi constant from the math module. pi represents the mathematical constant π (pi), which is approximately equal to 3.141592653589793.

-The code prompts the user to enter the radius of a circle by displaying the message "Enter the Radius of the circle:".
It then takes the user's input as a string and converts it into a floating-point number (decimal number) using float(input(...)).

-The code calculates the area of a circle using the formula for the area of a circle: A = π * r^2, where A is the area and r is the radius.Then it converts the result to a string using str(...) to prepare it for concatenation.

-At end the code displays the result as a string using the print(...) function.

## Program 5
**Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.**

### Code Explanation
-The code prompts the user to enter their first name and last name using the input function and stores these values in the firstname and lastname variables, respectively.

-In last line It concatenates the user's last name, first name, and a greeting message ("HEY!") into a single string using the + operator.

-In type conversion converts the firstname and lastname variables to strings using the str() function, ensuring they can be concatenated with other strings.

-At the end it prints the combined string, which includes the greeting, last name, and first name, effectively displaying a reverse order of the user's name with a greeting.

## Program 6
**Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

Sample data : 3, 5, 7, 23**

Output :

List : ['3', ' 5', ' 7', ' 23']

Tuple : ('3', ' 5', ' 7', ' 23')

### Code Explanation
-First line of code start by asking the user to input some values separated by commas using the input function. The entered values are stored in the variable values.

-The input values are split into a list using the split method with a comma , as the separator. The resulting list is stored in a variable called list.

-The list is converted into a tuple using the tuple() constructor, and the resulting tuple is stored in a variable named tuple.

-At the end the code prints the tuple variable, displaying the values as a tuple. Note that using tuple as a variable name might not be a good practice since it overwrites the built-in tuple type.

## Program 7
**Write a Python program that accepts a filename from the user and prints the extension of the file.

Sample filename : abc.java**

Output : java

### Code Explation
-The code prompts the user to enter the name of a file, including its extension, and stores it in the filename variable.

-Display File Name prints out the name of the entered file, including the extension, to the console.

-The code splits the filename using the dot (.) as a separator and stores the resulting parts in the extension variable. This effectively extracts the file's extension.

-Display Extension then prints out the extracted extension of the file name to the console, using the -1 index to access the last part of the extension list, which is typically the file's extension.

## Program 8
**Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]**

### Code Explanation
-The code creates a list named color_list containing four color names: "Red," "Green," "White," and "Black."

-The String formatting uses string formatting with the % operator to print the first and last elements of the color_list list. %s is a placeholder for string values.

-color_list[0] accesses the first element ("Red") of the list, and color_list[-1] accesses the last element ("Black").

-The code prints the result as "Red Black," which are the first and last color names in the list, separated by a space.

## Program 9
**Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)

Sample Output : The examination will start from : 11 / 12 / 2014**

### Code Explanation
-exam_st_date is a variable used to store the examination date, which is set to (11, 12, 2023). This date is represented as a tuple with day, month, and year components.

-The print statement is used to display a formatted message. It uses string formatting to insert the values from the exam_st_date tuple into the message.

-The "%i / %i / %i" within the string is a format specifier. The %i placeholders are placeholders for integer values, and they are used to indicate where the values from the exam_st_date tuple should be inserted.

-When the code is executed, it will print a message that reads something like "The examination will start from: 11 / 12 / 2023", where the numbers 11, 12, and 2023 are replaced by the values from the exam_st_date tuple.

## Program 10
**Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

Sample value of n is 5

Expected Result : 615**

### Code Explanation
-This Python code takes an integer input 'n' from the user.

-It creates three new variables: 'n1', 'n2', and 'n3', each containing 'n' repeated 1, 2, and 3 times, respectively, by formatting the input as strings and converting them back to integers.

-It calculates the sum of 'n1', 'n2', and 'n3'.

-At the end it prints the result as "The Value of n+nn+nnn is:" followed by the sum of 'n1', 'n2', and 'n3' converted to a string.

## Program 11
**Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

Sample function : abs()

Expected Result :abs(number) -> number Return the absolute value of the argument.**

### Code Explanation
-The code snippet uses the abs() function in Python, which is a built-in function for calculating the absolute value of a number.

-It prints the documentation string (docstring) of the abs() function using abs.__doc__. The docstring is a descriptive text that provides information about what the function does and how to use it.

-In this case, print(abs.__doc__) will display the documentation for the abs() function, helping users understand its purpose and usage.

-This code is a simple example of how to access and display the docstring of a Python function using the .__doc__ attribute.

## Program 12
**Write a Python program that prints the calendar for a given month and year.

Note : Use 'calendar' module.**

### Code Explanation
-The code begins by importing the calendar module, which provides various functions and classes for working with calendars, including generating calendar views for different years and months.

-It prompts the user to enter two integers: one for the year (stored in the variable y) and another for the month (stored in the variable m). The int(input(...)) function combination is used to read integer input from the user via the console.

-After obtaining the user's input for the year and month, it utilizes the calendar.month(y, m) function to generate and display a calendar view for the specified year and month. This function takes the year (y) and month (m) as arguments and returns a formatted string representing the calendar for that specific month.

-At the end the code prints the generated calendar string to the console, displaying the calendar for the user-provided year and month.


## Program 13
**Write a Python program to print the following 'here document'.

Sample string :

a string that you "don't" have to escape

This

is a ....... multi-line

heredoc string --------> example**

### Code Explanation
-The code uses triple double-quotes (""") to define a multi-line string. This allows you to include both single and double quotes within the string without escaping them.

-Inside the string, there is an example of escaping double quotes using the backslash ("don't"). This means the double quotes around "don't" are included as part of the string.

-The string spans multiple lines, and the indentation is preserved as part of the string content. So, the spaces before "This" and "is a..." are part of the string.

-The string content itself includes line breaks and various whitespace characters, which are also preserved as-is. The string ends with the text "example", but it includes all the line breaks and indentation within the triple-quoted string.


## Program 14
**Write a Python program to calculate the number of days between two dates.

Sample dates : (2014, 7, 2), (2014, 7, 11)

Expected output : 9 days**

### Code Explanation
-The code imports the date class from the datetime module, allowing you to work with date objects.

-It creates a firstdate variable and assigns it the date June 22, 2023.

-It creates a lastdate variable and assigns it the date June 26, 2023.

-It calculates the difference between lastdate and firstdate and stores it in the delta variable. Then, it prints the number of days between the two dates using delta.days.

## Program 15
**Write a Python program to get the volume of a sphere with radius six.**

### Code Explanation
-The code begins by importing the mathematical constant pi from the math module.

-Defining the radius : It sets the variable 'r' to a value of 6.0, which represents the radius of a sphere.

-It calculates the volume of the sphere using the formula for the volume of a sphere, which is (4/3)πr^3, and stores the result in the 'volume' variable.

-At the end it prints out a message that displays the radius and calculated volume of the sphere using the 'print' function. It converts numerical values to strings and combines them with text for the output message.

## Program 16
**Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.**
## Program 17
**Write a Python program to test whether a number is within 100 of 1000 or 2000.**
## Program 18
**Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.**
## Program 19
**Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".**
## Program 20
**Write a Python program that returns a string that is n (non-negative integer) copies of a given string.**
## Program 21
**Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.**
## Program 22
**Write a Python program to count the number 4 in a given list.**
## Program 23
**Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.**
## Program 24
**Write a Python program to test whether a passed letter is a vowel or not.**
## Program 25
**Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False**
## Program 26

## Program 27

## Program 28

## Program 29

## Program 30

## Program 31

## Program 32

## Program 33

## Program 34

## Program 35

## Program 36

## Program 37

## Program 38

## Program 39

## Program 40

## Program 41

## Program 42

## Program 43

## Program 44

## Program 45

## Program 46

## Program 47

## Program 48

## Program 49

## Program 50

## Program 51

## Program 52

## Program 53

## Program 54

## Program 55

## Program 56

## Program 57

## Program 58

## Program 59

## Program 60

## Program 61

## Program 62

## Program 63

## Program 64

## Program 65

## Program 66

## Program 67

## Program 68

## Program 69

## Program 70

## Program 71

## Program 72

## Program 73

## Program 74

## Program 75

## Program 76

## Program 77

## Program 78

## Program 79

## Program 80

## Program 81

## Program 82

## Program 83

## Program 84

## Program 85

## Program 86

## Program 87

## Program 88

## Program 89

## Program 90

## Program 91

## Program 92

## Program 93

## Program 94

## Program 95

## Program 96

## Program 97

## Program 98

## Program 99

## Program 100

## Program 101

## Program 102

## Program 103

## Program 104

## Program 105

## Program 106

## Program 107

## Program 108

## Program 109

## Program 110

## Program 111

## Program 112

## Program 113

## Program 114

## Program 115

## Program 116

## Program 117

## Program 118

## Program 119

## Program 120

## Program 121

## Program 122

## Program 123

## Program 124

## Program 125

## Program 126

## Program 127

## Program 128

## Program 129

## Program 130

## Program 131

## Program 132

## Program 133

## Program 134

## Program 135

## Program 136

## Program 137

## Program 138

## Program 139

## Program 140

## Program 141

## Program 142

## Program 143

## Program 144

## Program 145

## Program 146

## Program 147

## Program 148

## Program 149

## Program 150


## How to Use

1. Clone the repository to your local machine using `git clone <repository-url>`.
2. Navigate to the relevant exercise directory using a terminal or command prompt.
3. Open the Python file for the exercise using a code editor or an IDE.
4. Read the exercise description and code provided.
5. Attempt to solve the exercise following the instructions.
6. Compare your solution with the provided solution in the file.
7. Repeat the process for other exercises.

Feel free to modify the code, experiment with different solutions, and learn from the exercises. The exercises are designed to encourage hands-on learning and practice.

## Contributing

Contributions to this repository are welcome! If you have additional exercises, improvements to existing exercises, or bug fixes, please follow these steps:

1. Fork the repository to your GitHub account.
2. Create a new branch from the `main` branch for your changes.
3. Make your changes, add new exercises, or make improvements.
4. Commit your changes with descriptive commit messages.
5. Push the changes to your forked repository.
6. Create a pull request targeting the `main` branch of this repository.

Your contributions can help others learn and improve their Python skills.

## License

This repository is licensed under the [MIT License](LICENSE). You are free to use the code and exercises for personal or educational purposes.

---

Happy coding!

Meet Gandhi & Rutvi Rathod
meetgandhi586@gmail.com
