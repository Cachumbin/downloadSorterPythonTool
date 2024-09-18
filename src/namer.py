import os
import sys
import io

categories = ["Uni", "Projects", "Personal", "Work", "Misc"]

directory_path = "C:/Users/simon/Downloads/test/"
file = "mockup_1[Uni].png"

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def rename_file(file_name: str, category: str):
    full_path = os.path.join(directory_path, file_name)
    if os.path.isfile(full_path):
        name, extension = os.path.splitext(file_name)
        new_name = f"{name}[{category}]{extension}"
        os.rename(full_path, os.path.join(directory_path, new_name))
        return
