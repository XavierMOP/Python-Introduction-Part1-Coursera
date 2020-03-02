import simpleguitk as simplegui

# Week 2a reading

# 1


def print_goodbye():
    message = 'Goodbye'
    print(message)


message = "Hello"
print(message)
print_goodbye()
print(message)

message = "Ciao"
print(message)
print_goodbye()
print(message)

print('')


# 2

def set_goodbye():
    global message
    message = 'Goodbye'
    print(message)


message = "Hello"
print(message)
set_goodbye()
print(message)

message = "Ciao"
print(message)
set_goodbye()
print(message)

print('')


# 3

def reset():
    global count
    count = 0


def increment():
    global count
    count += 1


def decrement():
    global count
    count -= 1


def print_count():
    global count
    print(count)


######
# Test

# note that the GLOBAL count is defined inside a function
reset()
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
# 1
# 2
# -2
print('')

# 4

# message = "My first frame!"

# # Handler for mouse click
# def click():
#     print(message)

# # Create a frame and assign callbacks to event handlers
# frame = simplegui.create_frame("My first frame", 100, 200)
# frame.add_button("Click me", click)

# # Start the frame animation
# frame.start()	####### remember to start the frame ######

# 5

# Open frame
# Student should add code where relevant to the following.

message = "My second frame!"

# Handler for mouse click


def click():
    print(message)


# Assign callbacks to event handlers
frame = simplegui.create_frame(message, 200, 100)
frame.add_button("Click me", click)

# Start the frame animation
frame.start()
