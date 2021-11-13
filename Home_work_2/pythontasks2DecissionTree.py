# Decision Tree
# Red Wine
# Load libraries
import pandas as pd
import matplotlib as plt
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

dataset = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\red_wine.csv')


# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test



# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)



#Decision Tree

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
predictions = model.predict_proba(X_test)

fpr1, tpr1, thresh1 = roc_curve(y_test, predictions[:,1], pos_label=1)

random_probs = [0 for i in range(len(y_test))]
p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)

auc_score1 = roc_auc_score(y_test, predictions[:,1])
print("AUC : ",auc_score1)

/
***************************************************************************************************************************************************************
/


# White Wine

import pandas as pd
import matplotlib as plt
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

dataset = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\white_wine.csv')


# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test



# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)



#Decision Tree

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
predictions = model.predict_proba(X_test)

fpr1, tpr1, thresh1 = roc_curve(y_test, predictions[:,1], pos_label=1)

random_probs = [0 for i in range(len(y_test))]
p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)

auc_score1 = roc_auc_score(y_test, predictions[:,1])
print("AUC : ",auc_score1)
