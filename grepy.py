#!/usr/bin/env python3

import sys
import os
import re
import termcolor

if __name__ == '__main__':
    pattern:str = sys.argv[1]
    file:str = os.path.abspath(sys.argv[2])

    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            data:list = f.readlines()

        for line in data:
            if re.search(pattern, line):
                print(termcolor.colored(line.strip(), 'blue'))
                print('')
            continue
