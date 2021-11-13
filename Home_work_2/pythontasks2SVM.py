#SVM
from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

dataset = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\red_wine.csv')
X = dataset.iloc[:, 0:3].values
# print(X)
Y = dataset.iloc[:, 3:4].values
# print(Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)

classifier_predictions = clf.predict(X_test)
print("Accuracy",accuracy_score(y_test, classifier_predictions)*100)

#SVC Classifier
model = svm.SVC(probability=True)
model.fit(X_train,y_train)
predictions = model.predict_proba(X_test)

fpr1, tpr1, thresh1 = roc_curve(y_test, predictions[:,1], pos_label=1)

random_probs = [0 for i in range(len(y_test))]
p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)

auc_score1 = roc_auc_score(y_test, predictions[:,1])
print("AUC : ",auc_score1)
