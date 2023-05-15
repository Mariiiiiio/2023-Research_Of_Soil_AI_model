import pandas as pd

filepath = "data_wave/20221205/1205_newFile/QGL_01_B1.txt"
l1 = []
#pf = pd.read_csv(filepath, sep=" ")
#with open(filepath, 'r') as fp:
    #l1 = fp.readlines()
    #print(l1)
#with open(filepath ,'w') as fp:
 #   for number, line in enumerate(l1):
  #      # print(f'{number} -> {line}')
   #     if number not in [0, 57]:
      #      fp.write(line)
     #       print(line)
    #fp.close()


file = open(filepath)    
lines = file.readlines()
             # 删除最后一行
del lines[0:56]           # 删除第1行到第17行
file.close()

file_new = open(filepath,'w+')
file_new.writelines(lines) # 将删除行后的数据写入文件
file_new.close()

