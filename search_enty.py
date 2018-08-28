import datetime
import csv
import re

class Search:
	def search(self, *args, **kwargs):
		result = []
		new_choice = input('How would you like to search?' 
			'\n 1 - Search By Date'
			'\n 2 - Search By Time Spent'
			'\n 3 - Search By Name'
			'\n 4 - Search By Regex Pattern \n \n')
		
		if new_choice == "1":
			date_given = input('\nWhat date would you like to search? MM/DD/YYYY \n \n')
			with open('Log.csv') as csvfile:
				csvreader = csv.DictReader(csvfile)
				for row in csvreader:
					if row['The Date'] == date_given:
						print("Task: {}".format(row['Task']),
							"Date: {}".format(row['The Date']),
							"Minutes Spent: {}".format(row['Minutes Spent']),
							"Notes: {}".format(row['Notes']))
		elif new_choice == "2":
			minutes_given = input('\nHow mant minutes were spent on task?\n \n')
			with open('Log.csv') as csvfile:
				csvreader = csv.DictReader(csvfile)
				for row in csvreader:
					if row['Minutes Spent'] == minutes_given:
						print(row)
		elif new_choice == "3":
			name_given = input('\nWhat is the name of the given task?\n \n')
			with open('Log.csv') as csvfile:
				csvreader = csv.DictReader(csvfile)
				for row in csvreader:
					if row['Task'] == name_given:
						print(row)
		elif new_choice == "4":
			search_given = input('\nWhat pattern would you like to use?\n \n')
			with open('Log.csv') as csvfile:
				csvreader = csv.DictReader(csvfile)
				for row in csvreader:
					if re.search(r''.format(search_given), row['Notes']):
						print(row)