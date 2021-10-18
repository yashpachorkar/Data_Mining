# Question 4
import pandas as pd
import os
import glob
import csv

question_read = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 1\EdNet-Contents\contents\questions.csv')

path = "C:\AnnacondaProjects\Anna Projects\Homework 1\Home_Work_4"
csv_files = glob.glob(os.path.join(path,"*.csv"))

with open(r'C:\AnnacondaProjects\Anna Projects\Homework 1\question4.csv', mode='w') as question4_file:
    
    writer = csv.writer(question4_file);
    writer.writerow(['user_name','played_video', 'question_answered']);
    
    for f in csv_files:
        question_count = 0;
        video_count = 0;
        

        user_read = pd.read_csv(f)
        for i in range(len(user_read)):
            if(user_read.iloc[i][2].startswith('l')):
                if(user_read.iloc[i][1]=='play_video'):
                    video_count += 1
            if(user_read.iloc[i][2].startswith('q')):
                question_count += 1
    

        writer.writerow([os.path.basename(f), video_count, question_count])
