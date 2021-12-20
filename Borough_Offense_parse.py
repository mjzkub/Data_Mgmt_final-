import csv 

with open('Arrests.csv', 'r') as csvfile:

    processed_csv = csv.reader(csvfile)

    #CSV is open and reading ready

    with open ('Queens_arrests.csv' , 'w') as csvout:

        writeable_csv = csv.writer(csvout)

        for row in processed_csv:

            if 'PROSTITUTION' in row[5] and row[8] == 'Q':
                writeable_csv.writerow(row)
