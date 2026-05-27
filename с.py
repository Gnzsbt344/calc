from tkinter import *
def click_on_button(number):
    current = calc_entry.get()
    calc_entry.delete(0, END)
    calc_entry.insert(0, str(current) + str(number))
def click_on_button_clear():
    calc_entry.delete(0, END)
def click_on_button_equal():
    try:
        result = eval(calc_entry.get())
        calc_entry.delete(0, END)
        calc_entry.insert(0, result)
    except Exception as ex:
        calc_entry.delete(0, END)
        calc_entry.insert(0, ex)
root = Tk()
root.title("Калькулятор")
root.iconbitmap("icon.ico")
calc_entry = Entry(width=45)
calc_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+'
]
row = 1
col = 0
for button in buttons:
    if button == 'C':
        Button(text=button, padx=40, pady=20, command=click_on_button_clear).grid(row=row, column=col)
    else:
        Button(text=button, padx=40, pady=20, command=lambda x=button: click_on_button(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
Button(text="=", padx=80, pady=20, command=click_on_button_equal).grid(row=5, column=1, columnspan=2)


root.mainloop()