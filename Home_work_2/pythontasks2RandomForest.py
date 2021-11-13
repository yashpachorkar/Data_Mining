# Red Wine
#Random Forest
import pandas as pd
import numpy as np
dataset = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\red_wine.csv')
X = dataset.iloc[:, 0:3].values
# print(X)
Y = dataset.iloc[:, 3:4].values
# print(Y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from sklearn.ensemble import RandomForestClassifier

regressor = RandomForestClassifier(max_features=3, n_estimators=1)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

from sklearn.metrics import accuracy_score


print("Accuracy",accuracy_score(y_test, y_pred)*100)

#Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train,y_train)
predictions = model.predict_proba(X_test)

fpr1, tpr1, thresh1 = roc_curve(y_test, predictions[:,1], pos_label=1)

random_probs = [0 for i in range(len(y_test))]
p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)

auc_score1 = roc_auc_score(y_test, predictions[:,1])
print(auc_score1)


/
****************************************************************************************************************************************************************************
/


#Random Forest
import pandas as pd
import numpy as np
dataset = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\white_wine.csv')
X = dataset.iloc[:, 0:3].values
# print(X)
Y = dataset.iloc[:, 3:4].values
# print(Y)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


from sklearn.ensemble import RandomForestClassifier

regressor = RandomForestClassifier(max_features=3, n_estimators=1)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

from sklearn.metrics import accuracy_score


print("Accuracy",accuracy_score(y_test, y_pred)*100)

#Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train,y_train)
predictions = model.predict_proba(X_test)

fpr1, tpr1, thresh1 = roc_curve(y_test, predictions[:,1], pos_label=1)

random_probs = [0 for i in range(len(y_test))]
p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)

auc_score1 = roc_auc_score(y_test, predictions[:,1])
print(auc_score1)




