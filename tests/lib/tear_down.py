#!/usr/bin/env python

import argparse

from lib.docker_tools import docker_compose
from lib.tools import show_status

def tear_down(version):
    dc = docker_compose(version)

    show_status('Stopping testing environment for PostgreSQL {version}...'.format(version=version))

    dc('down')

    show_status('Testing environment stopped')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set up testing environment.')
    parser.add_argument('version', help='PostgreSQL version')
    args = parser.parse_args()

    version = args.version
    tear_down(version)