from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeat = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global repeat
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark.config(text="")
    repeat = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global repeat
    repeat += 1
    pomodoro_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # print(pomodoro_sec)

    if repeat % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif repeat % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
        repeat = 0
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(pomodoro_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    global repeat

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        if repeat % 2 == 0:
            for _ in range(math.floor(repeat/2)):
                mark += "✔"
                checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()