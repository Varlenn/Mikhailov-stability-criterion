import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

x = []
y = []
x_pos = []
y_pos = []

n = int(input('enter the number of points:\n'))
v = []
for i in range(n):
    v.append(i / 10)

odds = [float(p) for p in input('enter odds:\n').split()]
odds.reverse()

for j in range(len(v)):
    x.append(odds[0])
    for i in range(1, len(odds), 4):
        y.append(odds[i] * v[j] ** i)
    for i in range(2, len(odds), 4):
        x.append(odds[i] * -1 * v[j] ** i)
    for i in range(3, len(odds), 4):
        y.append(odds[i] * -1 * v[j] ** i)
    for i in range(4, len(odds), 4):
        x.append(odds[i] * v[j] ** i)

size_x = int(len(x) / len(v))
size_y = int(len(y) / len(v))

for i in range(0, len(x), size_x):
    x_pos.append(sum(x[i:i + size_x]))
for i in range(0, len(y), size_y):
    y_pos.append(sum(y[i:i + size_y]))

print('\nx = ' + str(x_pos))
print('y = ' + str(y_pos))

plt.grid()
plt.axvline(color='black')
plt.axhline(color='black')
plt.plot(x_pos, y_pos, color='c')
plt.show()
