#!/usr/bin/python3
'''Script that reads stdin line by line and computes HTTP log metrics.

This script parses HTTP request logs and computes metrics
including total file size and count of different HTTP status codes.
It prints statistics every 10 lines and/or when interrupted by CTRL+C.

'''
import re


def extract_input(input_line):
    '''Extracts and validates components from a line of HTTP request log.

    Args:
        input_line (str): A line from the HTTP request log.

    Returns:
        dict: A dictionary containing:
            - status_code (str): The HTTP status code from the log line
            - file_size (int): The file size from the log line
            Returns default values (status_code: 0, file_size: 0).
    '''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated HTTP request log statistics.

    Args:
        total_file_size (int): The cumulative sum of all file sizes processed
        status_codes_stats (dict): Dictionary containing
        counts of HTTP status codes

    Format:
        File size: <total size>
        <status code>: <number>
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates metrics based on the processed HTTP request log line.

    Args:
        line (str): The log line to process
        total_file_size (int): Current cumulative file size
        status_codes_stats (dict): Dictionary tracking status code counts

    Returns:
        int: Updated total file size after processing the current line

    Note:
        Only updates status code counts for valid codes
        (200, 301, 400, 401, 403, 404, 405, 500)
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Starts the HTTP log parser.

    Continuously reads from stdin line by line and computes metrics:
    - Tracks total file size
    - Counts occurrences of HTTP status codes
    - Prints statistics every 10 lines
    - Handles keyboard interruption (CTRL + C)
    - Prints final statistics before exiting
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
