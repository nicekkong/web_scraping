import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("table", {"class" : "wikitable"})[1]
rows = table.findAll("tr")
csvFile = open("../editors.csv", "wt")
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            if cell.get_text() not in 'Enrico Tröger':
                print(cell.get_text())
                csvRow.append(cell.get_text())
        writer.writerow(csvRow)
except Exception as e:
    print('::::::::::::::::::::' + cell.__str__)
finally:
    csvFile.close()