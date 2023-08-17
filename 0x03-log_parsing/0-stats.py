#!/usr/bin/python3
""" This module parses a log (or log file) and returns data from the lines """
import re
import sys


# def sigint_handler(signal, frame):
#     """ Handles C-c signal from stdin """
#     log(message)
#     sys.exit(0)


def log(message: dict) -> None:
    """ Logs the status to the screen """

    for key, value in message.items():
        if value != 0:
            print(f"{key}: {value}")


def processor(counter):
    """ Runs the program to log parse"""

    try:
        for line in sys.stdin:
            if counter == 10:
                log(message)
                counter = 0
            line = line.strip()
            valid = re.match(regEX, line)
            counter += 1
            if not valid:
                continue
            valid = regEX.search(line)
            res = list(valid.groups())
            message["File size"] += int(res[-1])
            message[int(res[-2])] += 1
    except KeyboardInterrupt:
        log(message)
        # sys.exit(0)


if __name__ == "__main__":
    message = {
        "File size": 0, 200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0}
    counter = 0
    regEX = re.compile(r"""([0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]
\.[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9])\ \-\ \[([0-9]{4}\-[0-1]{1}
[0-9]{1}\-[0-3]{1}[0-9]{1}\ [0-2]{1}[0-9]{1}\:[0-5]{1}[0-9]{1}\:
[0-5]{1}[0-9]{1}\.[0-9]{6})\]\ (\"GET\ \/projects\/260\ HTTP\/1\.1\")
\ (200|301|400|401|403|404|405|500)\ ([1-9][0-9]*)""", re.X)
    processor(counter)
