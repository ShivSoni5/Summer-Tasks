import csv

# Read
#with open('employee_birthday.txt') as csv_file:
with open('employee_file.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            print(row)
"""
# Write
with open('employee_file.csv', mode='w') as e_file:
#    employee_writer = csv.writer(e_file, delimiter=',')
    employee_writer = csv.writer(e_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
"""
