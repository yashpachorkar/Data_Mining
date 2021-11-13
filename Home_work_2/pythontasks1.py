# Python Task 1 Pandas Profiling

import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

profiledf = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\red_wine.csv')

profile = ProfileReport(profiledf)
profile
profile.to_notebook_iframe()

profile.to_file("yash.html")
