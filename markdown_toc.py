#!/usr/bin/python

#
# File: markdown_toc.py
# Desc: Creates 'Table of Contents' for a Markdown file.
# Author: Aravindhan Dhanasekaran
#

import argparse

MAX_HEADERS = 6
HORIZONTAL_LINE = '---'

parser = argparse.ArgumentParser(description=
    'Create a \'Table of Contents\' for a Markdown file.')
parser.add_argument('filename', type=str, help='name of the Markdown file')
parser.add_argument('-d', '--depth', metavar='D', type=int, action='store',
    default=0, help='depth of headers to include')

args = parser.parse_args()
filename = args.filename
depth = MAX_HEADERS if args.depth is 0 else args.depth

headers = ()
for i in xrange(1, depth + 1):
    headers += ('#' * i + ' '),

toc = []
code_block = False
with open(filename) as f:
    for each_line in f:
        each_line = each_line.rstrip('\n')

        if code_block is False and '```' in each_line:
            code_block = True
            continue

        if code_block is True and '```' in each_line:
            code_block = False

        if code_block is False and each_line.startswith(headers):
            toc.append(each_line)

indent = '  '
tmp_indent = ''
header_index = 1
tmp_index = 0

print 'Table of Contents'
for item in toc:
    tmp_index = item.index(' ')
    if tmp_index > header_index:
        tmp_indent = indent * tmp_index
    item_text = item.lstrip('# ')
    item_link = item_text.lower().replace(' ', '-')
    print '%s * [%s](#%s)' % (tmp_indent, item_text, item_link)

print '\n%s\n' % (HORIZONTAL_LINE)
