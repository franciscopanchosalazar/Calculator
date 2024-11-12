from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.font as font

with open("developer_info.txt", "r") as file:
    info_description = file.read()

current_value = ""
# Function which is called when pressing a number
def show_num(button_text):
    global current_value
    current_value += str(button_text)
    main_text.set(current_value)

def del_b():
    global current_value
    current_value = current_value[:-1] 
    main_text.set(current_value)

def ac_b():
    global current_value
    current_value = ""
    main_text.set(current_value)

def new_window():
    showinfo(title='Program information', message=info_description)



# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

root = Tk(className="Calculator")
#root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="black")

screen_row = 1
screen_column = 0

font_size = font.Font(size=15)
bt_px = 30
bt_py = 20
bt_width = 1
bt_height = 1

main_text = StringVar()

e = Entry(root, textvariable=main_text, fg="white", bg="green", font=font_size, justify=RIGHT, borderwidth=10, width=32)
e.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

# Numeric buttons
for i in range(9, 0, -1):
    numeric_buttons = Button(root, text=str(i), fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width,
                            command=lambda num_to_pass=i: show_num(num_to_pass))
    numeric_buttons.grid(row=screen_row, column=screen_column)

    screen_column += 1
    if screen_column == 3:
        screen_row += 1
        screen_column = 0

# Zero and operational buttons
b0 = Button(root, text="0", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=lambda num_to_pass="0": show_num(num_to_pass))
b_dot = Button(root, text=".", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=lambda num_to_pass=".": show_num(num_to_pass))
b_exp = Button(root, text="Exp", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=lambda num_to_pass="Ans": show_num(num_to_pass))
b_ans = Button(root, text="Ans", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=lambda num_to_pass="": show_num(num_to_pass))
b_eq = Button(root, text="=", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width)
b_add = Button(root, text="+", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=lambda num_to_pass=" + ": show_num(num_to_pass))
b_sub = Button(root, text="-", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=lambda num_to_pass=" - ": show_num(num_to_pass))
b_mul = Button(root, text="X", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=lambda num_to_pass=" X ": show_num(num_to_pass))
b_div = Button(root, text="/", fg="white", bg="black", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=lambda num_to_pass=" / ": show_num(num_to_pass))
b_del = Button(root, text="DEL", fg="black", bg="yellow", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=del_b)
b_ac = Button(root, text="AC", fg="black", bg="yellow", font=font_size, padx=bt_px, pady=bt_py, width=bt_width, command=ac_b)

b0.grid(row=4, column=0)
b_dot.grid(row=4, column=1)
b_exp.grid(row=4, column=2)
b_ans.grid(row=4, column=3)
b_eq.grid(row=4, column=4)
b_add.grid(row=3, column=3)
b_sub.grid(row=3, column=4)
b_mul.grid(row=2, column=3)
b_div.grid(row=2, column=4)
b_del.grid(row=1, column=3)
b_ac.grid(row=1, column=4)    

root.mainloop()
