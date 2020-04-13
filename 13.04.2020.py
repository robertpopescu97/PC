
#Importare date CSV

import csv
with open("sdasda.txt ") as csv_file:
    csv_reader = csv.reader(csv_file,dellimiter = ';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        print(f'\t{row[0]} {row[1]} {row[2]}.')
        line_count +=1
        print(f' Processed {line_count} lines.')
        csv_file.close()


# Append new raw to CSV file
with open("text.csv", mode = "a") as csv_file_write: # daca nu pui nici un mod o sa se inteleaga de la sine ca modul o sa fie read
    csv_Write = csv.writer(csv_file_write, delimiter = ',')
    csv_Write.writerow([']5', 'gigi', 'florin'])