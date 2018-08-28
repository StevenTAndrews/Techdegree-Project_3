import datetime
import csv
import re

class Search:
	def search(self, *args, **kwargs):
		new_choice = input('\nHow would you like to search?' 
			'\n 1 - Search By Date'
			'\n 2 - Search By Time Spent'
			'\n 3 - Search By Name'
			'\n 4 - Search By Regex Pattern \n \n')
		
		if new_choice == "1":
			date_given = input('\nWhat date would you like to search? MM/DD/YYYY \n \n')
			result = []
			empty = []
			with open('Log.csv') as csvfile:
				csvreader = csv.DictReader(csvfile)
				for row in csvreader:
					if row['The Date'] == date_given:
						result.append(row)
						print("Task: {}".format(row['Task']),
							"Date: {}".format(row['The Date']),
							"Minutes Spent: {}".format(row['Minutes Spent']),
							"Notes: {}".format(row['Notes']))
				if result == empty:
					print("No results found.")
		elif new_choice == "2":
			result = []
			empty = []
			minutes_given = input('\nHow mant minutes were spent on task?\n \n')
			with open('Log.csv') as csvfile:
				csvreader = csv.DictReader(csvfile)
				for row in csvreader:
					if row['Minutes Spent'] == minutes_given:
						result.append(row)
						print("Task: {}".format(row['Task']),
							"Date: {}".format(row['The Date']),
							"Minutes Spent: {}".format(row['Minutes Spent']),
							"Notes: {}".format(row['Notes']))
				if result == empty:
					print("No results found.")
					else:
						print('Sorry, no results found.')
		elif new_choice == "3":
			result = []
			empty = []
			name_given = input('\nWhat is the name of the given task?\n \n')
			with open('Log.csv') as csvfile:
				csvreader = csv.DictReader(csvfile)
				for row in csvreader:
					if row['Task'] == name_given:
						result.append(row)
						print("Task: {}".format(row['Task']),
							"Date: {}".format(row['The Date']),
							"Minutes Spent: {}".format(row['Minutes Spent']),
							"Notes: {}".format(row['Notes']))
				if result == empty:
					print("No results found.")
					else:
						print('Sorry, no results found.')
		elif new_choice == "4":
			result = []
			empty = []
			search_given = input('\nWhat pattern would you like to use?\n \n')
			with open('Log.csv') as csvfile:
				csvreader = csv.DictReader(csvfile)
				for row in csvreader:
					if re.search(r''.format(search_given), row['Notes']):
						result.append(row)
						print("Task: {}".format(row['Task']),
							"Date: {}".format(row['The Date']),
							"Minutes Spent: {}".format(row['Minutes Spent']),
							"Notes: {}".format(row['Notes']))
				if result == empty:
					print("No results found.")
					else:
						print('Sorry, no results found.')
		else:
			print("\nSorry {} was not a valid option.".format(new_choice))
			search = Search()
			search.search()
