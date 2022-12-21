import csv

data1 = []
data2 = []

with open("bright_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data1.append(row)

with open("dwarfs.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data2.append(row)

header1 = data1[0]
header2 = data2[0]

star_data1 = data1[1:]
star_data2 = data2[1:]

headers = header1 + header2
stars_data = []

for i in star_data1:
    stars_data.append(i)

for i in star_data2:
    stars_data.append(i)

with open("final_stars.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(stars_data)