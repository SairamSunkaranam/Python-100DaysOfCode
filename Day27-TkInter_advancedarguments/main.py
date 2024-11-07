import tkinter

gui = tkinter.Tk()

gui.title("Test GUI")
gui.minsize(width=1000, height=800)
gui.config(padx=100, pady=100)

def click_button():
    # lable_test["text"] ="Button clicked"
    # lable_test.config(text="Button Clicked")
    lable_test.config(text=input.get())

#label
lable_test = tkinter.Label(text="Nekenduke ra", font=("Times New Roman", 24, "bold"))
lable_test.grid(column=0, row=0)
lable_test.config(padx=50, pady=50)

#Button
button = tkinter.Button(text="Click me", command=click_button)
button.grid(column=1, row=1)

button1 = tkinter.Button(text="Click me", command=click_button)
button1.grid(column=2, row=0)

input = tkinter.Entry()
input.grid(column=3, row=2)



gui.mainloop()