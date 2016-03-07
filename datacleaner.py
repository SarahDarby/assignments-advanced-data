import csv

# Open our input and output files
csvfile = open('./cleanme.csv', 'r')
outfile = open('./cleanme-clean.csv', 'w')

# Now a DictReader and DictWriter
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

# Write headers
writer.writeheader()

# Clean and write the data to output
for row in reader:
    row['first_name'] = row['first_name'].upper()
    row['zip'] = row['zip'].zfill(5)
    row['city'] = row['city'].replace('&nbsp;',' ')
    if float(row['amount']) > 1000.0: 
        writer.writerow(row)











