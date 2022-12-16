#!/usr/bin/env python

import argparse
import os
import sys
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--recursive', help='remove directories and their contents recursively', action='store_true')
parser.add_argument('path', type=str, nargs='*', help='objects to delete')

args = parser.parse_args()


for elem in args.path:
	if os.path.isfile(elem):
		os.remove(elem)
	elif os.path.isdir(elem) and args.recursive:
		shutil.rmtree(elem, ignore_errors=True)
	elif os.path.isdir(elem) and not args.recursive:
		print(f'rm: cannot remove {elem}: Is a directory')