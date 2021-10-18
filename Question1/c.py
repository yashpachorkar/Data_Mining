# Question 1 c
import pandas as pd
import csv
import os
import glob

path = r"C:\AnnacondaProjects\Anna Projects\Homework 1\Home_Work_1_c"
csv_files = glob.glob(os.path.join(path,"*.csv"))

for f in csv_files:
    user_read = pd.read_csv(f)
    user_read["hardworking"] = "Yes"
    user_read["mental_strength"] = "Good"
    user_read["problem_solving"] = "Great"
    print(user_read);
