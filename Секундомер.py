from tkinter import *
from datetime import datetime

temp = 0
after_id = ''

def tick():
    global temp,after_id
    after_id = root.after(1000,tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label1.configure(text=str(f_temp))
    temp += 1

def start_tick():
    btnStart.pack_forget()
    btnStop.pack()
    tick()


def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after_id)


def continue_tick():
    btnStop.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()

def reset_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')
    btnReset.pack_forget()
    btnStart.pack()

root = Tk()
root.title('Секундомер')
root.resizable(False,False)
root.geometry('400x200')

label1 = Label(root,width=10,font='Arial 20 bold',text='00:00')
label1.pack()

btnStart = Button(root,text='Start',font='Arial 15 bold',width=16,command=start_tick)
btnStop = Button(root,text='Stop',font='Arial 15 bold',width=16,command=stop_tick)
btnContinue = Button(root,text='Continue',font='Arial 15 bold',width=16,command=continue_tick)
btnReset= Button(root,text='Reset',font='Arial 15 bold',width=16,command=reset_tick)
btnStart.pack()

root.mainloop()