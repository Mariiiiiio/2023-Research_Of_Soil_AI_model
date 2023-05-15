import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_excel("SN_014_A6.asc.xlsm")
data1 = list(df['A'])
data2 = list(df['B'])
print(data1,data2)

plt.plot(data1, data2)
plt.show()