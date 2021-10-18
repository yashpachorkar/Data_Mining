# Question 2 (a)
import pandas as pd
import csv
import os
import glob

path = r"C:\AnnacondaProjects\Anna Projects\Homework 1\Home_Work_2_a"
question_read = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 1\EdNet-Contents\contents\questions.csv')
csv_files = glob.glob(os.path.join(path,"*.csv"))

with open(r'C:\AnnacondaProjects\Anna Projects\Homework 1\question2a.csv', mode='w') as question2a_file:
    
    writer = csv.writer(question2a_file);
    writer.writerow(['user_name','item_id']);

    for f in csv_files:

        user_read = pd.read_csv(f)

        for i in range(len(question_read)):

            for j in range(len(user_read)):

                if(user_read.iloc[j][1] == 'respond'):

                    a = question_read.iloc[i][0];
                    b = user_read.iloc[j][2];

                    if(a==b):
                        writer.writerow([os.path.basename(f), a]);                            
