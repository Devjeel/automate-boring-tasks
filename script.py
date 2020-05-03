#!/usr/bin/python3

import os, sys, getpass

def shutdown():  
	shutdown = input("Do you wish to shutdown your computer ? (Y / N): ") 

	if shutdown == 'N': 
		exit()
	else:
		if sys.platform == "win32": 
			os.system("shutdown /s /t 1")
		else:
			os.system("sudo shutdown now")

def restart():
	restart = input("Do you wish to restart your computer ? (Y / N): ") 

	if restart == 'N': 
		exit()
	else:
		if sys.platform == "win32": 
			os.system("shutdown /r /t 1")
		else:
			os.system("sudo reboot")


def logout():
	logout = input("Do you wish to logout your computer ? (Y / N): ") 
	
	if logout == 'N': 
		exit()
	else:
		if sys.platform == "win32": 
			os.system("shutdown -l")
		else:
			os.system("sudo pkill -KILL -u " + getpass.getuser())


if __name__ == "__main__":
	globals()[sys.argv[1]]()
