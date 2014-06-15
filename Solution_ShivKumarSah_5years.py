#! /usr/bin/python 
# -*- encoding: ASCII -*-

# Author - Shiv Kumar Sah
# Date - 16 June 2014

# Company max share price calculation from CSV file

# Program takes CSV file as STDIN for data 

# Output 
# <company>:<year>:<march> 
 

import sys   # Sys for stdinp , stdout
import csv   # CSV parser


def read_csv_convert_tuples(input_csv=False):
    """ Read and convert to flat tuples """
    # Convert the datastructue into tuple list , 
    # e.g [(year, 1990, 1991), (month, jan, feb), (compA,10,20), (compB,20,30)] 
    if not input_csv:
        input_csv =  csv.reader(sys.stdin, delimiter=',', quoting=csv.QUOTE_NONE)
    else:
        input_csv = input_csv.strip().split('\n')
        input_csv = [i.split(',') for i in input_csv]
    flat_tuples = zip(*[map(lambda x: x.strip(),row) for row in input_csv])
    return flat_tuples 

def get_company_max_shares_time(flat_tuples):
    """ Use the flat tuple DS to get maximum share value and the corresponding
    time values """
    output = []
    for company_stats in flat_tuples[2:]:  # Company details start from 2nd ele
        share_values = list(map (int, company_stats[1:]))
        time_index =  share_values.index(max(share_values))
        # Find this time index in year and month tuple
        output.append(":".join([company_stats[0],flat_tuples[0][time_index+1], flat_tuples[1][time_index+1]]))
    output = '\n'.join(output)
    return output
 
def main(input_csv=False):  # Can take a input_csv importing modules
    try:
        flat_tuples = read_csv_convert_tuples(input_csv)
        return get_company_max_shares_time(flat_tuples)
    except: 
        return "[Critical]: Something wrong in CSV format. Plese verify."
    
if __name__ == "__main__":
   print main()           # Drive the startup
