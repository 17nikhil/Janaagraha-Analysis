import csv

data = []
with open("land_values.csv", 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
 		data.append(row)

#print(data[0])
#print(data[1])
Data = []
Data.append(data[0])
for i in range(1, len(data)):
	if data[i][0] == 'Potholes':
		Data.append(data[i])

TempData = Data[1:]
TempData = sorted(Data, key = lambda x: x[1])
Data[1:] = TempData
with open("potholesData.csv", 'wb') as F:
	writer = csv.writer(F)
	for i in range(len(Data)):
		writer.writerow(Data[i])
		
tempData = Data[1:] 
i = 0
newData = []
while i < len(tempData):
	areaName = tempData[i][1]
	freq = 1
	while i < len(tempData)-1 and tempData[i][1] == tempData[i+1][1]:
		freq += 1
		i += 1
	newData.append([areaName, freq])
	i += 1


with open("potholeFrequency.csv", 'wb') as F:
	writer = csv.writer(F)
	writer.writerow(["AreaName", "Frequency"])
	for i in range(len(newData)):
		writer.writerow(newData[i])


