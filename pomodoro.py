import tkinter  as tk 
import winsound

t = 25 * 60
f = 5 * 60


duration = 1000  # milliseconds
freq = 440  # Hz

pomo = tk.Tk()
pomo.title('Pomodoro')
pomo.geometry("500x500")
pomo.configure(background='red')
pomo.resizable(False, False)




def crono():
    global t
    global f
    global timer
    mins = t // 60
    secs = t % 60

    fmins = f // 60
    fsecs = f % 60



    timer = '{:02d}:{:02d}'.format(mins, secs)
    ftimer = '{:02d}:{:02d}'.format(fmins, fsecs)

    

    if t > 0:
        msg.config(text=timer)
        t = t-1
        msg.after(1000, crono)
        if t == 0:
            winsound.Beep(freq, duration)
        

    else:
        if t == 0:
            
            msg5.config(text=ftimer)
            f = f-1
            msg5.after(1000,crono)
            if f == 0:
                winsound.Beep(freq, duration)
                crono_stop()


def crono_stop():
    global t
    
    t = 1500
    
   
    


msg1 = tk.Label(pomo,text='00:00', font=('times 20', 90), background='red' )
msg1.place(x=110, y=140)


msg = tk.Label(pomo, font=('times 20', 90), background='red' )
msg.place(x=110, y=140)

msg5 = tk.Label(pomo, font=('times 20', 90), background='red')
msg5.place(x=110, y=140)



b1 = tk.Button(pomo, text='START', width=20, command = crono)
b1.place(x=160, y = 350)

b2 = tk.Button(pomo, text='RESET', width=20, command = crono_stop)
b2.place(x=160, y = 400)




pomo.mainloop()
