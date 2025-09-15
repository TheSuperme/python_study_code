'''
大致开发步骤
  一、准备pygame的开发环境：窗口的尺寸、标题、一些要用到的变量
  二、while True:
    1、用户的输入时间
    2、根据用户的输入时间进行一些游戏逻辑的判断
    3、渲染界面
    4、控制渲染速度
'''
#------------------------------------
#导入相应的包
import pygame
from pygame.locals import *
'''拓展：
from pygame.locals import * 的作用是什么？
简单来说，这行代码的作用是把 pygame.locals 模块里的所有常量都引入到你的代码中，让你可以直接使用这些常量的名字，而不需要每次都写完整的 pygame. 前缀。
具体效果：
没用这行代码时：你需要写 pygame.QUIT、pygame.KEYDOWN 这样带前缀的名字。
用了这行代码后：你可以直接写 QUIT、KEYDOWN,省去了 pygame. 的麻烦。
'''
#初始化pygame
pygame.init()
#------------------------------------
WEIGHT =  1080   #窗口宽
HEIGH  =  680   #窗口高
BLOCK_SIZE = 20  #定义每一个正方形小格的大小   
COLOR  = (15,255,170) #设置颜色--后续可能会用
COLOR_BLUE = (0,0,255)
COLOR_WHITE = (255,255,255)
COLOR_RED = (255,0,0)
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
dict_aux_move = {
        UP : (0,-20),
        DOWN:(0,20),
        LEFT:(-20,0),
        RIGHT:(20,0),
    }
