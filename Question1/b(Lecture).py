# Question1 (b) # lectures watched(Best Version)
import pandas as pd
import csv
import os
import glob

path = r"C:\AnnacondaProjects\Anna Projects\Homework 1\Home_Work_1_b_Lecture"
csv_files = glob.glob(os.path.join(path,"*.csv"))

with open(r'C:\AnnacondaProjects\Anna Projects\Homework 1\question1blecture.csv', mode='w') as question1blecture_file:
    
    writer = csv.writer(question1blecture_file);
    writer.writerow(['username', 'lecture_counting_update']);
    for f in csv_files:
        lecture_counting_update = 0;

        user_read = pd.read_csv(f)
        for i in range(len(user_read)):
            if(user_read.iloc[i][2].startswith('l')):
                if(user_read.iloc[i][1] == 'enter'):
                    for j in range(i+1,len(user_read)):
                        if(user_read.iloc[j][1] == 'quit'):
                            lecture_counting_update += 1;
                            break

        writer.writerow([os.path.basename(f), lecture_counting_update]);
