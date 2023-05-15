import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pf = pd.read_excel('fcuData.xlsx', header=1)

# print(pf.index)
# print(pf.columns)

#print(pf['LOC(%)'].describe())
# print(temp[0])
data =   pf['LOC(%)']
data1 =  pf['ROC(%)']
data2 =  pf['TOC(%)']
data3 =  pf['TIC (%)']
data4 =  pf['TC(%)']
data5 =  pf['TN (%)']
data_sum = [data, data1, data2, data3, data4, data5]
print(data.name)
data_lab = ['LOC(%)', 'ROC(%)', 'TOC(%)', 'TIC(%)', 'TC(%)', 'TN(%)']
print(pf['TOC(%)'].describe()[0])
for i  in data_sum:

    print(i.describe())
    pf[i.name+'Info'] = 
print(pf.head(5))
plt.boxplot([data, data1, data2, data3, data4, data5],
            notch=None, sym = '*', vert=True, whis=None, 
            positions=None, widths=None, patch_artist=True, 
            bootstrap=None, usermedians=None, conf_intervals=None, 
            meanline=None, showmeans=True, showcaps=None, showbox=True,
            showfliers=True, labels=['LOC(%)', 'ROC(%)', 'TOC(%)', 'TIC(%)', 'TC(%)', 'TN(%)'], flierprops=None, boxprops = {'color':'orangered','facecolor':'pink'})
plt.show()




