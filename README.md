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

### Code Explanation 
-The code defines a function called difference that takes one argument, n.

-Inside the function, it checks if the value of n is less than or equal to 17. If it is, it calculates the difference between 17 and n and returns it. If n is greater than 17, it calculates twice the difference between n and 17 and returns that value.

-The code then calls the difference function with two different values, 22 and 10, and prints the results.

-When n is 22, the function returns 10 because it falls into the else branch and calculates (22-17)*2, which equals 10. When n is 10, the function returns 7 because it falls into the if branch and calculates 17-10, which equals 7.

## Program 17
**Write a Python program to test whether a number is within 100 of 1000 or 2000.**

### Code Explanation
-The code defines a function called near_thousand that takes one argument, n.

-Inside the function, it checks if the absolute difference between n and 1000 is less than or equal to 100 OR if the absolute difference between n and 2000 is less than or equal to 100.

-The function returns True if either of these conditions is met, indicating that the input number is "near" either 1000 or 2000; otherwise, it returns False.

-The code then calls the near_thousand function with various numbers and prints the results, showing whether each number is "near" 1000 or 2000 based on the defined criteria.

## Program 18
**Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.**

### Code Explanation
-Function Definition: The code defines a function called sum_thrice that takes three arguments, x, y, and z.

-Inside the function, it calculates the sum of the three input values x, y, and z and stores it in a variable called sum.

-It then checks if x, y, and z are all equal by using the condition x == y == z.

-If x, y, and z are all equal, it multiplies the sum by 3 (triples it). Otherwise, it returns the original sum.

## Program 19
**Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".**

### Code Explanation
-The code defines a function called new_string that takes one parameter, text.

-Inside the function, there's a conditional check using an if statement. It checks if the length of the text is greater than or equal to 2 characters and if the first two characters of text are "Is."

-If the condition is met, meaning the input text already starts with "Is" or is at least two characters long, the function returns text as it is. Otherwise, it adds "Is" to the beginning of text and returns the modified string.

-The code then calls the new_string function twice: First with the argument "Array," and it prints the result. In this case, the function adds "Is" to "Array," so it prints "IsArray." Second with the argument "IsEmpty," and it prints the result. Since "IsEmpty" already starts with "Is," the function returns it as it is, so it prints "IsEmpty."

## Program 20
**Write a Python program that returns a string that is n (non-negative integer) copies of a given string.**

### Code Explanation
-The code defines a function named larger_string that takes two arguments: text (a string) and n (an integer).

-Inside the function, a variable named result is initialized with a single space character (' '). This variable will store the repeated string.

-The code uses a for loop that runs n times to concatenate the text with the result variable. This effectively repeats the text n times and stores the result in the result variable.

-The code demonstrates the larger_string function by calling it twice with different inputs and printing the results. The first call repeats 'Meet Gandhi' twice and prints the result, and the second call repeats 'Rutvi Rathod' three times and prints the result.

## Program 21
**Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.**

### Code Explanation
-The code first takes an integer input from the user and stores it in the variable num.

-Modulo Calculation calculates the remainder of num when divided by 2 and stores it in the variable mod. This is done using the modulo operator %, which helps determine if the number is even or odd.

-The code uses an if-else statement to check the value of mod. If mod is greater than 0, it means the number is odd. If mod is 0, it means the number is even.

-Depending on whether the number is odd or even, the code prints either "This is an odd number." or "This is an even number." to inform the user about the nature of the input number.

## Program 22
**Write a Python program to count the number 4 in a given list.**

### Code Explanation
-The function count_num_4 takes a list of numbers called nums as input.

-Inside the function, it initializes a variable count to 0, which will be used to count the number of times the value 4 appears in the input list.

-It then uses a for loop to iterate through each number in the nums list. If a number in the list is equal to 4, it increments the count variable by 1.

-At th end the function returns the value of count, which represents the number of times the value 4 appeared in the input list.

