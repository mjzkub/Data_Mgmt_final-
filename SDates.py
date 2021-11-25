import csv 

with open('Staten_arrests.csv', 'r') as csvfile:

    processed_csv = csv.reader(csvfile)

    #CSV is open and reading ready

    with open ('S2021.csv' , 'w') as csvout:

        writeable_csv = csv.writer(csvout)

        for row in processed_csv:

            if '2021' in row[1]:
                writeable_csv.writerow(row)