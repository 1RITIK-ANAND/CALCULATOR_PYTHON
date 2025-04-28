import tkinter as tk
from tkinter import messagebox

# Main colors
ORANGE = "#FFA500"
DARK_ORANGE = "#FF8C00"
BLACK = "#000000"
WHITE = "#FFFFFF"

# Hover effects
def on_enter(e):
    e.widget['background'] = DARK_ORANGE
    e.widget['foreground'] = WHITE

def on_leave(e):
    e.widget['background'] = ORANGE
    e.widget['foreground'] = BLACK

# Handling button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Cannot divide by 0")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "⌫":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])
    elif text == "±":
        try:
            value = entry.get()
            if value.startswith('-'):
                entry.delete(0, tk.END)
                entry.insert(tk.END, value[1:])
            else:
                entry.delete(0, tk.END)
                entry.insert(tk.END, '-' + value)
        except:
            pass
    else:
        entry.insert(tk.END, text)

# Keyboard input binding
def key_input(event):
    key = event.char
    if key in '0123456789.+-*/':
        entry.insert(tk.END, key)
    elif key == '\r':  # Enter key
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == '\x08':  # Backspace key
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])

# Theme switching
def toggle_theme():
    global theme
    if theme == "dark":
        root.config(bg=WHITE)
        button_frame.config(bg=WHITE)
        entry.config(bg=BLACK, fg=WHITE)
        for btn in buttons_list:
            btn.config(bg=ORANGE, fg=BLACK)
        theme = "light"
    else:
        root.config(bg=BLACK)
        button_frame.config(bg=BLACK)
        entry.config(bg=WHITE, fg=BLACK)
        for btn in buttons_list:
            btn.config(bg=ORANGE, fg=BLACK)
        theme = "dark"

# Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("500x600")
root.config(bg=BLACK)
root.resizable(False, False)
theme = "dark"

# Entry Field
entry = tk.Entry(root, font=("Poppins", 28, "bold"), bg=WHITE, fg=BLACK, bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Frame for buttons
button_frame = tk.Frame(root, bg=BLACK)
button_frame.pack(expand=True)

# All buttons text
buttons = [
    ["C", "⌫", "±", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "Theme"]
]

buttons_list = []

# Create buttons dynamically
for i in range(5):
    for j in range(4):
        btn_text = buttons[i][j]
        btn = tk.Button(
            button_frame, text=btn_text, font=("Poppins", 18, "bold"),
            width=5, height=2, bd=0, bg=ORANGE, fg=BLACK, relief=tk.RAISED,
            activebackground=DARK_ORANGE, activeforeground=WHITE
        )
        btn.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")
        
        # Save buttons for theme switching
        buttons_list.append(btn)

        if btn_text == "Theme":
            btn.config(command=toggle_theme)
        else:
            btn.bind("<Button-1>", click)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

# Keyboard binding
root.bind("<Key>", key_input)

# Grid row-column expand
for i in range(5):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)

root.mainloop()
