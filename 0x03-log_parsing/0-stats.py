#!/usr/bin/python3
"""Module that defines function stats
"""
import re
import signal
import sys


ip_reg = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
dt_reg = r'\[[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}(.[0-9]+)?\]'
code_reg = r'[0-9]{3}'
size_reg = r'[0-9]+'

log_reg = '^{} - {} "GET /projects/260 HTTP/1.1" {} {}$'.format(
        ip_reg, dt_reg, code_reg, size_reg
        )

status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
        '404': 0, '405': 0, '500': 0
        }

total_size = 0
line_num = 0


def print_stats(sig=None, frame=None):
    """Prints the stats"""
    print("File size: {}".format(total_size))
    for code, count in status_codes.items():
        if count > 0:
            print('{}: {}'.format(code, count))


signal.signal(signal.SIGINT, print_stats)

for line in sys.stdin:
    if line_num and line_num % 10 == 0:
        print_stats()

    log_legit = re.search(code_reg, line) or re.search(size_reg, line)

    if log_legit or re.search(log_reg, line):
        line_num += 1
        file_size = re.search(size_reg + '$', line)
        code_end_pos = (file_size.endpos - len(file_size.group())) - 2
        code_start_pos = code_end_pos - 3

        total_size += int(file_size.group())
        status_code = line[code_start_pos:code_end_pos]
        if status_code in status_codes:
            status_codes[status_code] += 1

if line_num == 0 or line_num % 10 != 0:
    print_stats()
