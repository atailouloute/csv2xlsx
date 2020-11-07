import xlsxwriter
import argparse
import csv
import os
from tqdm import tqdm
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, help='The path of the CSV input file')
parser.add_argument('--output_file', required=True, help='The path of the XLSX output file')
parser.add_argument('--delimiter', default=',', help='The delimiter of the CSV file')
parser.add_argument('--override', default=False, type=bool,
                    help='Whether to override the output file if it exists or not')
parser.add_argument('--show_progress', default=False, type=bool, help='Whether to show the progressBar or not')
args = parser.parse_args()

if not os.path.exists(args.input_file) or not os.access(args.input_file, os.R_OK):
    raise Exception('Unable to find or read the input file')

if os.path.exists(args.output_file) and not args.override:
    raise Exception('The output file exists already, you forgot to add --override ?')


def file_len(file_name):
    p = subprocess.Popen(['wc', '-l', file_name], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])


def convert(input_file, output_file, delimiter, callable=None):
    workbook = xlsxwriter.Workbook(output_file, {'constant_memory': True})
    worksheet = workbook.add_worksheet()

    row_number = 0
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            col_number = 0
            for cell in row:
                worksheet.write(row_number, col_number, cell)
                col_number += 1
            row_number += 1
            if callable != None:
                callable()
    workbook.close()


if args.show_progress:
    number_of_lines = file_len(args.input_file)
    progressBar = tqdm(total=number_of_lines, unit=' line', desc='Converting ' + str(number_of_lines) + ' lines')
    convert(args.input_file, args.output_file, args.delimiter, lambda: progressBar.update(1))
    progressBar.close()
else:
    convert(args.input_file, args.output_file, args.delimiter)
