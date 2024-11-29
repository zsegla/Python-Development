import time
import os
import pandas
while True: 
    if os.path.exists("python.txt"):
            data = pandas.read_csv("python.txt")
            print(data.mean()["st1"]) 
    else:
        print("File does not exist") 