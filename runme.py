# jmiu CS4308

import json
import os
import Book

def cls():
	os.system('cls' if os.name=='nt' else 'clear')
	print('(c) 2017 Snep Corporation. All rights reserved.\n')


sneps = Book.Book('mow', 'sneps', 12)
print json.dumps(sneps.get_json())