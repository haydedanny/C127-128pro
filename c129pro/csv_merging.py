import csv

dataset_1 = []
dataset_2 = []

with open("c127pro/stars.csv", "r", encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("c128pro/brown_dwarfs.csv", "r", encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

len_1 = len(planet_data_1)
len_2 = len(planet_data_2)
print(f"Length of planet_data_1: {len_1}") #98
print(f"Length of planet_data_2: {len_2}") #59

headers = headers_1 + headers_2
planet_data = []
for index in range(min(len_1, len_2)):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("c129pro/merged_dataset.csv", 'w', newline='', encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)