# Practice Exercises for Logic and Conditionals
# Solve each of the practice exercises below. Each problem includes three CodeSkulptor links: one for a template that you should use as a starting point for your solution, one to our solution to the exercise, and one to a tool that automatically checks your solution.

# Write a Python function \color{red}{\verb|is_even|}is_even that takes as input the parameter \color{red}{\verb|number|}number (an integer) and returns \color{red}{\verb|True|}True if \color{red}{\verb|number|}number is even and \color{red}{\verb|False|}False if \color{red}{\verb|number|}number is odd. Hint: Apply the remainder operator to \color{red}{\verb|n|}n (i.e., \color{red}{\verb|number % 2|}number%2) and compare to zero. Even template --- Even solution --- Even (Checker)
# Write a Python function \color{red}{\verb|is_cool|}is_cool that takes as input the string \color{red}{\verb|name|}name and returns \color{red}{\verb|True|}True if \color{red}{\verb|name|}name is either \color{red}{\verb|"Joe"|}"Joe", \color{red}{\verb|"John"|}"John" or \color{red}{\verb|"Stephen"|}"Stephen" and returns \color{red}{\verb|False|}False otherwise. (Let's see if Scott manages to catch this. ☺ ) Cool template --- Cool solution --- Cool (Checker)
# Write a Python function \color{red}{\verb|is_lunchtime|}is_lunchtime that takes as input the parameters \color{red}{\verb|hour|}hour (an integer in the range [1, 12][1,12]) and \color{red}{\verb|is_am|}is_am (a Boolean “flag” that represents whether the hour is before noon). The function should return \color{red}{\verb|True|}True when the input corresponds to 11am or 12pm (noon) and \color{red}{\verb|False|}False otherwise. If the problem specification is unclear, look at the test cases in the provided template. Our solution does not use conditional statements. Lunchtime template --- Lunchtime solution --- Lunchtime (Checker)
# Write a Python function \color{red}{\verb|is_leap_year|}is_leap_year that take as input the parameter \color{red}{\verb|year|}year and returns \color{red}{\verb|True|}True if \color{red}{\verb|year|}year (an integer) is a leap year according to the Gregorian calendar and \color{red}{\verb|False|}False otherwise. The Wikipedia entry for leap yearscontains a simple algorithmic rule for determining whether a year is a leap year. Your main task will be to translate this rule into Python. Leap year template --- Leap year solution --- Leap year (Checker)
# Write a Python function \color{red}{\verb|interval_intersect|}interval_intersect that takes parameters \color{red}{\verb|a|}a, \color{red}{\verb|b|}b, \color{red}{\verb|c|}c, and \color{red}{\verb|d|}d and returns \color{red}{\verb|True|}True if the intervals [a, b][a,b] and [c, d][c,d] intersect and \color{red}{\verb|False|}False otherwise. While this test may seem tricky, the solution is actually very simple and consists of one line of Python code. (You may assume that a \leq ba≤b and c \leq dc≤d.) Interval intersect template --- Interval intersect solution --- Interval intersect (Checker)
# Write a Python function \color{red}{\verb|name_and_age|}name_and_age that take as input the parameters \color{red}{\verb|name|}name (a string) and \color{red}{\verb|age|}age (a number) and returns a string of the form \color{red}{\verb|"% is % years old."|}"%is%yearsold." where the percents are the string forms of \color{red}{\verb|name|}name and \color{red}{\verb|age|}age. The function should include an error check for the case when \color{red}{\verb|age|}age is less than zero. In this case, the function should return the string \color{red}{\verb|"Error: Invalid age"|}"Error:Invalidage". Name and age template --- Name and age solution --- Name and age (Checker)
# Write a Python function \color{red}{\verb|print_digits|}print_digits that takes an integer \color{red}{\verb|number|}number in the range [0,100)[0,100) and prints the message \color{red}{\verb|"The tens digit is %, and the ones digit is %."|}"Thetensdigitis%,andtheonesdigitis%." where the percents should be replaced with the appropriate values. The function should include an error check for the case when \color{red}{\verb|number|}number is negative or greater than or equal to 100100. In those cases, the function should instead print (\color{red}{\verb|"Error: Input is not a two-digit number."|}"Error:Inputisnotatwo-digitnumber.". print (digits template --- print (digits solution --- print (digits (Checker)
# Write a Python function \color{red}{\verb|name_lookup|}name_lookup that takes a string \color{red}{\verb|first_name|}first_name that corresponds to one of (\color{red}{\verb|"Joe"|}"Joe", \color{red}{\verb|"Scott"|}"Scott", \color{red}{\verb|"John"|}"John" or \color{red}{\verb|"Stephen"|}"Stephen") and then returns their corresponding last name (\color{red}{\verb|"Warren"|}"Warren", \color{red}{\verb|"Rixner"|}"Rixner", \color{red}{\verb|"Greiner"|}"Greiner" or \color{red}{\verb|"Wong"|}"Wong"). If \color{red}{\verb|first_name|}first_name doesn't match any of those strings, return the string \color{red}{\verb|"Error: Not an instructor"|}"Error:Notaninstructor". Name lookup template --- Name lookup solution --- Name lookup (Checker)
# Pig Latin is a language game that involves altering words via a simple set of rules. Write a Python function \color{red}{\verb|pig_latin|}pig_latin that takes a string \color{red}{\verb|word|}word and applies the following rules to generate a new word in Pig Latin. If the first letter in \color{red}{\verb|word|}word is a consonant, append the consonant plus \color{red}{\verb|"ay"|}"ay" to the end of the remainder of the word. For example, \color{red}{\verb|pig_latin("pig")|}pig_latin("pig") would return \color{red}{\verb|"igpay"|}"igpay". If the first letter in \color{red}{\verb|word|}word is a vowel, append \color{red}{\verb|"way"|}"way" to the end of the word. For example, \color{red}{\verb|pig_latin("owl")|}pig_latin("owl") returns \color{red}{\verb|"owlway"|}"owlway". You can assume that \color{red}{\verb|word|}word is in lower case. The provided template includes code to extract the first letter and the rest of \color{red}{\verb|word|}word in Python. Note that, in full Pig Latin, the leading consonant cluster is moved to the end of the word. However, we don't know enough Python to implement full Pig Latin just yet. Pig Latin template --- Pig Latin solution --- Pig Latin (Checker)
# Challenge: Given numbers aa, bb, and cc, the quadratic equation a x^2 + b x + c = 0ax
# 2
#  +bx+c=0 can have zero, one or two real solutions (i.e; values for xx that satisfy the equation). The quadratic formulax = \frac{-b \pm \sqrt{b^2 - 4 a c}}{2 a}x=
# 2a
# −b±
# b
# 2
#  −4ac
# ​
# ​	 can be used to compute these solutions. The expression b^2 - 4 a cb
# 2
#  −4ac is the discriminant associated with the equation. If the discriminant is positive, the equation has two solutions. If the discriminant is zero, the equation has one solution. Finally, if the discriminant is negative, the equation has no solutions. Write a Python function \color{red}{\verb|smaller_root|}smaller_root that takes an input the numbers \color{red}{\verb|a|}a, \color{red}{\verb|b|}b and \color{red}{\verb|c|}c and returns the smaller solution to this equation if one exists. If the equation has no real solution, print (the message \color{red}{\verb|"Error: No real solutions"|}"Error:Norealsolutions" and simply return. Note that, in this case, the function will actually return the special Python value \color{red}{\verb|None|}None. Quadratic root template --- Quadratic root solution --- Quadratic root (Checker)


