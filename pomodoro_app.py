
import tkinter

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Ubuntu"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Reps = 0
timer = None  # Initialize timer as a global variable
x1 = 245
# UI setup
window = tkinter.Tk()
window.title('Pomodoro')
window.minsize(width=600, height=400)
window.config(bg=YELLOW)

# COUNTDOWN MECHANISM

def check_mark_position():
    global x1
    for x_cor in range(1):
        x1 += 15
        check_mark = tkinter.Label(text="✓", fg=GREEN, bg=YELLOW)
        check_mark.place(x=x1, y=305)

def start_button_action():
    global Reps
    Reps += 1
    if Reps == 1 or Reps == 3 or Reps == 5 or Reps == 7:
        countdown(WORK_MIN * 60)
        work_break.config(text='Work', font=('Courier', 50), bg=YELLOW, fg=GREEN, highlightbackground=YELLOW)
        if Reps != 1:
            check_mark_position()
    elif Reps == 2 or Reps == 4 or Reps == 6 or Reps == 8:
        countdown(SHORT_BREAK_MIN * 60)
        work_break.config(text='Break', fg=RED)


    elif Reps == 9:
        countdown(LONG_BREAK_MIN * 60)
        work_break.config(text='Break', fg=RED)
        Reps = 0
    print(Reps)

def countdown(count):
    global timer
    global Reps
    first_result = int(count / 60)
    second_result = int(count % 60)
    if second_result < 10:
        second_result = '0' + str(second_result)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
        canvas.itemconfig(the_timer, text=f'{first_result}:{second_result}')
    elif count == 0:
        start_button_action()

def reset_button_action():
    global Reps
    global timer  # Access the global timer variable
    global the_timer
    window.after_cancel(timer)  # Cancel the timer
    canvas.itemconfig(the_timer, text="25:00")
    work_break.config(text='Work', font=('Courier', 50), bg=YELLOW, fg=GREEN, highlightbackground=YELLOW)

    Reps = 0

# working with tkinter Canvas to add photo

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_png)
the_timer = canvas.create_text(105, 132, text='25:00', font=('Courier', 32), fill='white')
canvas.place(x=190, y=55)

start_button = tkinter.Button(text='Start', bg=YELLOW, highlightbackground=YELLOW, command=start_button_action)
start_button.place(x=90, y=300)

reset_button = tkinter.Button(text='Reset', bg=YELLOW, highlightbackground=YELLOW, command=reset_button_action)
reset_button.place(x=420, y=300)

work_break = tkinter.Label(text='Work', font=('Courier', 50), bg=YELLOW, fg=GREEN, highlightbackground=YELLOW)
work_break.place(x=227, height=60)

check_mark = tkinter.Label(text="✓", fg=GREEN, bg=YELLOW)
check_mark.place(x=245, y=305)

window.mainloop()

