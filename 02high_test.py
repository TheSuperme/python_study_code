'''ss = {'白龙马', '唐僧', '八戒', '悟空', '沙僧',1,23}

print(ss)

'''

'''
ss = '中华人民共和国欢迎您'
print(ss[7:1:-1])


list1 = range(3)
list2 = range(1,7)

print(list(zip(list1,list2,'mmdsybb')))
'''

'''
请写出一段Python代码实现分组一个1ist里面的元素
比如[1,2,3, ...100] 变成[[1,2,3],[4,5,6]....[100]
问题简化 :
[10,20,30,40,50,60,70,80] = {
    [10,20,30],
    [40,50,60],
    [70,80]
} 

'''
'''
list1 = [10,20,30,40,50,60,70,80]  

reciv = [list1[ele:ele+3]  for ele in range(len(list1)) if ele % 3 == 0]

print(reciv)   


#现在在再来挑战问题，

list2 = list(range(1,101))

reciv2 = [list2[ele:ele+3]  for ele in range(len(list2)) if ele % 3 == 0]

print(reciv2)'''



#----------------------------------
'''需求
完成字符串的逆序以及统计
设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
打印如下内容
-----------------------------
    您输入的字符串：zhongshanshan
    长度：13
    逆序后为：nahsnahsgnohz
    字符统计结果:z:1 h:3 o:1 n:3 g:1 s:2.a:2
-----------------------------'''

'''while True:
    userinput_list = input('请输入一个长度小于31的字符串:')  #接收用户输入的字符串
    if len(userinput_list) > 31:
        print('输入的字符串长度大于31，请重新输入')
    else:
        break

template = 
----------------------------
    您输入的字符串是:{}
    长度是{}
    逆序后为:{}
    字符统计结果为:{}
----------------------------

aux_dict = {}
ss_string = ''
for ele in userinput_list:
    if ele in aux_dict:
        aux_dict[ele] += 1
    else:
        aux_dict[ele] = 1
    
ss_string = ['{}:{}'.format(k,v)  for k,v in aux_dict.items()]



print(template.format(
    userinput_list,
    len(userinput_list),
    userinput_list[::-1],
    ' '.join(ss_string)
    )
)



'''
#----------------------------------
'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print("你好小姐")

    def love(self,name):
       print("{}你{}".format(self.name,name))
p = Person('s',20)

p.say_hello()
p.love('w')'''


#----------------------------------
'''
class Item:
    def __init__(self,type,area):
        self.type = type
        self.area = area
    
    def __str__(self):
        return '家具类型:{},面积:{}'.format(self.type,self.area)
    
bed = Item('床',4)
print(bed)

class House:
    def __init__(self,address,area,free_area,items):
        self.address = address
        self.area = area
        self.free_area = free_area
        self.item = items
    
    def __str__(self):
       return '房子地址:{},房子面积:{},剩余面积:{},家具列表:{}'.format(self.address,self.area,self.free_area,self.item) 
   
   
    def add_item(self,item):
        if self.free_area >= item.area: #判断剩余面积是否大于家具面积
            self.free_area -= item.area #剩余面积减少
            self.item.append(item.type) #添加家具
        else:
            print('剩余面积不足,添加家具失败')
    
king_house = House('四川',120,100,[])
print(king_house)   
king_house.add_item(bed)
print(king_house)   

desk = Item('桌子',2)  
print(desk)
king_house.add_item(desk)
print(king_house)   

'''

#----------------------------------
'''class Bank:
    def __init__(self,user_card,all_money):
        self.user_card = user_card
        self.__all_money = all_money
    
    def take_out_money(self,number):
        if 0 < number < self.__all_money:
            self.__all_money -= number
        else:
            print('取款失败，可能是您输入的金额错误或者余额不足')
        return
    def take_in_money(self,number):
        if 0 < number:
            self.__all_money += number
        else:
            print('存款失败，可能是您输入的金额错误')
        return
    def query_money(self):
        print('剩余余额:{}'.format(self.__all_money) )
    

user = Bank('张三',1000)
user.take_out_money(300)
user.query_money()
user.take_out_money(100)
user.query_money()
user.take_in_money(600)
user.query_money()


'''

#-------------------------------------------------------
'''class washMeachine:
    def __init__(self,band,volume):
        self.band = band
        self.volume = volume
        
        self.__is_open = False
        self.__motor = 0
        self.__speed_mode = 0 #0--轻柔模式  1--普通模式  2--强力模式
        
    def open(self):
         self.__is_open = True
         print('洗衣机已打开，请放入衣物')
    
    def setmode(self,number):
        if number not in [0,1,2]:
            return
        self.__speed_mode = number
        print('模式已设置完毕')  
    def close(self):
        self.__is_open = False
        print('洗衣机已关闭，可以开始工作')

    def work(self):
        if self.__is_open != False:
            print('未关闭洗衣机，无法开始工作')
            return
        print('机器启动中...')
        if self.__speed_mode == 0:
            self.__motor = 500
        elif self.__speed_mode == 1:
            self.__motor = 1000
        else:
            self.__motor = 2000
        print('现在模式下洗衣机的转速为 {} 转/min'.format(self.__motor))
        print('机器正在猛猛运作中') 
        print('watting......') 
        print('清洗完毕') 
        
wash = washMeachine('海尔',20)
wash.open()
wash.setmode(1)
wash.close()
wash.work()
'''

#-------------------------
#导入相关的pygame包
import pygame
#初始化pygame
pygame.init()
#创建窗体
screen = pygame.display.set_mode(size = (1080,600))
COLOR = (155,15,55) 
girl_image = pygame.image.load('E:\Study_Note\Python_code/b.png')
girl_image = pygame.transform.rotate(girl_image,90) #旋转图片90度（逆时针）
pygame.display.set_caption('一个测试v1.0') #设置窗体的标题
icon_image = pygame.image.load('E:\Study_Note\Python_code/c.png') #设置窗体的图标
pygame.display.set_icon(icon_image) #设置窗体的图标
clock = pygame.time.Clock()  # 初始化时钟对象
while True:
    #*************第一部分：事件处理************
    event_list = pygame.event.get() #获取用户触发的事件
    for event in event_list:
        if event.type == pygame.QUIT:      #事件：鼠标点击关闭按钮
            pygame.display.quit() #退出pygame
            exit(0) #退出中端
        elif event.type == pygame.KEYDOWN: #事件：按下电脑上的键盘
            print(f'按下了{event.key}')
            if event.key == pygame.K_a:
                print('按下a键,向左')
            elif event.key == pygame.K_d:
                print('按下d键,向右')
            elif event.key == pygame.K_w:
                print('按下w键,向上')
            elif event.key == pygame.K_s:
                print('按下s键,向下')
            
    #*************第二部分：界面绘制************
    screen.fill(COLOR) #填充背景色
    screen.blit(girl_image,(0,0)) #绘制图片
    pygame.display.flip() #刷新屏幕
    clock.tick(60) #设置帧率
    print(clock.get_fps()) #打印帧率
    