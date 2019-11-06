#!/usr/bin/python3

import sys
import os
import subprocess
import datetime
from jinja2 import Environment, PackageLoader, select_autoescape


fname = sys.argv[1]
fprefix = fname.split(".")[0]

items = []
with open(fname) as f:
    (place,place_code) = tuple(map(str.strip,f.readline().split("-")))
    for line in f:
        items.append(tuple(map(str.strip,line.strip().split("-"))))


env = Environment(
        loader=PackageLoader('inv', 'templates'),
    	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
)

template = env.get_template('place.tex')

subprocess.call(["barcode","-E","-o",f"temp/place_bc.eps","-b",place_code,"-e","code93","-u","mm","-g","100x30"])
subprocess.call(["epstopdf",f"temp/place_bc.eps"])

for item in items:
    name = item[1].replace("/","_")
    subprocess.call(["barcode","-E","-o",f"temp/{name}.eps","-b",item[1],"-e","128","-u","mm","-g","100x30"])
    subprocess.call(["epstopdf",f"temp/{name}.eps"])

output = template.render(items=items, place=place)

with open(f"{fprefix}.tex","w") as f:
	f.write(output)

subprocess.call(["pdflatex",f"{fprefix}.tex"])
