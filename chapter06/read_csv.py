from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')


dataFile = StringIO(data) # StringIO : in-memory buffer 라서 1번 호출되면 사라지는 휘발성 데이터

# CSV 타이틀 포함하여 list로 반환
csvFile = csv.reader(dataFile)
for row in csvFile:
     print("Title : %s / year, %s"%(row[0], row[1]))

print("========================================================")

# CSV 타이틀은 제외하고 dict 타입으로 변환
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
for row in dictReader:
    print("Title : %s / year, %s"%(row['Name'], row['Year']))