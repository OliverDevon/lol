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
from collections import Counter
data=Counter(newData)
modeRange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height, occ in data.items():
    if 50 < float(height)< 60:
        modeRange['50-60']+=occ
    elif 60 < float(height)< 70:
        modeRange['60-70']+=occ
    elif 70 < float(height)< 80:
        modeRange['70-80']+=occ
mRange, mocc=0,0
for range, occ in modeRange.items():
    if occ > mocc:
        mRange, mocc = [int(range.split("-")[0]), int(range.split("-")[1])], occ
mode =float((mRange[0]+mRange[1])/ 2)
print(f"mode,,,,{mode:2f}")