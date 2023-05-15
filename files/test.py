import os
import os.path as osp
import matplotlib.pyplot as plt
import pandas as pd

def change_DataType(count, list_data):
    root_path = data_root_path
    for out_name in list_data:
        now_file = root_path + out_name
        checkfile = os.listdir(now_file)
        # print(checkfile)
        for inside_name in checkfile:
            now_data = now_file+'/'+inside_name
            # print(now_data)
            checkdata = os.listdir(now_data)
            # print(checkdata)
            count = 0
            for i in range(len(checkdata)):
                if '.txt' in checkdata[i]:
                    path = checkdata[i] 
                    # print(path)
                    # print(count)
                    if count < 9:
                        # path = checkdata[i] 
                        # print(path)
                        list_Wavenumber = []
                        list_Transmittance = []
                        file = None
                        try:
                            # print(now_data +"/"+ path)
                            file = open(now_data +"/"+ path, 'r')
                            for line in file.readlines():
                                line = line.strip('\n')
                                if line != '':
                                    line_split = line.split('\t')
                                    line_Wavenumber = line_split[0]
                                    line_Transmittance = line_split[1]
                                    # print(line_Wavenumber,line_Transmittance)
                                    list_Wavenumber.append(float(line_Wavenumber))
                                    list_Transmittance.append(float(line_Transmittance))
                        except IOError:
                            print('ERROR: can not found ' + path)
                            if file:
                                file.close()
                        finally:
                            if file:
                                count += 1
                                file.close()
                        
                        # print(list_Wavenumber,list_Transmittance)
                        plt.gca().invert_xaxis()
                        plt.plot(list_Wavenumber,list_Transmittance, label=path)
                    else:
                        count = 0
                        plt.plot(list_Wavenumber,list_Transmittance, label=path)
                        plt.xlabel("Wavenumber(cm-1)") # x label
                        plt.ylabel("Transmittance(%)") # y label
                        plt.legend(loc = 'lower left')
                        plt.show()


data_root_path = '20221205/'
# wavedata = data_root_path + 'data_wave'
datalist = os.listdir(data_root_path)
# print(datalist)
change_DataType(len(datalist), datalist)