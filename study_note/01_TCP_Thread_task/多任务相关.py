# #               阻塞式的执行任务
# import time

# def talk()->None:
#     for i in range(5):
#         print('你从丹东来。。。',i)
#         time.sleep(1)

# def play()->None:
#     for i in range(5):
#         print('一起玩游戏qwq',i)
#         time.sleep(1)
        

# if __name__ == "__main__":
#     talk()
#     play()

#***************************************************************************************************************************************************************************
#               线程的执行任务
import time
import threading

def talk()->None:
    for i in range(5):
        print('你从丹东来。。。',i)
        time.sleep(1)

def play()->None:
    for i in range(5):
        print('一起玩游戏qwq',i)
        time.sleep(1) #可将这里的时间改成0.5感受一下
        

if __name__ == "__main__":
    sub_thread_talk = threading.Thread(target=talk)
    sub_thread_play = threading.Thread(target=play)
    sub_thread_talk.start()
    sub_thread_play.start()
    