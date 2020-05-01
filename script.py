#!/usr/bin/python3

import os, sys

def shutdown():  
	shutdown = input("Do you wish to shutdown your computer ? (Y / N): ") 

	if shutdown == 'N': 
		exit()
	else: 
		os.system("shutdown /s /t 1")

def restart():
	restart = input("Do you wish to restart your computer ? (Y / N): ") 

	if restart == 'N': 
		exit()
	else: 
		os.system("shutdown /r /t 1")

def logout():
	logout = input("Do you wish to logout your computer ? (Y / N): ") 
	
	if logout == 'N': 
		exit()
	else: 
		os.system("shutdown -l")

if __name__ == "__main__":
	globals()[sys.argv[1]]()
