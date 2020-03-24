# Remainder - modular arithmetic

# systematically restrict computation to a range
# long division - divide by a number, we get a quotient plus a remainder
# quotient is integer division //, the remainder is % (Docs)


# problem - get the ones digit of a number
import random   	# functions to generate random numbers
import math	 		# access to standard math functions, e.g; trig
num = 49
tens = num // 10
ones = num % 10
print(tens, ones)
print(10 * tens + ones, num)


# application - 24 hour clock
# http://en.wikipedia.org/wiki/24-hour_clock

hour = 20
shift = 8
print((hour + shift) % 24)


# application - screen wraparound
# Spaceship from week seven

width = 800
position = 797
move = 5
position = (position + move) % width
print(position)


# Data conversion operations

# convert an integer into string - str
# convert an hour into 24-hour format "03:00", always print leading zero

hour = 3
ones = hour % 10
tens = hour // 10
print(tens, ones, ":00")
print(str(tens), str(ones), ":00")
print(str(tens) + str(ones) + ":00")

# convert a string into numbers using int and float


# Python modules - extra functions implemented outside basic Python


# look in Docs for useful functions

print(math.pi)


def print_digits(number):
    print("tens is", str(number // 10))
    print("ones is", str(number % 10))
    return number


a = print_digits(random.randint(0, 99))

print(a)


def powerball():
    a = random.randint(0, 59)
    b = random.randint(0, 59)
    c = random.randint(0, 59)
    d = random.randint(0, 59)
    e = random.randint(0, 35)
    print("Today's numbers are", str(a), str(b), str(c), str(d), str(e))


powerball()
