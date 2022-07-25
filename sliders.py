from tkinter import *

root = Tk()
root.title('Slider Application')
# root.iconbitmap('apple.ico')
# root.geometry('500 * 500')

vertical_slider = Scale(root, from_=0, to=250, orient=VERTICAL)
vertical_slider.pack(anchor='w')

horizontal_slider = Scale(root, from_=0, to=250, orient=HORIZONTAL)
horizontal_slider.pack(anchor='w')

def slider():
    ver_label = Label(root, text=vertical_slider.get()).pack()
    horizontal_label = Label(root, text=horizontal_slider.get()).pack()

ver_button = Button(root, text="CLICK FOR VALUES!", command=slider)
ver_button.pack()

root.mainloop()