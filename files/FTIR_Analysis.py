import os
import os.path as osp
import matplotlib.pyplot as plt
import pandas as pd
def draw(list1, list2, vary):
    plt.plot(list1, list2)
    if vary == 'wzwc':
        plt.gca().invert_xaxis()
    plt.xlabel("Wavenumber(cm-1)") # x label
    plt.ylabel("Transmittance(%)") # y label
    # plt.legend(loc = 'lower left')
    plt.legend(loc = 'best', fontsize = 'x-small')
    plt.show()
def count_number(data, file_le):
    check_for_letter_A = []
    check_for_letter_B = []
    check_for_letter_C = []
    # for j in range(len(data)):
    #     if 'wzwa' in data[j]:
    #         print(data[j])
    #         check_for_letter_A.append(data[j])
    #         print(check_for_letter_A)
        # elif 'wzwb' in data[j]:
        #     check_for_letter_B.append(data[j])
        #     print(check_for_letter_B)
        # elif 'wzwc' in data[j]:
        #     check_for_letter_C.append(data[j])
    if file_le == 'wzwa':
        for j in range(len(data)):
            if 'wzwa' in data[j]:
                print('===',data[j])
                check_for_letter_A.append(data[j])
        print('Here--------',len(check_for_letter_A))
        return len(check_for_letter_A)
    elif file_le == 'wzwb':
        for j in range(len(data)):
            if 'wzwb' in data[j]:
                check_for_letter_B.append(data[j])
            print(check_for_letter_B)
        print(len(check_for_letter_B))
        return len(check_for_letter_B)
    elif file_le == 'wzwc':
        for j in range(len(data)):
            if 'wzwc' in data[j]:
                check_for_letter_C.append(data[j])
            print(check_for_letter_B)
        print(len(check_for_letter_C))
        return len(check_for_letter_C)