#--------- 
class Snake():
    def __init__(self):
        self.direction = DOWN
        head_image = pygame.image.load('E:/Study_Note/python_code/b.png')  #蛇头图片
        self.snake_head_image = pygame.transform.scale(head_image,(BLOCK_SIZE,BLOCK_SIZE))#对图片进行缩放
        self.snake_body = [
            pygame.Rect(5*BLOCK_SIZE,3*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(4*BLOCK_SIZE,3*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
            pygame.Rect(3*BLOCK_SIZE,3*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
        ]
        
    def draw(self,screen):      #描绘蛇头
        for node in self.snake_body[1:]:
            pygame.draw.rect(screen,COLOR_WHITE,node,border_radius=3)  
        head_snake = self.snake_body[0]
        screen.blit(self.snake_head_image,(head_snake.x,head_snake.y))  #设置背景图片     
    def change_direction(self,dir):
        UD = (UP,DOWN)
        LR = (LEFT,RIGHT)
        if self.direction in UD and dir in UD:
            return
        if self.direction in LR and dir in LR:
            return
        self.direction = dir

    def move(self):
        #将蛇头复制一份
        new_node = self.snake_body[0].copy()  
        next_move = dict_aux_move[self.direction]
        #向前进的方向移动一格
        new_node.x += next_move[0]
        new_node.y += next_move[1]
        
        # if new_node.x >= 800:
        #     new_node.x -= 800
        # elif new_node.x < 200:
        #     new_node.x += 200
            
        # if new_node.y >= 600:
        #     new_node.y -= 600
        # elif new_node.y < 100:
        #     new_node.y += 100
            
        #将新的蛇头放在最前面
        self.snake_body.insert(0,new_node)   #不用后面这个self.snake_body.append(new_node)
        #移除蛇尾   
        self.snake_body.pop()  #不加索引默认移除最后一个元素 
        
    def graw(self):
        #将蛇尾巴复制一份
        new_node = self.snake_body[-1].copy()  
        #将新的节点放在最后面
        self.snake_body.append(new_node)
         

#-----------
def generate_food_pos(snake:Snake):
    import random
    while True:
        x = random.randint(0,WEIGHT//BLOCK_SIZE-1)
        y = random.randint(0,HEIGH//BLOCK_SIZE-1)
        new_pos = pygame.Rect(x*BLOCK_SIZE,y*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE),
        if new_pos not in snake.snake_body:
            return new_pos
class Food():
    def __init__(self,node):
        self.food_node = node
    def draw(self,screen):
        pygame.draw.rect(screen,COLOR_BLUE,self.food_node,border_radius=3)         
#---------    
class Game():
    def __init__(self):
        self.score = 0
        self.fps = 0
        self.is_gameover = False #游戏是否结束标志位
        #创建窗口并定义大小
        self.screen:pygame.surface.Surface = pygame.display.set_mode(size=(WEIGHT,HEIGH))    #screen后面的:pygame.surface.Surface是给我们看的
        #定义窗口的名称
        pygame.display.set_caption('贪吃蛇v1.0')
        #定义窗口的图标
        icon_image = pygame.image.load('E:/Study_Note/python_code/c.png')  #用于窗口图标的图片
        pygame.display.set_icon(icon_image)
        self.girl_image = pygame.image.load('E:/Study_Note/python_code/a.png')  #用于背景填充
    
    def show_text(self,string,text_size,x,y):
        '''
            string: 要显示的内容
            text_size:字号
            x:显示的字的横坐标
            y:显示的字的横坐标
        '''
        font = pygame.font.SysFont('SimHei',text_size)  #设置字体样式和大小
        text = font.render(string,True,COLOR_RED)       #设置要显示的文本以及是否反锯齿和字体颜色
        self.screen.blit(text,(x,y))
         
    def start(self) ->None:    
        #-----------------
        temp = UP
        clock = pygame.time.Clock() #初始化时钟对象
        snake = Snake()#初始化贪吃蛇对象 
        food = Food(generate_food_pos(snake)) #获取新的事物的位置  ---初始化食物对象 
        #------------------------------------
        while True:
        #--------------处理用户输入事件
            event_list = pygame.event.get() #获取用户输入的事件
            for event in event_list:
                if event.type == pygame.QUIT:  #点击窗口的x
                    pygame.display.quit() #退出窗口
                    exit(0) #退出进程
                elif event.type == pygame.KEYDOWN:
                    if self.is_gameover == True:
                        self.score = 0
                        if event.key == pygame.K_q:
                            pygame.display.quit()  #退出窗口
                        else:
                            clock = pygame.time.Clock() #初始化时钟对象
                            snake = Snake()#初始化贪吃蛇对象 
                            food = Food(generate_food_pos(snake)) #获取新的事物的位置  ---初始化食物对象 
                            self.is_gameover =  False
                            continue
                            
                    if event.key == pygame.K_a:
                        print('向左')
                        temp = LEFT
                    elif event.key == pygame.K_d:
                        print('向右')
                        temp = RIGHT
                    elif event.key == pygame.K_w:
                        print('向上')  
                        temp = UP
                    elif event.key == pygame.K_s:
                        print('向下')
                        temp = DOWN
            snake.change_direction(temp) 
            #----------根据事输入事件处理一些逻辑
            if self.is_gameover == False:
                snake.move() #贪吃蛇移动
                snake_head = snake.snake_body[0]
                #遇到食物，吃掉蛇身长一节
                if snake_head == food.food_node:
                    food = Food(generate_food_pos(snake))  #生成新的食物位置
                    snake.graw() #贪吃蛇增长一节
                    self.score += 1
                #如果蛇头撞到边界，游戏结束
                if  snake_head.x < 0 or snake_head.x >=  WEIGHT or snake_head.y < 0 or snake_head.y >= HEIGH:
                    self.is_gameover = True
                #如果咬到自己也游戏结束         赵宇龙来了
                if snake_head in snake.snake_body[1:]:
                    self.is_gameover = True
                
                
                    
                #--------------界面渲染
                self.screen.blit(self.girl_image,(-20,-20))  #设置背景图片
                #绘制网格线
                for a in range(0,HEIGH,20):   #横向
                    start = (0,a)
                    end   = (WEIGHT,a)
                    pygame.draw.line(self.screen,COLOR,start,end)
                for b in range(0,WEIGHT,20):   #纵向
                    start = (b,0)
                    end   = (b,HEIGH)
                    pygame.draw.line(self.screen,COLOR,start,end)    
                snake.draw(self.screen)  #设置贪吃蛇位置
                food.draw(self.screen)   #设置食物位置
                
                if self.is_gameover == True:
                    self.show_text("游戏结束",70,WEIGHT//4,HEIGH//4)
                    self.show_text(f"score:{self.score}",25,WEIGHT//4,HEIGH//4+80)
                    self.show_text("按任意键重新开始",25,WEIGHT//4,HEIGH//4+105)
                    self.show_text("按Q退出",25,WEIGHT//4,HEIGH//4+130)
                    
                self.show_text(f"score:{self.score}",25,0,0)
                self.show_text(f"fps:{12.00 + 1.5*self.score:.2f}",25,WEIGHT-150,0)
                pygame.display.flip() #执行最终的渲染（刷新屏幕）
                #------------控制渲染速度（帧率)
                clock.tick(12 + self.score) #设置帧率
                self.fps = clock.get_fps() #打印帧率
                
    
        
game = Game()
game.start()