## Program 23
**Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.**

### Code Explanation

## Program 24
**Write a Python program to test whether a passed letter is a vowel or not.**

### Code Explanation
-The code defines a function named is_vowel that takes one argument char, which is expected to be a single character.

-Inside the function, there is a string variable everyvowel containing all lowercase and uppercase vowels ('aeiouAEIOU').

-The function checks whether the input character char is present in the everyvowel string. If the character is a vowel (either lowercase or uppercase), the function returns True; otherwise, it returns False.

-At rhe end the code calls the is_vowel function with different characters ('a', 'A', 'c', 'F') and prints the results. It checks if each character is a vowel and displays True or False accordingly.

## Program 25
**Write a Python program that checks whether a specified value is contained within a group of values.

Test Data :

3 -> [1, 5, 8, 3] : True

-1 -> [1, 5, 8, 3] : False**

### Code Explanation 
-The code defines a Python function named isgroupmember which takes two parameters: groupdata (a list) and n (an element to check for membership in the list).

-Inside the function, there is a for loop that iterates through each element in the groupdata list.

-Within the loop, it checks if the current element (value) is equal to the provided value n. If they are equal, it immediately returns True, indicating that n is a member of the groupdata.

-If the loop completes without finding a match (i.e., n is not in groupdata), the function returns False. The code then calls this function twice, once with [1,2,3,4,5,3,3] and 3 as arguments, and once with [1,2,3,4,5] and -1 as arguments, and prints the results.

## Program 26
**Write a Python program to create a histogram from a given list of integers.**

### Code Explanation
-The code defines a Python function called histogram(item) that takes a list of integers (item) as input.

-Inside the function, a for loop iterates through each integer in the input list. For each integer n in the list, the code initializes an empty string output and a variable times with the value of n.

-Using a while loop, the code repeatedly adds an asterisk (*) to the output string as long as times is greater than 0. This effectively creates a string of asterisks whose length is equal to the value of n.

-After generating the asterisk string for each integer in the input list, the code prints each output string on a separate line. This results in a histogram-like pattern of asterisks, where each line represents the value of an integer in the input list.

## Program 27
**Write a Python program to print all even numbers from a given list of numbers in the same
order and stop printing any after 237 in the sequence.

Sample numbers list :

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]**

### Code Explanation
-The code begins by defining a list named numbers containing a sequence of integers. This list serves as the input data for the code, and it contains a mix of random numbers.

-The code then enters a for loop that iterates through each element (x) in the numbers list one by one.

-he first if statement checks if the current value of x is equal to 237. If this condition is true, it prints the value of x and then immediately exits the loop using the break statement. This means that if 237 is encountered in the list, it will be printed, and the loop will terminate. The elif (short for "else if") statement checks if the current value of x is an even number (divisible by 2) by using the modulo operator (%). If the condition is true, it prints the value of x. So, whenever an even number is encountered in the list, it will be printed.

-The code executes these conditional statements while iterating through the numbers list. It prints the numbers that meet the specified conditions (equal to 237 or even) and stops when it encounters the number 237. If 237 is not in the list, it will print all even numbers in the list before terminating.

## Program 28
**Write a Python program that concatenates all elements in a list into a string and returns it.**

### Code Explanation
-The code defines a function named concate that takes one parameter, list, which is expected to be a list of elements.

-Inside the function, an empty string named result is initialized. This string will be used to store the concatenated values of the elements in the input list.

-The code uses a for loop to iterate through each element in the input list. During each iteration, the current element is converted to a string (using str(element)) and then appended to the result string using the += operator. This process continues until all elements in the input list have been concatenated.

-At the end the function returns the result string, which contains the concatenated values of the elements in the input list. The function is then called with a sample list [2, 3, 4, 5, 7, 9, 15], and the result is printed using print.

## Program 29
**Write a Python program that prints out all colors from color_list_1 that are not 
present in color_list_2.

Test Data :

