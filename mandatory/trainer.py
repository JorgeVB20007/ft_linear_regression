from estimatePrice import estimatePrice


def error_and_exit(line1, line2=None):
	print("Error:", line1)
	if line2:
		print(">>", line2, "<<")
	exit(1)

try:
	f = open("data.csv", "r")
	data = (f.read()).split("\n")
	f.close()
except:
	error_and_exit("Unable to open file `data.csv`.")

values = []
xs = []
ys = []
for d in data[1:]:
	d = d.split(",")
	if len(d) == 0 or len(d[0]) == 0:
		continue
	elif len(d) != 2:
		error_and_exit("The `data.csv` file is not formatted correctly.", d)
	try:
		values.append((int(d[0]), int(d[1])))
		xs.append(int(d[0]))
		ys.append(int(d[1]))
	except:
		error_and_exit("The `data.csv` file is not formatted correctly.", d)


temp_theta0 = 0
temp_theta1 = 0

while True:
	thesum0 = 0
	for sumattempt in range(len(values)):
		thesum0 += estimatePrice(xs[sumattempt], temp_theta0, temp_theta1) - ys[sumattempt]
	thesum1 = 0
	for sumattempt in range(len(values)):
		thesum1 += (estimatePrice(xs[sumattempt], temp_theta0, temp_theta1) - ys[sumattempt]) * (xs[sumattempt] / max(xs))
	if (abs((1 / len(values)) * thesum0) < 0.0001) and (abs((1 / len(values)) * thesum1 / max(xs)) < 0.0001):
		break
	temp_theta0 -= 0.1 * (1 / len(values)) * thesum0
	temp_theta1 -= 0.1 * (1 / len(values)) * thesum1 / max(xs)
	

line_xs = [min(xs), max(xs)]
line_ys = [estimatePrice(min(xs), temp_theta0, temp_theta1), estimatePrice(max(xs), temp_theta0, temp_theta1)]

print(">> Thetas found:", temp_theta0, temp_theta1)

try:
	f = open("vars", "w")
	f.write("theta0 = " + str(temp_theta0) + "\ntheta1 = " + str(temp_theta1))
	f.close()
except:
	print("Error: Unable to write result to a `vars` file")
