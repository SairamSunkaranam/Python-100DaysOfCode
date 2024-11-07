import tkinter

window = tkinter.Tk()
# window.minsize(width=300, height=100)
window.title("Miles to KM convertor")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = int(input.get())
    print(miles)
    km = miles * 1.609
    label3.config(text=km)


input = tkinter.Entry(width=7)
input.insert(index=0, string="0")
print(input.get())
input.grid(column=1, row=0)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = tkinter.Label(text="0")
label3.grid(column=1, row=1)

label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=2)

button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)




window.mainloop()