color_list_1 = set(["White", "Black", "Red"])

color_list_2 = set(["Red", "Green"])

Expected Output :

{'Black', 'White'}**

### Code Explanation
-Two sets, color_list_1 and color_list_2, are defined with different color elements.

-The code prints the set color_list_1 minus the elements present in color_list_2, which is the difference between the two sets. This will output the elements unique to color_list_1.

-The code also prints the set color_list_2 minus the elements present in color_list_1, which is the difference between the two sets. This will output the elements unique to color_list_2.

## Program 30
**Write a Python program that will accept the base and height 
of a triangle and compute its area.**

### Code Explanation
-The code starts by prompting the user to enter the base and height of a triangle using the "input" function. It takes these values as integers and stores them in the "base" and "height" variables, respectively.

-The code then calculates the area of the triangle using the formula for the area of a triangle: area = (height * base) / 2. It performs this calculation and stores the result in the "area" variable.

-Finally, the code prints out the calculated area of the triangle using the "print" function. It converts the "area" variable to a string and includes it in the output message.

-The user sees the calculated area of the triangle as the final output on the screen.

## Program 31
**Write a Python program that computes the greatest common divisor (GCD) 
of two positive integers.**

### Code Explanation
-This code defines a function called gcd (Greatest Common Divisor) that calculates the greatest common divisor of two numbers, x and y.

-It initializes gcd to 1. If x is evenly divisible by y, it returns y as the greatest common divisor.

-Otherwise, it iterates through a range of numbers from y/2 down to 1, checking if both x and y are divisible by the current number (k). If they are, it updates the gcd with the current k value and breaks out of the loop.

-The code then calls the gcd function with different sets of parameters and prints the results, finding the greatest common divisors of pairs of numbers: (12, 17), (4, 6), and (336, 360).

## Program 32
**Write a Python program to find the least common multiple (LCM) of two positive integers.**

### Code Explanation
-This code defines a function named lcm that calculates the least common multiple (LCM) of two numbers, x and y. It determines the greater of the two input numbers and assigns it to the variable z.

-Then, it enters a while loop that continues until it finds a number (z) that is divisible by both x and y (i.e., their remainders are both zero when divided by z).

-Once it finds such a number, it assigns it to the variable lcm and breaks out of the loop.

-Finally, the function returns the calculated LCM. The code then demonstrates the usage of the lcm function by calling it with two different sets of parameters and printing the results: lcm(4, 6) and lcm(15, 17).

## Program 33
**Write a Python program to sum three given integers. 
However, if two values are equal, the sum will be zero.**

### Code Explanation
-The code begins by defining a function named sum_three that takes three parameters: x, y, and z. This function is intended to calculate the sum of these three numbers, with a special condition.

-Inside the function, there is a conditional check using the if statement. It checks whether x is equal to y, y is equal to z, or x is equal to z. If any of these conditions are true, it implies that at least two of the three input values are the same.

-If the conditional check in the previous step evaluates to true (i.e., two or more input values are the same), the sum variable is set to 0. This means that the sum of the three numbers is zero in this case.

-Finally, the function returns the value of the sum variable, which is either the sum of x, y, and z or 0, depending on the condition. The code then calls this sum_three function with four different sets of input values and prints the results.

## Program 34
**Write a Python program to sum two given integers. 
However, if the sum is between 15 and 20 it will return 20.**

### Code Expllanation
-The code defines a Python function named sum that takes two parameters, x and y. This function is designed to calculate the sum of x and y.

-Inside the function, the sum of x and y is calculated and stored in a variable also named sum. However, it's important to note that using the same name as a built-in function or keyword (in this case, sum) is generally not recommended, as it can lead to confusion and unexpected behavior. This code overwrites the built-in sum function temporarily.

-After calculating the sum, there is a conditional check to see if the sum falls within the range of 15 (inclusive) to 20 (exclusive). If the sum is within this range, the function returns the integer value 20.

