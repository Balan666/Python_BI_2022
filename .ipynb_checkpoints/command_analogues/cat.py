#!/usr/bin/env python

import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('path', nargs='*', help='files to read', type=str)

args = parser.parse_args()

if len(args.path)==0 or args.path[0]=='-':
	while True:
		x=sys.stdin.readline()
		sys.stdout.write(x)
else:
	for object in args.path:
		if  os.path.isfile(object):
			with open(object) as file:
				for line in file.readlines():
					sys.stdout.write(line)
		elif os.path.isdir(object):
			print(f'cat: {object}: is a directory')
		elif not os.path.exists(object):
			print(f'cat: {object}: No such file or directory')