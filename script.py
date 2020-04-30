import os 

def shutdown():  
	shutdown = input("Do you wish to shutdown your computer ? (Y / N): ") 

	if shutdown == 'N': 
		exit()
	else: 
		os.system("shutdown /s /t 1")

if __name__ == "__main__":
	shutdown()