-Finally, the code demonstrates the usage of the sum function by calling it with two sets of different arguments and printing the results

## Program 35
**Write a Python program that returns true if the two given integer values 
are equal or their sum or difference is 5.**

### Code Explanation
-The code defines a Python function named test_number that takes two parameters, x and y.

-Inside the test_number function, there is a conditional statement that checks three conditions using logical OR (or) operators: x == y: This condition checks if x is equal to y. abs(x - y) == 5: This condition checks if the absolute difference between x and y is equal to 5. (x + y) == 5: This condition checks if the sum of x and y is equal to 5.

-If any of the above conditions are true, the function returns True. This means that if either x is equal to y, the absolute difference between x and y is 5, or the sum of x and y is 5, the function will return True.
If none of the conditions are met, the function returns False

-The code demonstrates the use of the test_number function by calling it four times with different sets of values and printing the results

## Program 36
**Write a Python program to add two objects if both objects are integers.**

### Code Explanation
-The code defines a Python function called add(x, y), which takes two parameters, x and y. This function is designed to perform addition on these parameters.

-Inside the function, there's an input validation check. It uses the isinstance() function to verify whether both x and y are of the integer type (int). If either x or y is not an integer, the function returns the string "Inputs must be Integers.". This is done to ensure that only valid integer inputs are accepted for addition.

-If both x and y are integers, the function proceeds to perform the addition operation by using the + operator. It calculates the sum of x and y.

-The code demonstrates the usage of the add function by making four function calls

## Program 37
**Write a Python program that displays your name, age, and address on three different lines.**

### Code Explanation
-The code starts by prompting the user to enter their name, age, and address using the input() function. input("Enter Your Name:") waits for the user to input their name as a string and assigns it to the variable name.input("Enter Your Age:") waits for the user to input their age as an integer (which is converted from the input string) and assigns it to the variable age.input("Enter Your Address:") waits for the user to input their address as a string and assigns it to the variable addr.

-The code uses three variables to store the user's input: name, age, and addr. These variables hold the user-provided information for further use.

-The code then proceeds to print out the collected information in a formatted manner. It uses the format() method to replace the placeholders {}, which are inside the string, with the values stored in the name, age, and addr variables. 

-The resulting output is displayed with labels for each piece of information, separated by line breaks, making it more readable.

## Program 38
**Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49**

### Code Explanation
-The code begins by taking user input for two integer values, X and Y, using the input function. It prompts the user to enter these values by displaying a message. The int() function is used to convert the user's input into integer data types, ensuring that the entered values can be used for mathematical operations.

-After collecting the values of X and Y from the user, the code calculates a mathematical expression: (X + Y) ^ 2. This is achieved by assigning the result of the expression to the variable result. The expression x*x + 2*x*y + y*y is used to compute the square of the sum of X and Y, which involves squaring X, squaring Y, and adding twice the product of X and Y to the result.

-The code employs the print function to display the result of the expression in a user-friendly format.
It uses the .format() method to insert the values of X, Y, and the computed result into a string. Inside the string, {} placeholders are used to indicate where these values should be inserted.

-Finally, the code prints the formatted string containing the values of X, Y, and the computed result to the console. This output provides the user with the squared value of the sum of X and Y in a clear and readable format.

## Program 39
**Write a Python program to compute the future value of a specified principal amount,
rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79**

### Code Explanation 
-amt = 10000: This line initializes a variable amt with a value of 10,000. It likely represents an initial investment amount. int = 3.5: This line initializes a variable int with a value of 3.5. However, it's important to note that "int" is a reserved keyword in Python and should not be used as a variable name. It might be better to use a different name, like interest_rate, to avoid conflicts. years = 7: This line initializes a variable years with a value of 7, indicating the number of years for which the investment will grow.

