#!/usr/bin/python3
''' Log parsing '''

import re
import sys
import signal


count = 0
total = 0
status_code = {'200': 0, '301': 0, '400': 0,
               '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}


def print_stats(signum=None, frame=None) -> None:
    print('File size: {}'.format(total))
    for code in status_code:
        if status_code[code] != 0:
            print('{}: {}'.format(code, status_code[code]))


signal.signal(signal.SIGINT, print_stats)

log_pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 '
    r'HTTP/1\.1" (\d{3}) (\d+)$'
)

for line in sys.stdin:
    count += 1
    line = line.strip()
    parsed_line = line.split()

    match = log_pattern.match(line)
    if match:
        size = int(parsed_line[8])
        total += size
        code = parsed_line[7]
        status_code[code] += 1

    if count == 10:
        print_stats()
        count = 0

print_stats()