# SOLUTIONS

import random


def is_even(n):
    print(n)
    if n % 2 == 0:
        print('even')
    elif n % 2 == 1:
        print('odd')
    else:
        print('Ah???')
        return n


is_even(random.randint(-99, 99))
is_even(4.5)

print('')


def is_cool(name):
    if name == 'Haha' or name == 'Bibi':
        print(name, 'is cool')
    else:
        print(name, 'is not cool')


is_cool('Haha')
is_cool('Sisi')

print('')


def is_lunchtime(hour, is_am):
    # hour = random.randint (0, 12)
    # print (str(hour))
    if (hour == 11 and is_am is True) or (hour == 12 and is_am is True):
        print('it is', str(hour), 'and it is lunchtime')
    else:
        print('Nononononono')


is_lunchtime(11, True)
is_lunchtime(12, True)
is_lunchtime(10, True)
is_lunchtime(11, False)

print('')


def isleapyear(year):
    if year % 400 == 0:
        print(str(year), 'is leap year')
    elif year % 100 == 0:
        print('HahaNono')
    elif year % 4 == 0:
        print(str(year), 'is leap year')
    else:
        print('HahaNono')


isleapyear(1900)
isleapyear(2000)
isleapyear(2018)
isleapyear(1903)

print('')


def is_leap_year(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else:
        return False


year = 44
is_leap_year(year)

if is_leap_year:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

year = 44

print('')


def name_and_age(name, age):
    if age < 0:
        print('Wrong!')
        # return 'Wrong!'
    elif age == 1:
        print(str(name), 'is', str(age), 'year old.')
    else:
        print(str(name), 'is', str(age), 'years old.')
        # return name, 'is', age, 'old.'


name_and_age('Bibi', 44)
name_and_age('Cici', -1)
name_and_age('Dada', 1)
name_and_age('2333', 12)


print('')


def print_digits(num):
    print(num)
    if (num < 0) or (num >= 100):
        print('Wrong!!!')
    else:
        print('The tens digit is', num // 10,
              'and the ons digit is', num % 10, '.')


print_digits(random.randint(-50, 150))


print('')


def first_name(name):
    if name == 'AAA':
        return 'aaa'
    elif name == 'BBB':
        return 'bbb'
    elif name == 'CCC':
        return 'ccc'
    else:
        return 'Error'


def check(name):
    print(first_name(name))


check('AAA')
check('BBB')
check('AA')

print('')


def pig_latin(word):
    first_letter = word[0]
    rest_of_word = word[1:]
    # if first_letter == 'a' or 'e' or 'i' or 'o' or 'u':
    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u':
        return word + 'way'
    else:
        return rest_of_word + first_letter + 'ay'


def test(word):
    print(pig_latin(word))


test("pig")
test("owl")
test("python")

print('')


def smaller_root(a, b, c):
    if b ** 2 - 4 * a * c >= 0 and a != 0:
        return (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    else:
        # print ('No root!')
        return


def abc(a, b, c):
    print(str(a) + "x^2 + " + str(b) + "x + " + str(c))
    print(str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c))
    print(smaller_root(a, b, c))


abc(random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100))
abc(1, 2, 3)
abc(2, 0, -10)
abc(6, -3, 5)
abc(0, 3, 3)

print('a', 'b')
print('a' 'b')
print(str(34), '34')
