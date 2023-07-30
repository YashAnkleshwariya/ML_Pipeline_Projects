# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:14:49 2023

@author: ankle
"""

import pandas as pd
import os

def process_data():
    # Define the paths to your files
    train_path = "input/training.csv"
    test_path = "input/test.csv"

    # Read the csv files into pandas dataframes
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

    # Convert column names to lower case for train and test dataframes
    train_df.columns = map(str.lower, train_df.columns)
    test_df.columns = map(str.lower, test_df.columns)

    # Define the paths to the output files
    output_train_path = "temp/traing.csv"
    output_test_path = "temp/test.csv"

    # Make sure the output directories exist
    os.makedirs(os.path.dirname(output_train_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_test_path), exist_ok=True)

    # Save the dataframes to csv
    train_df.to_csv(output_train_path, index=False)
    test_df.to_csv(output_test_path, index=False)

if __name__ == "__main__":
       process_data()
