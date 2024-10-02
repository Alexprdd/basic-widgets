import tkinter as tk

window=tk.Tk()
window.title("Basic widgets")
window.geometry("1000x1000")
window.configure(bg="blue")

#labels
title=tk.Label(window, text="basic widgets-2")
#title.pack()
#title.place(x=10,y=10)
title.grid(row=0, column=0, columnspan=2)

#label1
l1=tk.Label(window, text="arial", font=("Helvetica", 20), bg="red", fg="white", width=10, height=2, bd=2, relief=tk.RAISED)
#l1.pack(pady=10, ipady=10,padx=5 ,side=tk.LEFT)
#l1.place(x=25,y=25)
l1.grid(row=1, column=0)

#button
b1=tk.Button(window,text="Press here",font=("Helvetica", 20), bg="red", fg="white",command=window.destroy, width=10, height=2, bd=4, relief=tk.FLAT)
#b1.pack(pady=10, ipady=10, padx=5 ,side=tk.RIGHT)
#b1.place(x=4,y=4)
b1.grid(row=1, column=1)

#entry
e1=tk.Entry(window,text="type...",font=("Times", 20), bg="white", fg="grey",justify=tk.CENTER ,width=10, bd=4, relief=tk.SUNKEN)
#e1.pack(pady=10, ipady=10, side=tk.BOTTOM)
#e1.place(x=346,y=599)
e1.grid(row=2, column=0)

window.mainloop()