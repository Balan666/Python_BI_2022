#!/usr/bin/env python

import argparse
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--all', help='do not ignore entries starting with .', action='store_true')
parser.add_argument('path', type=str, nargs='*', default=[os.getcwd()])

args = parser.parse_args()

if args.all:
	for i in range(len(args.path)):
		if len(args.path)>1:
			sys.stdout.write(args.path[i]+':'+'\n')
		for object in os.listdir(path = args.path[i]):
			if os.path.isdir(object):
				sys.stdout.write(f"{bcolors.OKBLUE}\033[1m{str(object)}\033[0m{bcolors.ENDC}  ")
			elif os.access(object, os.X_OK):
				sys.stdout.write(f"{bcolors.OKGREEN}\033[1m{str(object)}\033[0m{bcolors.ENDC}  ")
			else:
				sys.stdout.write(str(object)+'  ')
		sys.stdout.write(f"{bcolors.OKBLUE}\033[1m{'.'+'  '+'..'}\033[0m{bcolors.ENDC}  ")
		sys.stdout.write('\n')

else:
	for i in range(len(args.path)):
		if len(args.path)>1:
			sys.stdout.write(args.path[i]+':'+'\n')
		for object in os.listdir(path = args.path[i]):
			if object[0]!='.':
				if os.path.isdir(object):
					sys.stdout.write(f"{bcolors.OKBLUE}\033[1m{str(object)}\033[0m{bcolors.ENDC}  ")
				elif os.access(object, os.X_OK):
					sys.stdout.write(f"{bcolors.OKGREEN}\033[1m{str(object)}\033[0m{bcolors.ENDC}  ")
				else:
					sys.stdout.write(str(object)+'  ')
			sys.stdout.write('\n')
		if len(args.path)==0:
			sys.stdout.write(os.listdir('.'))
