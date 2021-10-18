# Question3  # Accuracy
import pandas as pd
import csv
import os
import glob

path = "C:\AnnacondaProjects\Anna Projects\Homework 1\Home_Work_3"
question_read = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 1\EdNet-Contents\contents\questions.csv')

csv_files = glob.glob(os.path.join(path,"*.csv"))

with open(r'C:\AnnacondaProjects\Anna Projects\Homework 1\question3.csv', mode='w') as question3_file:
    
    writer = csv.writer(question3_file);
    writer.writerow(['user_name','question_counting', 'correct_answer', 'accuracy']);

    for f in csv_files:
        question_counting = 0;
        correct_answer = 0;
        accuracy = 0;

        user_read = pd.read_csv(f)
        for i in range(len(user_read)):
            if(user_read.iloc[i][2].startswith('q')):
                question_counting += 1;

                for j in range(len(question_read)):
                    if(question_read.iloc[j][0]==user_read.iloc[i][2]):

                        if(question_read.iloc[j][3]==user_read.iloc[i][5]):
                            correct_answer += 1;
        
        accuracy = ((correct_answer)/(question_counting))
        writer.writerow([os.path.basename(f), question_counting, correct_answer, accuracy]);
