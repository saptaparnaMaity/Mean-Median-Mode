import csv
with open("heightweight.csv",newline="")as f :
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)

newdata=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    newdata.append(num)

newdata.sort()
n=len(newdata)
if(n%2==0):
    num1=float(newdata[n//2])
    num2=float(newdata[n//2-1])
    median=(num1+num2)/2
else:
    median=newdata[n//2]

print("median is"+str(median))