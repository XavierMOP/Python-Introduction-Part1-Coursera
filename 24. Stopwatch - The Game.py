# template for "Stopwatch: The Game"
import simpleguitk as simplegui

# define global variables

time = 0
success = 0
total_played = 0
timer_status = False

'''
Why use 0.1 interval instead of 1.0, why use time in integer instead of float : floatint point is imprecise.
'''

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D


def format(t):
    A = t // 600
    B = (t - A * 600) // 100
    C = (t - A * 600 - B * 100) // 10
    D = t - A * 600 - B * 100 - C * 10
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)

# help functions to check the success/total


def total_played_check():
    global total_played, timer_status
    if timer_status is True:
        total_played += 1
        timer_status = False


def success_check():
    global success
    if time % 10 == 0 and time != 0 and timer_status is True:
        success += 1
# define event handlers for buttons; "Start", "Stop", "Reset"


def start():
    global timer_status
    if timer_status is False:
        timer.start()
        timer_status = True


def stop():
    timer.stop()
# call success check and total check order is crucial
    success_check()

    total_played_check()


def reset():
    timer.stop()
    global time, success, total_played
    time = 0
    success = 0
    total_played = 0

# define event handler for timer with 0.1 sec interval


def tick():
    global time
    time += 1


timer = simplegui.create_timer(100, tick)

# define draw handler


def draw(canvas):
    canvas.draw_text(str(format(time)), (20, 130), 60, 'Red')
    canvas.draw_text(str(success) + '/' + str(total_played), (200, 50), 30, 'Green')


# create frame
frame = simplegui.create_frame("Stopwatch - The game", 300, 150)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frameS
frame.start()
