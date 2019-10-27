import csv

with open("All Data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count+=1
        else:
            print(f'Row {line_count}\t{row[0]} \t{row[1]} \t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}'
                  f'\t{row[8]}\t{row[9]}\t{row[10]}\t{row[11]}\t{row[12]}\t{row[13]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
    