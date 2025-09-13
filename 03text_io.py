# list_txt = [
#     'Hello ',
#     ' My Wife'
# ]
# f = open('hhh.txt','w',encoding='utf-8')
# list_txt = [item + '\n' for item in list_txt]
# f.writelines(list_txt)
# f.close()

#--------------------------------------------------------------
# '''输入文件的名字，然后程序自动完成对文件进行备份
# 分析：
# 1.输入文件名 b.py
# 2.创建文件文件名[复制]·py->b[复制]-py
# 3.读取文件，写入到复制的文件中'''
# import os

# file_name = None

# while True:
#     file_name = input('请输入文件名:')
#     if os.path.exists(file_name) == False:
#         print('文件不存在')
#     else:
#         break

# copy_txt_index = file_name.rfind('.')
# copy_txt_pre = file_name[:copy_txt_index]
# copy_txt_suf = file_name[copy_txt_index:]

# with open(file_name,encoding='utf-8') as f:
#     copy_txt = f.read()
#     print(copy_txt)
#     with open(f'{copy_txt_pre}[复制].{copy_txt_suf}','w',encoding= 'utf-8') as f:
#         f.write(copy_txt)



#--------------------------------------------------------------
import os

while True:
    file_name = input('请输入文件名:')
    if os.path.exists(file_name) == False:
        print('文件不存在')
    else:
        
        break

with open(file_name,encoding='utf-8') as f:
    line_txt = f.readlines()
    line_num = len(line_txt)
print(line_num)
       
       
    