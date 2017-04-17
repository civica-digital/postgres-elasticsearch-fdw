#!/usr/bin/env python

import argparse
import sys
import time

from lib.set_up import set_up
from lib.load_fixtures import load_fixtures
from lib.test import perform_tests
from lib.tear_down import tear_down
from lib.tools import show_status

def run_tests(version):
    print('Testing PostgreSQL {version}'.format(version=version))

    set_up(version)
    load_fixtures()

    time.sleep(10)

    success = perform_tests(version)

    tear_down(version)

    return success

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set up testing environment.')
    parser.add_argument('version', nargs='+', help='PostgreSQL version')
    args = parser.parse_args()

    result = all(list(run_tests(version) for version in args.version))
    show_status('PASS' if result else 'FAIL')
    print()

    sys.exit(0 if result else 1)
