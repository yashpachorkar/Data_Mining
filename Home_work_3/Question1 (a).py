#Question 1 (a)
import pandas as pd
import matplotlib.pyplot as plt
faithful=pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 3\faithful.csv')
faithful.plot(kind ="scatter",
          x ='eruptions',
          y ='waiting')

plt.show()
