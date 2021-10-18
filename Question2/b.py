# Question 2 (b)
import pandas as pd
import csv
import os
import glob

path = r"C:\AnnacondaProjects\Anna Projects\Homework 1\Home_Work_2_b"
csv_files = glob.glob(os.path.join(path,"*.csv"))

question_read2 = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 1\EdNet-Contents\contents\questions.csv')
# user_read2 = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 1\EdNet-KT4\KT4\u3.csv')
with open(r'C:\AnnacondaProjects\Anna Projects\Homework 1\question2b.csv', mode='w') as question2b_file:
    
    writer = csv.writer(question2b_file);
    writer.writerow(['user_name','item_id','question_type']);

    for f in csv_files:

        user_read2 = pd.read_csv(f)
        for i in range(len(question_read2)):
            for j in range(len(user_read2)):
                if(user_read2.iloc[j][2].startswith('q')):

                    if(user_read2.iloc[j][2] == question_read2.iloc[i][0]):

                        if(question_read2.iloc[i][4] <= 4 ):
                            writer.writerow([os.path.basename(f), question_read2.iloc[i][0], 'Learning_Comprehension']);

                        if(question_read2.iloc[i][4] >= 5):
                            writer.writerow([os.path.basename(f), question_read2.iloc[i][0], 'Reading_Comprehension']);
