import matplotlib.pyplot as plt
from estimatePrice import estimatePrice


f = open("data.csv", "r")
data = (f.read()).split("\n")
f.close()

values = []
xs = []
ys = []
for d in data[1:]:
	d = d.split(",")
	if len(d) != 2:
		break
	values.append((int(d[0]), int(d[1])))
	xs.append(int(d[0]))
	ys.append(int(d[1]))



print(xs)
print(ys)

temp_theta0 = ys[0]
temp_theta1 = 0

for attempt in range(1, len(values)):
	print(">", temp_theta0, temp_theta1)
	thesum = 0
	for sumattempt in range(attempt):
		thesum += estimatePrice(xs[sumattempt], temp_theta0, temp_theta1) - ys[sumattempt]
	temp_theta0 = (1 / attempt) * thesum
	thesum = 0
	for sumattempt in range(attempt):
		thesum += estimatePrice(xs[sumattempt], temp_theta0, temp_theta1) - ys[sumattempt]
	temp_theta1 = (1 / attempt) * thesum * xs[sumattempt]
	
print(max(xs))

line_xs = [0, max(xs)]
line_ys = [estimatePrice(0, temp_theta0, temp_theta1), estimatePrice(max(xs), temp_theta0, temp_theta1)]


plt.scatter(xs, ys)
# plt.plot(line_xs, line_ys)
plt.show()