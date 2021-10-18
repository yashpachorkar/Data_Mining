# Question 2 (c)
import pandas as pd
import csv
import os
import glob

path = "C:\AnnacondaProjects\Anna Projects\Homework 1\Home_Work_2_c"
question_read3 = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 1\EdNet-Contents\contents\questions.csv')
csv_files = glob.glob(os.path.join(path,"*.csv"))
with open(r'C:\AnnacondaProjects\Anna Projects\Homework 1\question2c.csv', mode='w') as question2c_file:
    writer = csv.writer(question2c_file);
    writer.writerow(['user_name','item_id', 'practice_count']);
    
    for f in csv_files:
        list = [];
        dict = {item_id:practice_count};

        user_read3 = pd.read_csv(f)

        for i in range(len(user_read3)):
            if(user_read3.iloc[i][2].startswith('q')):
                item_id=user_read3.iloc[i][2]
                practice_count = 0;
                if(item_id in list):
                    continue;
                else:
                    j = i + 1;
                    for j in range(len(user_read3)):
                            if(user_read3.iloc[i][2].startswith('q')):
                                if(item_id == user_read3.iloc[j][2]):
                                    practice_count += 1;
                    dict.update()
                list.append(item_id)
                writer.writerow([os.path.basename(f), item_id, practice_count])
