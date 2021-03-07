import pandas as pd
import os
import csv
os.chdir("C:\\Users\\90596\\Desktop")
df = pd.read_csv('dict_file.csv', header=None)
df.iloc[:, [1]] = '"' + df.iloc[:, [1]]  + '"'
df.to_csv('list1.csv', index=False, header= None)
# Then add cloumn 3,4 of double quotes in excel by hand
# Get new list1.csv
# Then we only want to save it as txt tile with semicolon delimiter

df = pd.read_csv('list2.csv', header=None)
df.to_csv('list2.txt',index=False,header=False, quoting=csv.QUOTE_NONE, escapechar="\\", sep=";")


