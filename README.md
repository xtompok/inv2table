# inv2table
Place inventory labels into table

## Instalation
Needed programs: barcode, pdflatex + czech, epstopdf

Instalation in virtualenv:

	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

## Usage
	. venv/bin/activate
	./inv.py <file.txt>

Output is created in the current directory, named `file.pdf`.

## Syntax of txt file
	<Room name> - <room_id>
	<Item 1 name> - <Item 1 code> - <Item 1 placement>
	<Item 2 name> - <Item 2 code> - <Item 2 placement>
	...
	
