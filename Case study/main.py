import warnings
import pandas as pd
import numpy as np
import argparse
from clean_data import clean_data, prepare_data, yearSplit, manufacturerSplit
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import normalize

def main():
    warnings.filterwarnings('ignore')
    # Read Files
    train = pd.read_csv('../cars-competition/data/{}'.format(train_dir), index_col='Id')
    submission = pd.read_csv('../cars-competition/data/{}'.format(submission_dir), index_col='Id')
    # Clean Data
    print('Starting train data cleaning:')
    train = clean_data(train,columns)
    print('Starting test data cleaning:')
    submission = clean_data(submission,columns)
    # Prepare Data
    # columns = ['year','manufacturer','condition','cylinders','fuel','odometer','title_status','transmission','drive','size','lat','long']
    du = False
    categorical = ['manufacturer','fuel','transmission','drive','size']
    if any(col in categorical for col in columns):
        du = True
    X, y = prepare_data(train,columns,typ='train',dummies=du)
    X_sub, _ = prepare_data(submission,columns,typ='test',dummies=du)
    # Spliting Data
    # By Year
    if mode == '1':
        print('Spliting Train')
        X_dec,y_dec = yearSplit(X,y)
        print('Spliting Test')
        X_sub_dec,_ = yearSplit(X_sub)
    # By Manufacturer
    elif mode == '2':
        print('Spliting Train')
        X_dec, y_dec = yearSplit(X,y)
        print('Spliting Test')
        X_sub_dec, _ = yearSplit(X_sub)
    # Normalizing
    print('Normalizing columns')
    norm = [ col for col in columns if col in ['year','condition','cylinders','odometer']]
    for i, X in X_dec.items():
        X[norm] = normalize(X[norm])
    for i, X_sub in X_sub_dec.items():
        X_sub[norm] = normalize(X_sub[norm])
    # Feature reduction PCA
    pca_status = False
    if len(columns) > 5:
        pca_status = True
        print('Creating different PCA feature reductions')
        n_components = [i for i in range(5,len(columns,5))]
        X_new_dec = {}
        pca = {}
        for i, X in X_dec.items():
            new = {}
            pca_n = {}
            for n in n_components:
                try:
                    pca_n[n] = PCA(n_components = n)
                    X_new = pca_n[n].fit_transform(X)
                except:
                    pass
                new[n] = X_new
            X_new_dec[i] = new
            pca[i] = pca_n
    else:
        X_new_dec = X_dec
    # Split Train and Test data
    print('Spliting Train data')
    train_test_dec = {}
    for i, X_new in X_new_dec.items():
        X_train, X_test, y_train, y_test = train_test_split(X_new,y_dec[i],test_size=0.2,random_state=200)
        train_test_dec[i] = [X_train, X_test, y_train, y_test]
    # Linear Regression
    print('Training Linear Regressions')
    lin_reg_dec = {}
    for i, dic in train_test_dec.items():
        lin_reg_n = {}
        for j, [X_train, X_test, y_train, y_test] in dic.items():
            lin_reg = LinearRegression()
            lin_reg_n[j] = lin_reg.fit(X_train,y_train)
        lin_reg_dec[i] = lin_reg_n
    # Predict
    print('Evaluating Models')
    print('Checking Prediction')
    y_pred_dec = {}
    for i, dic in train_test_dec.items():
        y_pred_n = {}
        for j, [X_train, X_test, y_train, y_test] in dic.items():
            y_pred_n[j] = lin_reg_dec[i][j].predict(train_test_dec[i][j][1])
        y_pred_dec[i]=y_pred_n
    # Check error
    print('Checking Error')
    error = {}
    for i, dic in train_test_dec.items():
        err_n = {}
        for j, [X_train, X_test, y_train, y_test] in dic.items():
            err_n[j] = mean_squared_error(y_test, y_pred_dec[i][j])
        error[i]=err_n
    if pca_status == True:
        # Check for optimal feature number for PCA
        print('Checking for optimal PCA')
        pca_n = {i:sorted([x for x in dic.items()],key=lambda x: x[1])[0] for i,dic in error.items()}
        # Predict for test data
        print('Predicting for Test data')
        y_sub = {}
        for i, df in X_sub_dec.items():
            x = pca[i][pca_n[i]].transform(df)
            y_sub[i] = lin_reg_dec[i][pca_n[i]].predict(x)
    else:
        # Try optimal Linear Regression for submission
        print('Predicting for Test data')
        y_sub = {}
        for i, df in X_sub_dec.items():
            x = df.drop(columns=['manufacturer','title_status','transmission','size'])
            y_sub[i] = lin_reg_dec[i].predict(x)
    for i, df in X_sub_dec.items():
        df['price'] = abs(y_sub[i])
    y_sub = pd.concat(list(X_sub_dec.values()),axis=0)['price']
    y_sub.to_csv('../cars-competition/data/submission.csv', header=True, index=True)
    print('Submission file saved to cars-competition/data/submission.csv')
    print('End of program')
    
if __name__ == '__main__':
    train_dir = 'cars_train.csv'
    submission_dir = 'cars_test.csv'
    columns = ['year','manufacturer','condition','cylinders','fuel','odometer','title_status','transmission','drive','size','lat','long']
    print('Regression of car prices.\n')
    print('Current files to train and test model are:\n     {}\n     {}\n'.format(train_dir,submission_dir))
    dec = input('Do you wish to change them y/n?\n')
    if dec == 'y':
        train_dir = input('Type test file name: \n')
        submission_dir = input('Type test file name: \n')
    print('Columns available: {}\n'.format(columns))
    dec = input('Do you wish to change them y/n?\n')
    if dec == 'y':
        col = input('Type relevant columns (separated by comma, no spaces): \n')
        columns = col.split(',')
    mode = None
    while mode not in ['1','2']:
        mode = input('Which should we do?\n\n   1 - Year based regression\n   2 - Manufacturer based regression\n')
        if mode not in ['1','2']:
            print('\n\nTry again. Options are 1 or 2.\n')
    main()