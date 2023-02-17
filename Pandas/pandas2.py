import pandas
 
csvFile = pandas.read_csv('/home/amals/Python_Training/Matplotlib/data.csv')

print(csvFile)
print(csvFile.head())
print(csvFile.head(3))
print(csvFile[['animal','uniq_id']])
print(csvFile[csvFile.animal=='zebra'])