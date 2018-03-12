# jmiu CS4308

import json
import os
import Book


command = ''
commandList = ['add_book', 'remove_book',  'edit_book', 'print_books']
editsList = ['author', 'title',  'pages']
bookList = []

def cls():
	os.system('cls' if os.name=='nt' else 'clear')
	print('(c) 2017 Snep Corporation. All rights reserved.\n')

def add_book() :
	author = input('         author>')
	title  = input('          title>')
	pages  = input('number of pages>')

	if pages.isdigit() :
		bookList.append(Book.Book(author, title, int(pages)))
	else :
		print('error: number of pages not a number!')
	save_books()

def remove_book() :
	print_books()
	print()
	bookToRemove = input('index to remove>')
	#print(command)
	if bookToRemove.isdigit() and int(bookToRemove) < len(bookList) :
		bookList.pop(int(bookToRemove))
	save_books()

def edit_book() :
	print_books()
	print('\nwhat book would you like to edit? (please enter a number!)')
	bookToEdit = input('>')
	if not bookToEdit.isdigit() or int(bookToEdit) >= len(bookList) :
		print ('error: book was not a correct index!')
		return
	print()
	for i in range(len(editsList)) :
		print('[' + str(i) + ']' + editsList[i])
	print('\nwhat attribute would you like to edit?')
	attrToEdit = input('>')
	if attrToEdit.isdigit() and int(attrToEdit) < len(editsList) :
		attrToEdit = editsList[int(attrToEdit)]
	print()
	if attrToEdit in editsList :
		newValue = input('enter new value for ' + attrToEdit + '>')
		getattr(Book.Book, 'set_' + attrToEdit)(bookList[int(bookToEdit)], newValue)
		save_books()
	else :
		print ('error: attrToEdit not in edits list!')	

def print_books() :
	for i in range(len(bookList)) :
		print('[' + str(i) + ']' + str(bookList[i]))

def save_books() :
	with open('booklist.txt', 'w') as outfile :
		for i in range(len(bookList)) :
			json.dump(bookList[i].toJSON(), outfile)
			outfile.write('\n')

def load_books() :
	with open('booklist.txt') as infile:
		for line in infile :
			book = json.loads(line)
			bookList.append(Book.Book(book['author'], book['title'], book['pages']))

def take_input() :	
	print()
	for i in range(len(commandList)) :
		print('[' + str(i) + ']' + commandList[i])
	print('\nenter your command below or enter a number from the list.')
	command = input('>')
	if command.isdigit() and int(command) < len(commandList) :
		command = commandList[int(command)]
	print()
	if command in commandList :
		globals()[command]()
	else :
		print ('error: command not in command list!')

#startup()
load_books()
while True:
	take_input()
#




























