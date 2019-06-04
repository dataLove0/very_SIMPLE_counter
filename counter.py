import time

i = 0
while 1 > 0:
	time.sleep(1) # waits one second
	i += 1

	if i == 60:
		print(i / 60, "Minute passed.")

	elif i % 60 == 0:
		print(i / 60, "Minutes passed.")
	
	print(i) # prints out seconds
