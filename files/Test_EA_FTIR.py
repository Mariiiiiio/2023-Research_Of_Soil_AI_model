import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
pf = pd.read_excel('Data/EA/EA.xlsx', sheet_name='WZW-A')

TOC = pf[0:41]['TOC(%)']
TN = pf[0:41]['TN(%)']
print(f'{TOC}')
print(f'{TN}')

plt.plot(TOC, TN, '.')
plt.show( )
# print(pf[0:41])