# Importing the os module
import os
import time

# Give the directory you wish to iterate through
my_dir = "D:/AutomationTest/POM/testCases"
# Using os.listdir to create a list of all of the files in dir
dir_list = os.listdir(my_dir)

# Use the for loop to iterate through the list you just created, and open the files
for f in dir_list:
   if f != "runTestCases.py" and f !="Test.py":
      print("Testing file: "+f)
      os.system("python -m unittest "+f)
