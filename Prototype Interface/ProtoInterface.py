import tkinter

gui = tkinter.Tk()
gui.geometry("600x600")
gui.configure(bg="black")

bg_image = tkinter.PhotoImage(file="600x600.png")
bg_label = tkinter.Label(gui, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


gui.mainloop()
