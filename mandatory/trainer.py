import matplotlib.pyplot as plt


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

plt.scatter(xs, ys)
plt.show()
