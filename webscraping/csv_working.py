import csv

#open file

data  = open("example.csv", encoding='utf-8')

#call csv reader

csv_data = csv.reader(data)

#reformat into python object
datalines = list(csv_data)
length = len(datalines)

for line in datalines[0:5]:
    print(line)
    

allemails = []
for line in datalines[1:15]:
    allemails.append(line[3])
    
    
print(allemails)


fullNames = []
for line in datalines[1:15]:
    fullNames.append(line[1]+' '+line[2])
    

print(fullNames)


filetooutput  = open("to_save_file.csv",mode='a',newline='')

csvwriter= csv.writer(filetooutput,delimiter=",")
   
csvwriter.writerow(['a','b','c']) 

csvwriter.writerows([['1','2','3'],['11','22','33']])
filetooutput.close()

data2 = open("to_save_file.csv", encoding='utf-8')

csv_data2 = csv.reader(data2)
print(list(csv_data2))