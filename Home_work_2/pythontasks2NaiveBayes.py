# Naive Bayes
import pandas
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score


def import_data():
    # import total dataset
    dataset = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\red_wine.csv')
    
    # get a list of column names
    headers = list(dataset.columns.values)
    
    # separate into independent and dependent variables
    x = dataset[headers[:-1]]
    y = dataset[headers[-1:]].values.ravel()

    return x, y

if __name__ == '__main__':
    # get training and testing sets
    x, y = import_data()

    # set to 10 folds
    skf = StratifiedKFold(n_splits=10)

    # blank lists to store predicted values and actual values
    predicted_y = []
    expected_y = []
    acc_score = []
    # partition data
    for train_index, test_index in skf.split(x, y):
        # specific ".loc" syntax for working with dataframes
        x_train, x_test = x.loc[train_index], x.loc[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # create and fit classifier
        classifier = GaussianNB()
        classifier.fit(x_train, y_train)

        # store result from classification
        predicted_y.extend(classifier.predict(x_test))

        # store expected result for this specific fold
        expected_y.extend(y_test)

    # save and print accuracy
        acc = metrics.accuracy_score(expected_y, predicted_y)
        acc_score.append(acc)
        
    avg_acc_score = sum(acc_score)/10*100
 
    
    print('accuracy of each fold - {}'.format(acc_score))
    print('Avg accuracy : {}'.format(avg_acc_score))
    
    #NaiveBays
    model = GaussianNB()
    model.fit(x_train,y_train)
    predictions = model.predict_proba(x_test)

    fpr1, tpr1, thresh1 = roc_curve(y_test, predictions[:,1], pos_label=1)

    random_probs = [0 for i in range(len(y_test))]
    p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)

    auc_score1 = roc_auc_score(y_test, predictions[:,1])
    print("AUC : ",auc_score1)
    
    
    
    /
    ***********************************************************************************************************************************************************************
    /
    
    # Naive Bayes
import pandas
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score


def import_data():
    # import total dataset
    dataset = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 2\white_wine.csv')
    
    # get a list of column names
    headers = list(dataset.columns.values)
    
    # separate into independent and dependent variables
    x = dataset[headers[:-1]]
    y = dataset[headers[-1:]].values.ravel()

    return x, y

if __name__ == '__main__':
    # get training and testing sets
    x, y = import_data()

    # set to 10 folds
    skf = StratifiedKFold(n_splits=10)

    # blank lists to store predicted values and actual values
    predicted_y = []
    expected_y = []
    acc_score = []
    # partition data
    for train_index, test_index in skf.split(x, y):
        # specific ".loc" syntax for working with dataframes
        x_train, x_test = x.loc[train_index], x.loc[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # create and fit classifier
        classifier = GaussianNB()
        classifier.fit(x_train, y_train)

        # store result from classification
        predicted_y.extend(classifier.predict(x_test))

        # store expected result for this specific fold
        expected_y.extend(y_test)

    # save and print accuracy
        acc = metrics.accuracy_score(expected_y, predicted_y)
        acc_score.append(acc)
        
    avg_acc_score = sum(acc_score)/10*100
 
    
    print('accuracy of each fold - {}'.format(acc_score))
    print('Avg accuracy : {}'.format(avg_acc_score))
    
    #NaiveBays
    model = GaussianNB()
    model.fit(x_train,y_train)
    predictions = model.predict_proba(x_test)

    fpr1, tpr1, thresh1 = roc_curve(y_test, predictions[:,1], pos_label=1)

    random_probs = [0 for i in range(len(y_test))]
    p_fpr, p_tpr, _ = roc_curve(y_test, random_probs, pos_label=1)

    auc_score1 = roc_auc_score(y_test, predictions[:,1])
    print("AUC : ",auc_score1)
