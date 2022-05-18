import tkinter
gui = tkinter.Tk()
gui.geometry("400x400")
gui.configure(bg="black")




bg_image=tkinter.PhotoImage(file="b.png")
bg_label=tkinter.Label(gui,image=bg_image)
bg_label.place(relwidth=1,relheight=1)


pad_1 = tkinter.Button(gui, text="pad1", width=10, height=5)
pad_2 = tkinter.Button(gui, text="pad2", width=10, height=5)
pad_3 = tkinter.Button(gui, text="pad3", width=10, height=5)
pad_4 = tkinter.Button(gui, text="pad4", width=10, height=5)

pad_1.grid(row=0,column=0)
pad_2.grid(row=0,column=1)
pad_3.grid(row=0,column=2)
pad_4.grid(row=0,column=3)

gui.mainloop()
