import csv
newdata = []
with open("heightweight.csv",newline="")as f :
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
for i in range(len(filedata)):
    num=filedata[i][1]   
    newdata.append(float(num))
n=len(newdata)
total=0
for x in newdata:
    total=total+x
mean=total/n
print(mean)
