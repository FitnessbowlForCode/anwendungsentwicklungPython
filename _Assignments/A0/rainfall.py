"""
Design a program that consumes a list of numbers (integers) representing daily rainfall amounts as entered by a user.
The list may contain the number -999 indicating the end of the data of interest.
Produce the average of the non-negative values in the list up to the first -999 (if it shows up).
There may be negative numbers other than -999 in the list.

Implement the rainfall problem discussed in the lecture (see the intro slides) in at least 3 alternative ways. Implement each alternative in a separate function. Be sure to handle the division-by-zero case correctly. 


Note: alternatives could be different, for example, by

- (noit) using if/else to handle the divide-by-zero
- (not) using exception to handle the divide-by-zero
- (not) using list comprehension
- (not) using some (other) loop
- (not) using a break statement
- (not) using a second list variable
- (not) using lambda expressions
- ... 

Also provide code that tests all of your alternative implementations.
"""
numbers = [1.0, -4, 2.0, 2.5, 0.5, 2, -999, -7, 4]
number = []

def vanillaRainfall(numbers):
    amount = 0
    newList = []
    try:
        for i in numbers:
            if i == -999:
                break
            elif i>=0:
                newList.append(i)

        print(newList)
        amount = sum(newList)/len(newList)
        print(amount)

    except ZeroDivisionError as msg:
        print("Ist was schief gelaufen: " + str(msg))

vanillaRainfall(numbers)
vanillaRainfall(number)