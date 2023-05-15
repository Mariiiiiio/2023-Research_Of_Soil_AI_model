import numpy as np 
import matplotlib.pyplot as plt
import os
import pandas as pd
def data_process(path, data_route, data):
    # print(data)
    print(len(data))
    for i in range(len(data_route)):
        # print(data[i])
        # print(path)
        path_org = f'{path}/{data_route[i]}'
        # print(path_org)

        # print(path_org)
        # file = open(path_org, 'r')     
        # for line in file.readlines():
        #     line = line.split('\n')
        #     if line != '':
        #         line_split = line.split('\t')
        #         print(line_split)

def checkfile(path):
    check_path = os.listdir(path)
    # print(check_path[0 : 40])
    start = 0
    end = 40
    file = []
    for i in check_path[start : end]:
        # print(i)
        cnt = i.count('_')
        if cnt == 2:
            # print('-'*20)
            # print(i)
            file.append(i)
    print(check_path)
    data_process(path, file)






if __name__ == '__main__':

    data_path = './Data/FTIR/Tamsui_FTIR_Data_newFile'
    data_FTIR = checkfile(data_path)
    # print()
    