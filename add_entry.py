import datetime
import csv
import os.path

class Add_Entry:
	def add(self):
		fmt = '%m/%d/%Y'
		if os.path.isfile('Log.csv'):
			with open('Log.csv', 'a') as csvfile:
				fieldnames = ['Task', 'The Date', 'Minutes Spent', 'Notes']
				logwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
				logwriter.writerow({
				'Task': input('What is the name of the task? \n \n'),
				'The Date': datetime.datetime.now().date().strftime(fmt),
				'Minutes Spent': input("\n How many minutes were spent on task? \n \n"),
				'Notes': input('\n Do you have any notes to add? If none, type "NA". \n \n'),
				})
			print('\nEntry has been added.')
		else:
			with open('Log.csv', 'a') as csvfile:
				fieldnames = ['Task', 'The Date', 'Minutes Spent', 'Notes']
				logwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
				logwriter.writeheader()
				logwriter.writerow({
				'Task': input('What is the name of the task? \n \n'),
                'The Date': datetime.datetime.now().date().strftime(fmt),
				'Minutes Spent': input("\n How many minutes were spent on task? \n \n"),
				'Notes': input('\n Do you have any notes to add? If none, type "NA". \n \n'),
				})
			print('\nEntry has been added.')