import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

data_file = os.path.join("data","attendance.json")
students = {}

def load_stuff():
    global students
    if not os.path.exists(data_file):
        students = {}
        return

    try:
        with open(data_file, 'r') as f:
            stuff = json.load(f)
            for name, parameter in stuff.items():
                if type(parameter) == int:
                    students[name] = {'present': parameter, 'absent': 0}
                else:
                    students[name] = parameter
    except:
        students = {}

def save_stuff():
    try:
        with open(data_file, 'w') as f:
            json.dump(students, f)
        messagebox.showinfo("Done", "Saved!")
    except:
        messagebox.showerror("Oops", "Couldn't save")

def update_list():
    for idx in tree.get_children():
        tree.delete(idx)

    for name, data in sorted(students.items()):
        p = data.get('present', 0)
        a = data.get('absent', 0)
        tree.insert("", "end", values=(name, p, a))

def add_kid():
    def do_add():
        name = entry.get().strip()
        if not name:
            return
        if name in students:
            messagebox.showwarning("Hey", "Already got that one")
            return

        students[name] = {'present': 0, 'absent': 0}
        update_list()
        top.destroy()

    top = tk.Toplevel(root)
    top.title("New Student")
    top.geometry("200x100")

    tk.Label(top, text="Name:").pack()
    entry = tk.Entry(top)
    entry.pack(pady=5)
    entry.focus()

    tk.Button(top, text="Add", command=do_add).pack()

def mark_it():
    if not students:
        messagebox.showinfo("Wait", "No students yet")
        return

    def do_mark():
        kid = box.get()
        if radio_val.get() == 1:
            students[kid]['present'] += 1
        else:
            students[kid]['absent'] += 1
        update_list()
        top2.destroy()

    top2 = tk.Toplevel(root)
    top2.title("Mark")
    top2.geometry("250x150")

    tk.Label(top2, text="Pick student:").pack()
    box = ttk.Combobox(top2, values=list(students.keys()), state="readonly")
    box.pack(pady=5)
    box.set(list(students.keys())[0])

    radio_val = tk.IntVar(value=1)
    tk.Radiobutton(top2, text="Present", variable=radio_val, value=1).pack()
    tk.Radiobutton(top2, text="Absent", variable=radio_val, value=0).pack()

    tk.Button(top2, text="OK", command=do_mark).pack(pady=10)

def quit_app():
    if messagebox.askyesno("Bye", "Save first?"):
        save_stuff()
    root.destroy()

root = tk.Tk()
root.title("Class Attendance")
root.geometry("500x350")

tk.Label(root, text="Attendance Manager", font=("Arial", 14)).pack(pady=10)

buttons = tk.Frame(root)
buttons.pack(pady=8)

tk.Button(buttons, text="Add", command=add_kid, width=8).pack(side=tk.LEFT, padx=4)
tk.Button(buttons, text="Mark", command=mark_it, width=8).pack(side=tk.LEFT, padx=4)
tk.Button(buttons, text="Save", command=save_stuff, width=8).pack(side=tk.LEFT, padx=4)

tree = ttk.Treeview(root, columns=("name", "Present", "out"), show="headings", height=12)
tree.heading("name", text="Student")
tree.heading("Present", text="Present")
tree.heading("out", text="Absent")
tree.column("name", width=200)
tree.column("Present", width=80)
tree.column("out", width=80)
tree.pack(pady=10, padx=15, fill='both', expand=True)

load_stuff()
update_list()
root.protocol("WM_DELETE_WINDOW", quit_app)
root.mainloop()