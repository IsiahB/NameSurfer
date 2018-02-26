#Name: Isiah Behner
#Assignment: Programming Assignment 6: Name Surfer
#Course/Semester: CS 343 - Fall 2017
#Instructor: Dr. Murphy
#Program Description: This program reads in data that contains 
#	name popularity over a certain span of years and allows the user
#	to search and view the rankings of certain names.
#Sources Consulted: Classmates

#!/usr/bin/python

#function to display options
def display():
	print("Choose one of the following: ")
	print("(1) Search")
	print("(2) Popularity Over Time")
	print("(3) Top Ten")
	print("(4) Quit")

#function to convert index to a year
def indexconverter(index):
	return 1900 + (index * 10)

#function to search for all names similar to the one given and
#print the names along with the most popular year for the name
def search():
	name = raw_input("Enter a name: ")
	name = name.capitalize()
	lilList = []
	top = 0
	x = 1 
	index = 0
	flag = False
	for k in names:
		if k.find(name) > -1:
			flag = True
			lilList = names[k]
			top = int(lilList[0])

			#setting top to a large number for comparsons 
			top = 10000

			#getting the smallest nonzero number
			for item in lilList:
				intItem = int(item)
				if intItem < top and intItem != 0:
					top = intItem

			#if the name has all 0's
			if top == 10000:
				top = 0

			index = lilList.index(str(top))

			#print the name with the most popular year
			print k, " ", indexconverter(index)
	if flag == False:
		print "name not found.."

#function that produces the rankings for the given name
def ranking():
	nam = raw_input("Enter a name: ")
	nam = nam.capitalize()
	yearArray = []
	flagg = False
	for k in names:
		if k == nam:
			yearArray = names[nam]
			print "1900   1910   1920   1930   1940   1950   1960   1970  1980  1990  2000  2010"
			print "--------------------------------------------------------------------------------"
		
			for y in yearArray:
				print y + "   ",

#function that produces the top10 names for the given year
def top10():
	year = raw_input("Enter a year: ")
	print "Most Popular Names for ", year
	print "-------------------------------------"

	year = (int(year) - 1900) / 10 #gets the index of that year
	ranks = []
	rank = 1
	while rank != 11:
		print rank, ". ",
		for key in names:
			ranks = names[key]
			if int(ranks[year]) == rank:
				print key, ", ",
		print "\n"
		rank = rank + 1

######### MAIN ######################################
names = {} #dictionary full of names and numbers
tokens = []
with open("names-data.txt") as f:
	num = int(f.readline()) #gets the total number of names
	for line in f:
		tokens = line.split()
		names[tokens[0]] = tokens[1:13]
f.close()

print(names["B"])

while True:
	display()
	answer = input("Choice: ")
	print("Your Choice: ", answer)

	if answer == 1:
		search()
	elif answer == 2:
		ranking()
	elif answer == 3:
		top10()
	elif answer == 4:
		break
	else:
		print "invalid input"



	
	