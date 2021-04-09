import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.2
checkmark = "￮ ￮ ￮ ￮"
reps = 0
timer = None
the_start = 0

#---------------------------Decorator---------------------------#
def check_start(function):
    def wraper():
        global the_start
        the_start += 1
        if the_start == 1:
            function()
    return wraper


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer, checkmark, the_start
    the_start = 0
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark = "￮ ￮ ￮ ￮"
    tick_marks.config(text=checkmark)
# ---------------------------- TIMER MECHANISM ------------------------------- # 

@check_start
def start_timer():
    global reps
    reps += 1
    global checkmark
    work_sec = int(WORK_MIN * 60)
    s_break_sec = int(SHORT_BREAK_MIN * 60)
    l_break_sec = int(LONG_BREAK_MIN * 60)
    if reps % 8 == 0:
        checkmark = checkmark[:reps % 9 - 2] + "●" + checkmark[(reps % 9 - 2) + 1:]
        tick_marks.config(text=checkmark)
        label.config(text="Break", fg=RED)
        count_time(l_break_sec)
    elif reps % 2 == 0:
        checkmark = checkmark[:reps % 9 - 2] + "●" + checkmark[(reps % 9 - 2) + 1:]
        tick_marks.config(text=checkmark)
        label.config(text="Break", fg=PINK)
        count_time(s_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        count_time(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_time(count):
    global timer, the_start
    text = f"{int(count / 60)}:{count % 60}"
    if count % 60 < 10:
        text = f"{int(count/60)}:0{count%60}"
    canvas.itemconfig(timer_text, text=text)
    if count > 0:
        timer = window.after(1000, count_time, count - 1)
    elif reps < 8:
        the_start = 0
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=80, pady=80, bg=YELLOW)

label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label.grid(row=0, column=1)

tomato_img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold "))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="start", fg='#28527a', highlightthickness=0, font=FONT_NAME)
start_button.config(command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="reset", fg='#28527a', highlightthickness=0, font=FONT_NAME)
reset_button.config(command=reset_timer)
reset_button.grid(row=2, column=2)


tick_marks = tk.Label(text=checkmark, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
tick_marks.grid(row=3, column=1)



window.mainloop()