-future_value = amt * ((1 + (0.01 * int)) ** years): This line calculates the future value of the investment using the formula for compound interest. It takes the initial amount (amt), multiplies it by the compound interest formula, and assigns the result to the variable future_value. The formula used here is: future_value = principal * (1 + (interest_rate / 100)) ^ time, where principal is the initial amount, interest_rate is the annual interest rate in percentage (converted to decimal form), and time is the number of years.

-print(round(future_value, 2)): This line prints the calculated future value after rounding it to two decimal places. The round() function is used to ensure that the result is displayed with only two decimal points for better readability.

-When you run this code, it will calculate the future value of the 10,000 investment with a 3.5% annual interest rate over 7 years and print the result rounded to two decimal places. The printed value will represent how much the initial investment will grow to after 7 years under the given interest rate.

## Program 40
**Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).**

### Code Explanation
-The code begins by importing the math module, which provides mathematical functions and constants in Python. In this case, it is used to access the sqrt function, which will be used to calculate the square root of a value.

-Two points, p1 and p2, are declared as lists. Each point is represented as a list with two elements: the first element represents the x-coordinate, and the second element represents the y-coordinate. In this code, p1 is [4, 0], and p2 is [6, 6].

-The code calculates the Euclidean distance between p1 and p2 using the Euclidean distance formula. This formula computes the square root of the sum of the squares of the differences between the x-coordinates and the y-coordinates of the two points. The calculated distance is stored in the variable distance.

-Finally, the code prints the calculated distance using the print function. The result is the Euclidean distance between p1 and p2, which is the straight-line distance between these two points in the 2D plane. In this example, the result will be printed to the console.

## Program 41
**Write a Python program to check whether a file exists.**

### Code Explanation
-The code begins with the line import os.path, which imports the os.path module in Python.

-The first print statement print(os.path.isfile('main.txt')) checks whether a file named 'main.txt' exists in the current directory. The os.path.isfile() function is used for this purpose. If the file exists, it will return True; otherwise, it will return False. In this case, it will likely print False because 'main.txt' is stated as not being in the directory.

-The second print statement print(os.path.isfile('program31.py')) checks whether a file named 'program31.py' exists in the current directory. S

-Similar to the previous check, it uses os.path.isfile() to determine if the file exists. Depending on whether 'program31.py' is present in the directory or not, it will print either True or False.

## Program 42
**Write a Python program to determine 
if a Python shell is executing in 32bit or 64bit mode on OS.**

### CodeExplanation
-The code starts by importing the 'struct' module in Python. This module provides tools for working with C-style data structures and allows you to interpret binary data packed in a specific format.

-The code then calls the 'struct.calcsize("P")' function. This function calculates the size of a C-style pointer (P) on the current platform. In many programming languages, including Python, the size of a pointer can vary between different architectures. Typically, it can be either 32 bits (4 bytes) or 64 bits (8 bytes) depending on whether the system is 32-bit or 64-bit.

-After calculating the size using 'struct.calcsize("P")', the code multiplies the result by 8. This step is performed to convert the size from bytes to bits since 1 byte equals 8 bits. The result of this calculation represents the size of a pointer in bits on the current platform.

-Finally, the code prints the calculated size in bits to the console using the 'print' statement. This line of code provides the user with information about whether the system's pointer size is 32 bits or 64 bits, which can be helpful when dealing with low-level memory operations or platform-specific code.

## Program 43
**Write a Python program to get OS name, platform and release information.**

### Code Explanation
-The code starts by importing two Python modules - os and platform. These modules are necessary to access and retrieve information about the operating system and the underlying hardware platform.

-The code uses os.name to retrieve and print the name of the current operating system. The os.name function returns a string representing the name of the operating system, such as 'posix' for Unix-based systems or 'nt' for Windows.

-Next, the code uses platform.system() to obtain and print the name of the underlying hardware platform or system. This function returns a string representing the platform name, which can be 'Linux', 'Windows', 'Darwin' (for macOS), or others depending on the system.

