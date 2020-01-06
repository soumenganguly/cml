'''
This file takes as an input an excel file and coverts it into a CSV file. 
The structure of the file is also made compatible for doing Exploratory Data Analyis.
'''

import sys 
import pandas as pd
import xlrd

# Pass the filename as an argument 
input_file = sys.argv[1]
#input_file = '../dataset/Dataset_completed _final_shashwat.xlsx'

# Convert the file to a pandas dataframe
df = pd.read_excel(input_file)

# Alter the header information
df.columns = [x for x in df.iloc[0]]
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
df.columns = df.columns.str.strip().str.lower().str.replace('\'', '_')
df.columns = df.columns.str.strip().str.lower().str.replace('(','_')
df.columns = df.columns.str.strip().str.lower().str.replace(')','_')

# Drop the duplicate header info
df = df.drop([0])

# Convert the modified dataframe to a csv file
df.to_csv('final_dataset.csv')
