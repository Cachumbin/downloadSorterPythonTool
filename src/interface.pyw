import ttkbootstrap as ttkb
import os
import file_checker as fc

items = os.listdir("C:/Users/simon/Downloads/test/")

display = fc.files_to_rename(items)

root = ttkb.Window(themename="solar")
root.title('File Organizer')
root.geometry('800x600')

root.mainloop()