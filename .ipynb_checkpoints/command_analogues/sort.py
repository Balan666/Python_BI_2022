#!/usr/bin/env python

import argparse
import os
import sys
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, nargs='*', help='files to sort strings from')


args = parser.parse_args()

if len(args.path)>0:
	os.environ["LC_ALL"] = "en_US.UTF-8"
	proc = subprocess.Popen(["sort", *args.path], stdout=subprocess.PIPE)
	sort_en_utf = proc.stdout.read().decode('utf-8')
	print(sort_en_utf)
else:
	os.environ["LC_ALL"] = "en_US.UTF-8"
	proc = subprocess.Popen(["sort"], stdin=sys.stdin, stdout=subprocess.PIPE)
	sort_en_utf = proc.stdout.read().decode('utf-8')
	print(sort_en_utf)
