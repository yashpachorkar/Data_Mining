# One R
import numpy as np
from sklearn.model_selection import train_test_split
from mlxtend.classifier import OneRClassifier
datasetdf = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\red_wine.csv')
a = datasetdf[['citric acid','sulphates','alcohol']]
b = datasetdf['type'].astype('category').cat.codes
xa = np.array(a)
ya = np.array(b)

def get_feature_quartiles(X):
    X_discretized = X.copy()
    for col in range(X.shape[1]):
        for q, class_label in zip([1.0, 0.75, 0.5, 0.25], [3, 2, 1, 0]):
            threshold = np.quantile(X[:, col], q=q)
            X_discretized[X[:, col] <= threshold, col] = class_label
    return X_discretized.astype(np.int)

X = get_feature_quartiles(xa)
X_train, X_test, y_train, y_test = train_test_split(X, ya, random_state=1, stratify=ya)

oner = OneRClassifier()
oner.fit(X_train, y_train);
oner.feature_idx_
oner.prediction_dict_
oner.predict(X_train)

y_pred = oner.predict(X_train)
train_accuracy = np.mean(y_pred == y_train) 
test_accuracy = oner.score(X_test, y_test)
print(f'Training accuracy {train_accuracy*100:.2f}%')
print(f'Test accuracy {test_accuracy*100:.2f}%')
