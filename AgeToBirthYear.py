'''
read data from a csv file (List.csv (name,age)) and write a new csv file (ListOut.csv(name, born_year))
in command prompt> python AgeToBirthYear.py List.csv ListOut.csv
'''

import argparse
import csv

TEMPLATE_STRING = "{name},{year_born}"

def convert_age_in_csv(data_in, data_out):
    reader = csv.reader(data_in)
    writer = csv.writer(data_out)
    for row in reader:
        name = row[0].strip()
        age = int(row[1])
        year_born = 2017 - age
        writer.writerow([name, year_born])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_in')
    parser.add_argument('data_out')
    args = parser.parse_args()

    with open(args.data_in, 'r') as data_in:
        with open(args.data_out, 'w') as data_out:
            convert_age_in_csv(data_in, data_out)

if __name__ == '__main__':
    main()

