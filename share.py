import os,time,platform
device=platform.architecture()[0]
if "64bit" in device:
	os.system("clear")
	print("\033[7;92mYour device is 64bit\033[0m")
	time.sleep(2)
	os.system("./sharemorijah")
else:
	os.system("clear")
	print("\033[7;91mYour device is not supported for the moment\033[0m")
	time.sleep(2)
	exit()