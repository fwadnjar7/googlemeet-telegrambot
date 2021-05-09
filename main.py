from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dependencies import *
from time import sleep
import time
import sys

argLen = len(sys.argv)

if argLen == 1:
	print(text2art("Google Meet Bot", font = "small"))
	classNow = 'TEST'
	driver = loadDriver()
	joinClass(classNow, driver)
	print('Left ' + classNow + ' class')
	driver.quit()


	'''
	dateAndTime = datetime.now()
	day = dateAndTime.day
	noClasses = False
	for holidayDate in holidayList:
		if day == holidayDate:
			console.print('No classes today due to '+ holidaysDict[holidayDate], style = "bold red")
			console.print('[bold][green]' + 'Done\n')
			noClasses = True


	if not noClasses:

		classNow = whichClass()

		
		else :
			driver = loadDriver()
			totalClassesToday = len(findClasses())
			usedPrintInSameLine = False

			for i in range(totalClassesToday):
				if usedPrintInSameLine:
					printInSameLine(newLine = True)
				classNow = whichClass()
				if(classNow == None) :
					print('No ongoing classes at the moment')
				while True:
					if(classNow == None) :
						printInSameLine(str1 = 'Waiting for Todays link'. Trying again in ', str2 = ' seconds', isChar = False, seconds = True, sleepTime = 30)
						usedPrintInSameLine = True
						#time.sleep(30)
					else :
						break
					classNow = whichClass()
				if usedPrintInSameLine:
					printInSameLine(newLine = True)
				print(classNow + ' is going on at the moment')
				print('Trying to join ' + classNow + ' class')
				joinClass(classNow, driver)
				print('Left ' + classNow + ' class')

	'''

elif argLen == 2:
	arg = sys.argv[1].lower()

	if arg == '--t':
		print(text2art("Time Table", font = "small"))
		classesToday()
		#print(whichClass())

	elif arg == '--h':
		holidaysList()
		data = fetchDataFromJSON('log.json')
		print(data["holidaysList"])

	else :
		print('Wrong argument ', arg)

elif arglen == 3:
	arg1 = sys.argv[1].lower()
	arg2 = sys.argv[2].lower()

	if arg1 == '--h' and arg2 == '-u':
		date, occasion = input("Enter holiday and occasion: ").split()
		holidaysList(date, occasion)
		data = fetchDataFromJSON('log.json')
		print(data["holidaysList"])

	else :
		print('Wrong argument ', option)

			

	