import csv
from collections import Counter
with open("heightweight.csv",newline="")as f :
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)

newdata=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    newdata.append(num)

data=Counter(newdata)
modedataforrange={ 
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occ in data.items():
    if(50<float(height)<60):
        modedataforrange["50-60"]+=occ

    elif (60<float(height)<70):
        modedataforrange["60-70"]+=occ
    elif(70<float(height)<80):
        modedataforrange["70-80"]+=occ

moderange,modeocc=0,0
for range,occ in modedataforrange.items():
    if(occ>modeocc):
        moderange,modeocc=[int(range.split("-")[0]),int(range.split("-")[1])],occ

mode=float((moderange[0]+moderange[1])/2)
print("mode is "+str(mode))







