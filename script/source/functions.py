import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


def loadData(path):
    data = pd.read_csv (path, index_col=0)
    return data


def cleaningData(data, size):
    if size is None:
        data = data.sample (n=len (data))
    else:
        data = data.sample (n=size)
    data.reset_index (inplace=True)
    data.rename (columns={"index": "Id"}, inplace=True)
    return data


def splitData(data, target):
    y = data[[target]]
    x = data[[i for i in list (data.columns) if i != target]]
    x_train, x_test, y_train, y_test = train_test_split (x, y, test_size=0.35, random_state=42)
    x_train.loc[:, target] = y_train
    x_test.loc[:, target] = y_test
    test_students_columns = [col for col in x_test.columns if col != target]
    test_students = x_test[test_students_columns]
    test_solution_columns = [col for col in x_test.columns if (col == target or col == 'Id' or col == 'id')]
    test_solution = x_test[test_solution_columns]
    sample_submission = test_solution.copy ()
    sample_submission[target] = np.random.randint (y_train[target].min (), y_train[target].max (),
                                                   size=(len (test_solution), 1))
    return x_train, test_students, test_solution, sample_submission


def saveData(path, x_train, test_students, test_solution, sample_submission):
    x_train.to_csv (path + '/data_students.csv', index=False)
    test_students.to_csv (path + '/test_students.csv', index=False)
    test_solution.to_csv (path + '/test_solution.csv', index=False)
    sample_submission.to_csv (path + '/sample_submission.csv', index=False)
    return x_train, test_students, test_solution, sample_submission
