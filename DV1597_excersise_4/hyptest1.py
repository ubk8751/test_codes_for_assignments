import matplotlib.pyplot as plt
import scipy.stats as scistats
import numpy as np

x_max = 55000
x_min = 20000

x1 = 37900
x2 = 39800

s1 = 5100
s2 = 5900

x = np.linspace(x_min, x_max, 1000)

y_a = scistats.norm.cdf(x,x1,s1)
y_b = scistats.norm.cdf(x,x2,s2)

y = np.concatenate((y_a, y_b))

normtest = scistats.normaltest(y)

print(normtest)

plt.plot(x,y_a, color='coral', label='Brand A')
plt.plot(x,y_b, color='blue', label='Brand B')

plt.grid()

plt.xlim(x_min,x_max)
plt.ylim(0,10000)

plt.title('Compare tire brand 1 and 2',fontsize=10)

plt.xlabel('Kilometers')
plt.ylabel('')

plt.savefig("images/tire_comparison.png")
plt.show()