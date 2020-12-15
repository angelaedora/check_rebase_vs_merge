from tkinter import *
from tkinter.ttk import *


class TaskRow:
    def __init__(self, window):
        self.hourStartVal = StringVar()
        self.minStartVal = StringVar()
        self.hourEndVal = StringVar()
        self.minEndVal = StringVar()
        self.hrsVal = StringVar()
        self.taskVal = StringVar()
        self.checkVal = IntVar()

        self.window = window

        self.hourStart = Combobox(window, width=2, textvariable=self.hourStartVal)
        self.minuteStart = Combobox(window, width=2, textvariable=self.minStartVal)
        self.hourEnd = Combobox(window, width=2, textvariable=self.hourEndVal)
        self.minuteEnd = Combobox(window, width=2, textvariable=self.minEndVal)
        self.lblhrs = Label(window, width=5, relief=SUNKEN, textvariable=self.hrsVal)
        self.task = Entry(window, width=10, textvariable=self.taskVal)
        self.lock = Checkbutton(
            window, text="Save", variable=self.checkVal, onvalue=1, offvalue=0
        )

        self.hourStart["values"] = range(23)
        self.minuteStart["values"] = (0, 15, 30, 45)
        self.hourEnd["values"] = range(23)
        self.minuteEnd["values"] = (0, 15, 30, 45)

    def showRow(self, row):
        self.row = row
        self.hourStart.grid(row=row, sticky="NWS", column=0)
        self.minuteStart.grid(row=row, sticky="NWS", column=2)
        self.hourEnd.grid(row=row, sticky="NWS", column=4)
        self.minuteEnd.grid(row=row, sticky="NWS", column=6)
        self.lblhrs.grid(row=row, sticky="NWS", column=8)
        self.task.grid(row=row, sticky="NWS", column=10, ipadx=50)
        self.lock.grid(row=row, sticky="NWS", column=12)


window = Tk()

# Comment 12345, 6789, 101112
window.title("TaskTimeBreakdown App")
window.geometry("500x200")

# Some code here by merger
# Some code here by merger again

labelFrame = Frame(window, width=500, height=50)
labelFrame.pack(side=TOP)

lblTimeStart = Label(labelFrame, text="Start", font=("Arial Bold", 12))
lblTimeStart.grid(column=0, row=0)

lblTimeEnd = Label(labelFrame, text="End", font=("Arial Bold", 12))
lblTimeEnd.grid(column=2, row=0)

lblHours = Label(labelFrame, text="Hours", font=("Arial Bold", 12))
lblHours.grid(column=4, row=0)

lblTask = Label(labelFrame, text="Task", font=("Arial Bold", 12))
lblTask.grid(column=6, row=0)

lblLock = Label(labelFrame, text="Lock", font=("Arial Bold", 12))
lblLock.grid(column=8, row=0)

taskFrame = Frame(window, width=500, height=272.5)
taskFrame.pack()

# taskFrame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
# taskFrame.columnconfigure(5, weight=4)

task1 = TaskRow(taskFrame)
task1.showRow(1)

task2 = TaskRow(taskFrame)
task2.showRow(2)

window.mainloop()
