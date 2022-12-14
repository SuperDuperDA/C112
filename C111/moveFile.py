import os
import shutil
from_dir = "C:/Users/dhyey/Downloads"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for list_of_files in list_of_files:
    root,extenstion = os.path.splitext(list_of_files)
    print("The root is: ",root)
    print("The extenstion is ",extenstion)