-Lastly, the code utilizes platform.release() to fetch and print the release or version number of the operating system. This function returns a string representing the version of the operating system, such as '10.0.19041' for a specific version of Windows.

## Program 44
**Write a Python program to locate Python site packages.**

###code Explanation
-The code begins by importing the site module in Python. The site module is a standard library module that provides access to various properties and functions related to Python's site-specific configuration. It is commonly used for tasks related to Python's site-specific installation and package management.

-The code calls the getsitepackages() function from the site module. This function is used to retrieve a list of directories or paths where Python packages are typically installed on a system. These directories represent the locations where Python looks for and stores third-party packages and modules.

-The code calls the getsitepackages() function from the site module. This function is used to retrieve a list of directories or paths where Python packages are typically installed on a system. 

-These directories represent the locations where Python looks for and stores third-party packages and modules.

## Program 45
**Write a Python program that calls an external command.**

### Code Explanation
-The code begins by importing the subprocess module, which allows Python to interact with and execute external shell commands.

-This code defines a Python function named call_external_command that takes a single argument, command. This function is designed to run external shell commands from within a Python script.

-Inside the function, the specified command is executed using subprocess.check_output(). It captures the command's output and stores it in the variable output.

-The code includes error handling using a try-except block. If the external command returns a non-zero exit status (indicating an error), it catches the subprocess.CalledProcessError exception, prints an error message with the exit status and any available error output, and handles the error gracefully.

## Program 46
**Write a Python program to retrieve the path and name of the file currently being executed.**

### Code Explanation
-The code begins by importing the 'os' module, which provides a way to interact with the operating system, including tasks like working with file paths.

-The 'os.path.realpath(file)' expression is used to retrieve the absolute file path of the currently executed script or program. 'os.path' is a sub-module of 'os' that deals with file paths, and 'realpath()' is a method within it that resolves the given path to its absolute form, resolving any symbolic links and relative references. 'file' is a built-in variable in Python that represents the path to the current Python script.

-The 'print()' statement is used to display a message to the console. It prints the text "Name of current file:" followed by the absolute file path of the currently executing Python script, which is obtained using 'os.path.realpath(file)'.

-When you run this code, it will display the name of the current file along with its absolute path as the output, providing information about the location of the script that is being executed.

## Program 47
**Write a Python program to find out the number of CPUs used.**

### Code Explanation
-The code begins by importing the 'multiprocessing' module, which is a Python library used for parallel and concurrent computing. It allows you to take advantage of multiple CPU cores to execute tasks concurrently.

-The code calls the 'multiprocessing.cpu_count()' function. This function is used to determine the number of CPU cores or processors available on the computer where the Python script is running.

-The result of 'multiprocessing.cpu_count()' is printed to the console. This will display the number of CPU cores available on the system.

-The main purpose of this code snippet is to provide information about the number of CPU cores available on the computer. This information can be useful when designing and implementing parallel or concurrent programs to ensure efficient utilization of the available hardware resources.

## Program 48
**Write a Python program to parse a string to float or integer.**

### Code Explanation
-The code begins by prompting the user to input a floating-point value. It uses the input function to capture user input and assigns it to the variable n.

-After receiving the user's input, the code converts the inputted value to a floating-point number using the float function. This ensures that the value entered by the user is treated as a decimal number, even if it was initially entered as a string.

-The code then prints the floating-point value using the print function. This line displays the entered value as a floating-point number, preserving any decimal places.

-Lastly, the code converts the floating-point value back to an integer using the int function and then prints it. This step removes any decimal places, leaving only the integer part of the number.

## Program 49
**Write a Python program to list all files in a directory.**

### Code Explanation
-It imports the listdir function from the os module to list the contents of a directory. It also imports the isfile and join functions from the os.path module to check if a given path is a file and to join paths, respectively.

-It creates a list called fileslist using a list comprehension.

-The fileslist now contains the names of all the files in the 'D:\pythonbasic1' directory.

