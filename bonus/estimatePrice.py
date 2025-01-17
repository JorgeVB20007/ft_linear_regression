import sys
import matplotlib.pyplot as plt

def error_and_exit(line1, line2=None):
	print("Error:", line1)
	if line2:
		print(">>", line2, "<<")
	exit(1)

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
			file = open("vars", "r")
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




def generateGraph(estimatedPrice, mileage):
	try:
		f = open("data.csv", "r")
		data = (f.read()).split("\n")
		f.close()
	except:
		error_and_exit("Unable to open file `data.csv`.")

	xs = []
	ys = []
	for d in data[1:]:
		d = d.split(",")
		if len(d) == 0 or len(d[0]) == 0:
			continue
		elif len(d) != 2:
			error_and_exit("The `data.csv` file is not formatted correctly.", d)
		try:
			xs.append(int(d[0]))
			ys.append(int(d[1]))
		except:
			error_and_exit("The `data.csv` file is not formatted correctly.", d)

	xs.append(mileage)
	ys.append(estimatedPrice)

	line_xs = [min(xs), max(xs)]
	line_ys = [estimatePrice(min(xs)), estimatePrice(max(xs))]

	plt.scatter(xs[:-1], ys[:-1])
	plt.plot(line_xs, line_ys, color="red")
	plt.scatter([xs[-1]], [ys[-1]], color="lime")
	plt.xlabel("Mileage (km)")
	plt.ylabel("Price (₳)")
	plt.title("Estimated price per mileage")
	plt.show()


if __name__=="__main__":
	estimatedPrice = 0
	if len(sys.argv) == 2:
		estimatedPrice = estimatePrice(sys.argv[1])
	elif len(sys.argv) == 4:
		estimatedPrice = estimatePrice(sys.argv[1], sys.argv[2], sys.argv[3])
	elif len(sys.argv) < 2: 
		error_and_exit("Not enough arguments provided.")
	elif len(sys.argv) == 3: 
		error_and_exit("Wrong amount of arguments provided.")
	else:
		error_and_exit("Too many arguments provided.")

	print("Estimated price:", estimatedPrice, "₳")
	print("Generating graph...")
	generateGraph(estimatedPrice, int(sys.argv[1]))



