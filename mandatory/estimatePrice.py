import sys

def estimatePrice(mileage=None, theta0=None, theta1=None):
	if mileage == None:
		print("Error: Please introduce a mileage as an input.")
		exit(1)
	try:
		mileage = float(mileage)
	except ValueError:
		print("Error: Mileage given must be a number.")
		exit(1)
	if theta0 == None or theta1 == None:
		try:
			file = open("mandatory/vars", "r")
			text = file.read()
			file.close()
		except:
			print("Error: Unable to open a vars file")
			exit(1)
		text = [x.split(" = ") for x in text.split("\n")]
		for var in text:
			if var[0] == "theta0":
				theta0 = float(var[1])
			elif var[0] == "theta1":
				theta1 = float(var[1])
	else:
		try:
			theta0 = float(theta0)
			theta1 = float(theta1)
		except ValueError:
			print("Error: θs given must be numbers.")
			exit(1)

	if theta0 == None or theta1 == None:
		print("Error: Unable to retrieve the variable's values.")
		exit(1)

	# print(float(mileage), theta0, theta1)
	return(theta0 + mileage * theta1)


if __name__=="__main__":
	if len(sys.argv) == 2:
		print(estimatePrice(sys.argv[1]))
	elif len(sys.argv) == 4:
		print(estimatePrice(sys.argv[1], sys.argv[2], sys.argv[3]))
	elif len(sys.argv) < 2: 
		print("Not enough arguments provided.")
	elif len(sys.argv) == 3: 
		print("Wrong amount of arguments provided.")
	else:
		print("Too many arguments provided.")