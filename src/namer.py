import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

directory_path = "C:/Users/simon/Downloads/test"

items = os.listdir(directory_path)

for item in items:
    full_path = os.path.join(directory_path, item)
    
    if os.path.isfile(full_path):
        
        filename, extension = os.path.splitext(item)
        
        new_filename = f"{filename}[Uni]{extension}"
        new_full_path = os.path.join(directory_path, new_filename)
        
        os.rename(full_path, new_full_path)
        
        print(f'Renamed {full_path} to {new_full_path}')
        