import ttkbootstrap as ttkb
import os

items = os.listdir("C:/Users/simon/Downloads/test/")

root = ttkb.Window(themename="solar")
root.title('File Organizer')
root.geometry('800x600')

root.mainloop()