def change_DataType(count, list_data, file_letter):
    root_path = data_root_path
    for out_name in list_data:
        
        now_file = root_path + out_name
        checkfile = os.listdir(now_file)
        # print(checkfile)
        for inside_name in checkfile:
            if '_newFile' in inside_name:
                # print(inside_name)
                now_data = now_file+'/'+inside_name
                # print(now_data)
                checkdata = os.listdir(now_data)
                # print(checkdata)
                count = 0
                a = 0
                
                letter_num = count_number(checkdata, file_letter)
                for i in range(len(checkdata)):
                    
                    check_for_newfile = checkdata[i].count('_')

                    # print(f'check_for : {check_for_letter}')
                    if '.txt' in checkdata[i] and check_for_newfile == 2 and file_letter in checkdata[i]:
                        a += 1
                        # print(f'{file_letter} = {a}')
                        path = checkdata[i] 
                        list_Wavenumber = []
                        list_Transmittance = []
                        file = None
                        try:
                            # if file_letter == 'wzwb':
                            #     print(now_data +"/"+ path)
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
                                if file_letter == 'wzwc':
                                    plt.plot(list_Wavenumber,list_Transmittance, label=path)
                                else:
                                    plt.gca().invert_xaxis()
                                    plt.plot(list_Wavenumber,list_Transmittance, label=path)
                                # plt.show()
                                if file_letter == 'wzwb':
                                    # print(f'wzwb')
                                    # print(count)
                                    # print('letter',letter_num)
                                    # print(letter_num/2)
                                    if count == letter_num/2 - 1:
                                        draw(list_Wavenumber, list_Transmittance, file_letter)
                                else:
                                    if count == letter_num/2:
                                        print('yes',path)
                                        draw(list_Wavenumber, list_Transmittance, file_letter)
                                

                                    
                
                # list_Wavenumber = []
                # list_Transmittance = []
                # for i in range(len(checkdata)):
                #     check_for_newfile = checkdata[i].count('_')
                #     check_for_letter = checkdata.count('wzwb')
                   
                #     if '.txt' in checkdata[i] and check_for_newfile == 2 and 'wzwb' in checkdata[i]:
                        
                #         path = checkdata[i] 
                        
                #         file = None
                #         try:
                #             # print(now_data +"/"+ path)
                #             file = open(now_data +"/"+ path, 'r')
                #             for line in file.readlines():
                #                 line = line.strip('\n')
                #                 if line != '':
                #                     line_split = line.split('\t')
                #                     line_Wavenumber = line_split[0]
                #                     line_Transmittance = line_split[1]
                #                     # print(line_Wavenumber,line_Transmittance)
                #                     list_Wavenumber.append(float(line_Wavenumber))
                #                     list_Transmittance.append(float(line_Transmittance))
                #         except IOError:
                #             print('ERROR: can not found ' + path)
                #             if file:
                #                 file.close()
                #         finally:
                #             if file:
                #                 # count += 1
                #                 file.close()
                #                 if count == len(check_for_letter_B)/2:
                #                     draw(list_Wavenumber, list_Transmittance, path)
                #                     count = 0
                                    

                # list_Wavenumber = []
                # list_Transmittance = []
                # for i in range(len(checkdata)):
                #     check_for_newfile = checkdata[i].count('_')
                #     check_for_letter = checkdata.count('wzwc')

                #     if '.txt' in checkdata[i] and check_for_newfile == 2 and 'wzwc' in checkdata[i]:
                #         # a += 1
                #         # print(f'a = {a}')
                #         path = checkdata[i] 
                #         list_Wavenumber = []
                #         list_Transmittance = []
                #         file = None
                #         try:
                #             # print(now_data +"/"+ path)
                #             file = open(now_data +"/"+ path, 'r')
                #             for line in file.readlines():
                #                 line = line.strip('\n')
                #                 if line != '':
                #                     line_split = line.split('\t')
                #                     line_Wavenumber = line_split[0]
                #                     line_Transmittance = line_split[1]
                #                     # print(line_Wavenumber,line_Transmittance)
                #                     list_Wavenumber.append(float(line_Wavenumber))
                #                     list_Transmittance.append(float(line_Transmittance))
                #         except IOError:
                #             print('ERROR: can not found ' + path)
                #             if file:
                #                 file.close()
                #         finally:
                #             if file:
                #                 # count += 1
                #                 file.close()
                #                 if count == len(check_for_letter_C)/2:
                #                     draw(list_Wavenumber, list_Transmittance, path)
                #                     count = 0
                                    
                #--------------------------------------- up is the main code
                #     if '.txt' in checkdata[i]:
                #         path = checkdata[i] 
                #         # print(path)
                #         # print(count)
                #         if count < 9:
                #             # path = checkdata[i] 
                #             # print(path)
                #             list_Wavenumber = []
                #             list_Transmittance = []
                #             file = None
                #             try:
                #                 # print(now_data +"/"+ path)
                #                 file = open(now_data +"/"+ path, 'r')
                #                 for line in file.readlines():
                #                     line = line.strip('\n')
                #                     if line != '':
                #                         line_split = line.split('\t')
                #                         line_Wavenumber = line_split[0]
                #                         line_Transmittance = line_split[1]
                #                         # print(line_Wavenumber,line_Transmittance)
                #                         list_Wavenumber.append(float(line_Wavenumber))
                #                         list_Transmittance.append(float(line_Transmittance))
                #             except IOError:
                #                 print('ERROR: can not found ' + path)
                #                 if file:
                #                     file.close()
                #             finally:
                #                 if file:
                                    # count += 1
                #                     file.close()
                            
                #             # print(list_Wavenumber,list_Transmittance)
                #             plt.gca().invert_xaxis()
                #             plt.plot(list_Wavenumber,list_Transmittance, label=path)
                #         else:
                #             count = 0
                #             plt.plot(list_Wavenumber,list_Transmittance, label=path)
                #             plt.xlabel("Wavenumber(cm-1)") # x label
                #             plt.ylabel("Transmittance(%)") # y label
                #             plt.legend(loc = 'lower left')
                #             plt.show()


data_root_path = 'data_wave/'
# wavedata = data_root_path + 'data_wave'
datalist = os.listdir(data_root_path)
# print(datalist)
change_DataType(len(datalist), datalist, 'wzwa')

change_DataType(len(datalist), datalist, 'wzwb')

change_DataType(len(datalist), datalist, 'wzwc')