-It prints the fileslist, which contains the names of all the files found in the 'D:\pythonbasic1' directory, to the console.

## Program 50
**Write a Python program to print without a newline or space.**

### Code Explanation
-The code starts with a "for" loop that initializes a variable "i" to a value of 0.

-The loop will continue to execute as long as "i" is less than 10. In other words, it will iterate 10 times (from 0 to 9).

-Within each iteration of the loop, it prints a single asterisk ('*') to the standard output without moving to a new line. The "end='' " argument in the "print" function ensures that the asterisks are printed on the same line without any spaces or line breaks.

-After the loop completes all 10 iterations, it prints a single new line character ('\n'). This new line character moves the cursor to the next line, ensuring that any subsequent output appears on a new line.

## Program 51
**Write a Python program to determine the profiling of Python programs.

Note: A profile is a set of statistics that describes how often and 
for how long various parts of the program executed. 
These statistics can be formatted into reports via the pstats module.**

### Code Explanation
-The code starts by importing the cProfile module, which is used for profiling Python programs. Profiling helps in analyzing and measuring the performance of code to identify bottlenecks and optimize it.

-A function named sum is defined. This function simply calculates the sum of 1 and 2 and then prints the result (3) to the console.

-The cProfile.run() function is used to profile the sum() function. This means that when the code is executed, cProfile will gather information about the execution of the sum() function, such as the time it takes to run and the number of function calls.

-When this code is run, cProfile will collect profiling data for the sum() function and display detailed information about its execution, including the time taken by each function call and the total time spent in the function. This information can be valuable for performance analysis and optimization.

## Program 52
**Write a Python program to print to STDERR.**

### Code Explanation
-The code begins with importing two modules: __future__ and sys. from __future__ import print_function is used to ensure compatibility with Python 3.x print syntax even in Python 2.x, where the print statement is used. This is done to make the code forward-compatible.

-The code defines a custom function called eprint(*args, **kwargs). This function is designed to mimic the behavior of the standard print function, but it directs the output to the standard error stream (sys.stderr) rather than the standard output (sys.stdout). This can be useful for error messages and debugging.

-After defining the eprint function, the code prints the string "abc", "efg", and "xyz" using the standard print function. It specifies the separator sep="--", which means that the strings will be separated by "--" when printed to the standard output.

-It's important to note that the strings "abc", "efg", and "xyz" are printed to the standard output (usually the console), not to the standard error. This is because the eprint function is not used for this specific print statement.

## Program 53
**Write a Python program to access environment variables.**

### Code Explanation
-The code begins by importing the 'os' module, which is a built-in Python module used for interacting with the operating system. It provides functions to access various operating system-related functionalities, including environment variables.

-The code uses the 'os.environ' dictionary to access and print all the environment variables currently set on the system. Environment variables are system-wide settings that store information such as configuration data, system paths, and user preferences.

-It then specifically accesses and prints the value of the 'TEMP' environment variable using 'os.environ['TEMP']'. The 'TEMP' variable typically points to the temporary directory or folder used by the operating system to store temporary files.

-Similarly, the code accesses and prints the value of the 'PATH' environment variable using 'os.environ['PATH']'. The 'PATH' variable is crucial as it specifies a list of directories where the operating system searches for executable files and programs when a user enters a command in the terminal.

## Program 54
**Write a Python program to get the current username.**

### Code Explanation
-The code begins by importing the getpass module, which is a standard Python library module used for handling password input and retrieving user-related information securely.

-It uses the getuser() function from the getpass module to retrieve and print the current username of the user running the script. This username corresponds to the user currently logged into the system.

-While not explicitly mentioned in the code, this script is typically used in command-line applications to provide user-specific functionality or personalize the user's experience based on their username.

-The getpass module is often used for handling sensitive information like passwords. In this case, it's only retrieving the username, which is not sensitive. However, the module is designed to securely handle user input, making it a good choice for dealing with potentially confidential data.

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
