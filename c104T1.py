import csv
with open('SOCR-HeightWeight.csv') as f:
    read = csv.reader(f)
    fileData = list(read)

fileData.pop(0)

newData = []
for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))
n = len(newData)
print(n)
total = 0
for x in newData:
    total += x
mean = total/n
print('avrage', mean)
newData.sort()
if n % 2 == 0:
    m1=float(newData[n//2])
    m2=float(newData[n//2-1])
    meadian = (m1+m2)/2
else:
    meadian= newData[n//2]
print('med schol',meadian)
