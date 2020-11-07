import xlsxwriter
import argparse
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, help='The path of the CSV input file')
parser.add_argument('--output_file', required=True, help='The path of the XLSX output file')
parser.add_argument('--delimiter', default=',', help='The delimiter of the CSV file')
parser.add_argument('--override', default=False, type=bool, help='Whether to override the output file if it exists or not')
args = parser.parse_args()

if not os.path.exists(args.input_file) or not os.access(args.input_file, os.R_OK):
    raise Exception('Unable to find or read the input file')

if os.path.exists(args.output_file) and not args.override:
    raise Exception('The output file exists already, you forgot to add --override ?')

workbook = xlsxwriter.Workbook(args.output_file, {'constant_memory': True})
worksheet = workbook.add_worksheet()
row_number = 0

with open(args.input_file, 'r') as file:
    reader = csv.reader(file, delimiter=args.delimiter)
    for row in reader:
        col_number = 0
        for cell in row:
            worksheet.write(row_number, col_number, cell)
            col_number += 1
        row_number += 1

workbook.close()