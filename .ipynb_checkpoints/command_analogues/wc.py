#!/usr/bin/env python
import os
import sys

options = []
files = []
sizes = []
for elem in sys.argv[1:]:
	if elem[0]=='-':
		options.append(elem)
	else:
		files.append(elem)

for file in files:
	with open(file, 'r') as f:
		data = f.read()
		lines_count = len(data.split('\n'))-1
		words_count = len(data.split())
		byte_count = os.stat(file).st_size
	sizes.append([lines_count, words_count, byte_count, file])
total_w = 0
total_b = 0
total_l = 0
if len(files) > 1:
	for elem in sizes:
		total_l += elem[0]
		total_w += elem[1]
		total_b += elem[2]
	sizes.append([total_l, total_w, total_b, 'total'])
if len(options)==0 or set(options)=={'-l','-w','-c'}:
	for i in sizes:
		sys.stdout.write(f'{i[0]}    {i[1]}    {i[2]}    {i[3]}\n')
elif set(options)=={'-l','-w'}:
	for i in sizes:
		sys.stdout.write(f'{i[0]}    {i[1]}    {i[3]}\n')
elif len(options)==0 or set(options)=={'-l','-c'}:
	for i in sizes:
		sys.stdout.write(f'{i[0]}    {i[2]}    {i[3]}\n')

elif len(options)==0 or set(options)=={'-w','-c'}:
	for i in sizes:
		sys.stdout.write(f'{i[1]}    {i[2]}    {i[3]}\n')

elif len(options)==0 or set(options)=={'-l'}:
	for i in sizes:
		sys.stdout.write(f'{i[0]}    {i[3]}\n')
elif len(options)==0 or set(options)=={'-w'}:
	for i in sizes:
		sys.stdout.write(f'{i[1]}    {i[3]}\n')
elif len(options)==0 or set(options)=={'-c'}:
	for i in sizes:
		sys.stdout.write(f'{i[2]}    {i[3]}\n')