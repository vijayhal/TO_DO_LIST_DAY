from tkinter import *
from tkinter import messagebox


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        # below code to clear the current entry
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "please enter task")


def deleteTask():
    lb.delete(ANCHOR)

window = Tk()
window.geometry('500x450+100+200')
window.title('TO DO LIST')
window.config(bg = '#223441')
window.resizable(width=False, height=False)


# creating frame box with left side with list of activity and right side with scroll bar.

frame = Frame(window)

frame.pack(pady = 10)

lb = Listbox(
    frame,
    width=30,height=10,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    selectbackground="#a6a6a6",
    activestyle="none"
)

lb.pack(side = LEFT, fill = BOTH)

task_list = [
    "Eat apple",
    "20 Push Ups",
    "20 Pull Ups",
    "Break",
    "Eat Eggs"
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    window, font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

addTask_btn = Button(button_frame,
                     text = 'Add Task',
                     font = ('times 14'),
                     bg ='#c5f776',
                     padx =20,
                     pady =10,
                     command = newTask)

addTask_btn.pack(fill=BOTH, expand=True, side = LEFT)

delTask_btn = Button(button_frame,
                     text = 'Delete Task',
                     font = ('times 14'),
                     bg ='#FF0000',
                     padx =20,
                     pady =10,
                     command = deleteTask)

delTask_btn.pack(fill=BOTH, expand=True, side = RIGHT)



window.mainloop()
