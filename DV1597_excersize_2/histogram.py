import pandas as pd
import matplotlib.pyplot as plt

data = [10.65, 2.64, 7.99, 4.44, 4.47, 1.72, 2.80, 7.58, 9.88, 4.89, 3.50, 0.04, 7.20, -1.43, 6.58,
2.98, 4.09, 4.75, 7.94, 3.19, 3.90, 6.71, 10.75, 2.16, 11.39, 7.36, 3.09, 4.81, 10.35, 5.50,
5.39, 4.09, 1.52, 3.45, 5.64, 6.15, 3.85, 5.95, 8.86, 4.65, 4.78, 7.63, 7.10, 2.04, 0.10,
4.39, 10.82, 6.31, 3.89, 7.47, 4.58, 2.76, 5.91, 4.01, 8.21, 8.64, 6.08, 4.90, 1.12, 8.20,
9.12, 3.64, 6.18, 12.52, 7.69, 10.10, 4.93, 3.87, 3.85, 4.62, 6.28, 9.30, 4.40, 8.04, 9.65,
6.54, 3.42, 2.20, 7.09, 6.24, 7.41, 7.97, 4.62, -2.66, 6.44, 4.53, 7.27, 3.06, 6.85, 5.46,
2.22, 7.63, 8.92, 8.29, 5.48, 6.21, 1.64, 8.23, 1.55, 4.51]

my_data = pd.Series(data)
my_data.hist()
plt.savefig('hist.pdf')