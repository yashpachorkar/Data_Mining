# Question1 (b)  explanation read(Best Version)

import pandas as pd
import csv
import os
import glob

path = r"C:\AnnacondaProjects\Anna Projects\Homework 1\Home_Work_1_b_Explain"
csv_files = glob.glob(os.path.join(path,"*.csv"))

with open(r'C:\AnnacondaProjects\Anna Projects\Homework 1\question1bexplain.csv', mode='w') as question1bexplain_file:
    
    writer = csv.writer(question1bexplain_file);
    writer.writerow(['user_name','explain_counting_update']);

    for f in csv_files:
        explain_counting_update = 0;

        user_read = pd.read_csv(f)
        for i in range(len(user_read)):

            if(user_read.iloc[i][2].startswith('e')):
                if(user_read.iloc[i][1] == 'enter'):
                    for j in range(i+1,len(user_read)):
                         if(user_read.iloc[j][1] == 'quit'):
                            explain_counting_update += 1;
                            break

        writer.writerow([os.path.basename(f),explain_counting_update]);
