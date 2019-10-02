from functions import *
import argparse
import os
import warnings


def get_args() :  # add arguments to prepare the data
    parser = argparse.ArgumentParser (description="Name of the csv file")
    parser.add_argument ('-n', '--name', help="type the name of the csv file", type=str)
    parser.add_argument ('-t', '--target', help="type the name of the target column", type=str)
    parser.add_argument ('-s', '--size', help="If your data is too big, choose the number of records", type=int,
                         required=False)
    return parser.parse_args ()


def menu() :
    print ('''--------Introduce the name of the csv file, the target column------

    Format required:

    ------------- main.py -n "cars.csv" -t "price" -s 170000 ------------''')


def main() :
    menu ()
    warnings.filterwarnings ("ignore")
    args = get_args ()
    name, target, size = args.name, args.target, args.size
    print ("loading the dataset...")
    data = loadData ('./{}'.format (name))
    print ("cleaning the dataset...")
    data_clean = cleaningData (data, size)
    print ("splitting into train and test the dataset...")
    x_train, test_students, test_solution, sample_submission = splitData (data_clean, target)
    saveData (os.getcwd (), x_train, test_students, test_solution, sample_submission)


if __name__ == '__main__' :
    main ()
