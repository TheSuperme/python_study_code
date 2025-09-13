''''超市买苹果计算金额
需求:
·收银员输入苹果的价格price，单位：元/斤
·收银员输入用户购买苹果的重量weight，单位：斤
计算并输出付款金额:xxx元'''


'''price = float(input('请输入苹果的价格：')) #单位：元/斤

weight = float(input('请输入用户购买苹果的重量：')) #单位：斤

all_spent = price * weight #单位：元

print('付款金额为：', all_spent, '元')'''


#--------------------------------------------------------


'''name = input('请输入您的姓名：')       #输入姓名
company = input('请输入您的公司：')    #输入公司
title = input('请输入您的职位：')      #输入职位
telephone = input('请输入您的电话：')  #输入电话
email = input('请输入您的邮箱：')      #输入邮箱

print('******************************************************')
print('公司名称 : ', company)sad
print('')
print('姓名(职务):',name,title)
print('')
print('电话号码 : ', telephone)
print('邮箱地址 : ', email)

print('******************************************************')
'''

'''real = 1 and 4

print(real,type(real))

num1 = 3
num2 = 4
if num1==3 and num2==4:
    print('yes') 
else:
    print('no')'''
    
#--------------------猜拳-------------------------------    
'''需求:
1. 从控制台输入要出的拳——一石头（1)/剪刀(2)/布（3)
2.电脑随机出拳——先假定电脑只会出石头，完成整体代码功能
3.比较胜负并输出结果'''
'''import random
computer_result = random.randint(1,3) #电脑出拳
user_result = int (input('请输入您的拳：')) #用户出拳

print('电脑出拳为：',computer_result)

if(user_result == 1 and computer_result == 1):
    print('平局')
elif(user_result == 1 and computer_result == 2):
    print('你赢了')
elif(user_result == 1 and computer_result == 3):
    print('你输了')
elif(user_result == 2 and computer_result == 1):
    print('你输了')
elif(user_result == 2 and computer_result == 2):
    print('平局')
elif(user_result == 2 and computer_result == 3):
    print('你赢了')    
elif(user_result == 3 and computer_result == 1):
    print('你赢了')
elif(user_result == 3 and computer_result == 2):
    print('平局')
elif(user_result == 3 and computer_result == 3):
    print('你输了')    '''
    

#--------------------------------------------------------
'''#九九乘法表
master_s = 1
slave_y = 1
aux = 1
while master_s <= 9:
    aux = 1
    while aux <= slave_y:
     print(" %d * %d = %d " %(aux,slave_y,aux*slave_y),end = '')
     aux += 1
    print()
    master_s += 1   
    slave_y += 1
    
    '''
#--------------------------------------------------------
'''    需求
个学校，有3个办公室，现在有8位老师等待工位的分配
［'袁腾飞‘，‘罗永浩‘，‘俞敏洪‘，'李永乐‘，＊王芳芳‘，＊马云‘，‘李彦宏‘，＊马化腾‘］
请编写程序：
1.完成随机的分配
2.打印办公室信息（每个办公室中的人数，及分别是谁）'''
'''import random

list_work = [
    [],
    [],
    []
]
personal_teacher = ['袁腾飞','罗永浩','俞敏洪','李永乐','王芳芳','马云','李彦宏','马化腾']

for i in range(8):
    index = random.randint(0,2)
    list_work[index].append(personal_teacher[i])
    
for i in range(3):
    print(list_work[i])
    

'''
#--------------------------------------------------------
'''
1.需求
1，程序启动，显示名片管理系统欢迎界面，并显示功能菜单
2.用户用数字选择不同的功能：新建名片、显示名片、查询名片、退出系统
a.用户名片需要记录用户的姓名、电话、QQ、邮件
b.显示名片可以列举出所有已经保存的名片
c，如果查询到指定的名片，用户可以选择修改、删除名片
**************************************************
欢迎使用【名片管理系统】V1.0
1.新建名片
2.显示全部
3.查询名片
0.退出系统
**************************************************
'''

'''list_all=[]
def new_card():
    name = input('请输入你的姓名: ')  
    number = input('请输入你的电话: ')   
    qq = input('请输入你的QQ: ')   
    email = input('请输入你的邮箱: ')  
    for card  in list_all:
        if name == card[0]:
            if number == card[1]:
                if qq == card[2]:
                    if email == card[3]:
                        print('该名片已存在')
                        return
                    
    # 将新名片的信息打包成一个小列表
    new_card_data = [name, number, qq, email]

    # 将这个新名片的小列表，作为一个整体，添加到 card_list 中
    list_all.append(new_card_data)
    print('添加成功')

 
def seek_cark(name):
    aux = -1
    just_num = 0
    for i in range(len(list_all)):
        if name  in list_all[i]:
           aux = i
        
    if(aux == -1):
        print('没有找到相关的名片')
        return
    print('找到了相关的名片')
    pase = input('是否对名片进行修改、删除操作[y/n]')
    if pase == 'n':
        return
    else:
        user_in = input('请输入你要进行的操作:1.修改 2.删除')
        if user_in == '1':
            list_all[aux][0] = input('请输入新的姓名: ')
            list_all[aux][1] = input('请输入新的电话: ')
            list_all[aux][2] = input('请输入新的QQ: ')
            list_all[aux][3] = input('请输入新的邮箱: ')
        elif user_in == '2':
            list_all.pop(aux)

while True:         
    print('*' *25) 
    print()
    print()
    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片')
    print()
    print()
    print('0.退出系统')
    print('*' *25) 
    flag = 1
    while flag == 1:
        user_input = int(input('请输入你想要进行的操作前的数字序号：'))
        if(user_input != 0 and user_input != 1 and user_input != 2 and user_input != 3):
            print('输入错误，请重新输入')
            flag = 1
        else :
            flag = 0
    
    if user_input == 1:   #新建名片
        new_card()
    elif user_input == 2:   #显示全部
        print(list_all)
    elif user_input == 3:   #查询名片
        name = input('请输入要查询的名片姓名：')
        seek_cark(name)
    elif user_input == 0:     #退出系统
          break   
      
 '''       
#--------------------------------------------------

'''string = '123abc'

print (string.isalnum() )      #判断字符串是否由字母和数字组成
print (string.isalpha()  )     #判断字符串是否由字母组成
print (string.isdigit()  )     #判断字符串是否由数字组成

print(string.startswith('123') )     #判断字符串是否以123开头
 
'''

#--------------------------------------------------
'''需求
·用户名和密码格式校验程序
·要求从键盘输入用户名和密码，分别校验格式是否符合规则
。如果符合，打印用户名合法，密码合法
。如果不符合，打印出不符合的原因，并提示重新输入
·用户名长度6-20，用户名必须以字母开头
·密码长度至少6位，不能为纯数字，不能有空格
'''

'''
while True:
    user_id = input('请输入用户账号：')
    if (len(user_id) <= 6 or len(user_id) >= 20) or not user_id[0].isalpha():
        print('用户名不合法，请重新输入')
    else :
        break
    
    
while True: 
    user_password = input('请输入密码：')
    if(len(user_password) < 6  or user_password.isdigit()  or (' ' in user_password)) :
        print('密码不合法，请重新输入')
    else :
        break
    
print('用户名： ',user_id)
print('密码： ',user_password)'''