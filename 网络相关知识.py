#***************************************************************************************************************************************************************************
#------------------编码解码
# bytes_arr = '你好呀'.encode()

# print(bytes_arr,type(bytes_arr))

# bysy = b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x91\x80\xe8\xaf\x97'
# result = bysy.decode()
# print(result,type(result))



#***************************************************************************************************************************************************************************
# #----------------tcp客户端(发送数据)              此时我们vscode是客户端(Client)     我们将NetAssist软件当服务端
'''流程：
1 导入socket模块
2 创建socket到套接字
3 建立tcp连接（和服务器端链接）
4 开始发送数据（不能发送字符串，而是字符串编码后的数据）
5 关闭套接字'''
# #1 导入socket模块
# import socket

# #2 创建socket到套接字
#     #参数1  地址类型 family： AddressFamily 地址簇
#     #                         socket.AF_INET      ---ipv4
#     #                         socket.AF_INET6     ---ipv6
#     # 参数2   协议类型
#     #                         socket.SOCK_STREAM --TCP
#     #                         socket.SOCK_DGRAM  --UDP                
# tcp_client_1_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       
#                     #这里第一个socket是我们导入的模块，第二个socket则是socket中的socket类，整理正常来说第二个socket的首字母一个大写，不然很容易搞混淆
# #3 建立tcp连接（和服务器端链接）
# addr = ("127.0.0.1",8080)  #这里值=指服务器(ip,port)元组
# tcp_client_1_socket.connect(addr)

# #4 开始发送数据（不能发送字符串，而是字符串编码后的数据）
# tcp_client_1_socket.send('你好，世界'.encode())

# #5 关闭套接字
# tcp_client_1_socket.close()


#***************************************************************************************************************************************************************************
# #----------------tcp客户端(发送并接收数据)                     此时我们vscode是客户端(Client)     我们将NetAssist软件当服务端
# '''流程：
# 1 导入socket模块
# 2 创建socket到套接字
# 3 建立tcp连接（和服务器端链接）
# 4 开始发送数据（不能发送字符串，而是字符串编码后的数据）
# 5 等待服务器回复消息
# 6 关闭套接字'''
# #1 导入socket模块
# import socket

# #2 创建socket到套接字
#     #参数1  地址类型 family： AddressFamily 地址簇
#     #                         socket.AF_INET      ---ipv4
#     #                         socket.AF_INET6     ---ipv6
#     # 参数2   协议类型
#     #                         socket.SOCK_STREAM --TCP
#     #                         socket.SOCK_DGRAM  --UDP                
# tcp_client_1_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       
#                     #这里第一个socket是我们导入的模块，第二个socket则是socket中的socket类，整理正常来说第二个socket的首字母一个大写，不然很容易搞混淆
# #3 建立tcp连接（和服务器端链接）
# addr = ("127.0.0.1",8080)  #这里值=指服务器(ip,port)元组
# tcp_client_1_socket.connect(addr)

# #4 开始发送数据（不能发送字符串，而是字符串编码后的数据）
# tcp_client_1_socket.send('你好，世界'.encode())

# #5 等待服务器回复消息   ---代码会在这里阻塞程序，直到服务器回复消息，自动释放阻塞
# #参数__bufsize： 设置缓冲区大小 
# print('-------------waiting datd---------------')
# recv_data = tcp_client_1_socket.recv(2048)

# print(recv_data)
# #6 关闭套接字
# tcp_client_1_socket.close()

#***************************************************************************************************************************************************************************
#----------------tcp服务器(接收数据)             此时我们vscode是服务端（Server）     我们将NetAssist软件当客户端(Client)
# '''流程：
# 1 导入socket模块
# 2 创建socket到套接字
# 3 bind绑定ip和port
# 4 listen 使套接字设置为被动模式
# 5 accept等待客户端的链接
# 6 recv/send接收发送数据
# 7 关闭套接字'''
# #1 导入socket模块
# import socket

# #2 创建socket到套接字
#     #参数1  地址类型 family： AddressFamily 地址簇
#     #                         socket.AF_INET      ---ipv4
#     #                         socket.AF_INET6     ---ipv6
#     # 参数2   协议类型
#     #                         socket.SOCK_STREAM --TCP
#     #                         socket.SOCK_DGRAM  --UDP                
# tcp_server_1_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       
#                     #这里第一个socket是我们导入的模块，第二个socket则是socket中的socket类，整理正常来说第二个socket的首字母一个大写，不然很容易搞混淆
# #3  bind绑定ip和port
# addr = ("",7788)  #这里值=指服务器(ip,port)元组   <------------------------------************这里ip将服务器绑定到 '0.0.0.0' 表示或者也可以写一个空字符串""        服务器将监听所有可用的网络接口上的连接
# tcp_server_1_socket.bind(addr)          

# #4 listen 使套接字设置为被动模式        
#     #参数表示等待客户端连接的最大数量
#     #此时，socket套接字对象由主动连接模式转变为被动接收模式，接收客户端链接
# tcp_server_1_socket.listen(128)

# print('服务器已经启动，等待客户端接入。。。。。。')
# #5 accept等待客户端的连接(值得注意的是，此时程序会阻塞，直到由客户端连接我们的服务器)
#     #服务器会为连接进来的客户端创建一个socket对象，用于与其收发数据
# while True:
#     tcp_client,tcp_client_addr = tcp_server_1_socket.accept()       #将接入服务端的客户端的信息通过提取出来（利用元组的自动解包）
#     print('有新的客户端接入：',tcp_client_addr)

#     while True:
#         #5 recv/send接收发送数据
#         print('-------------waiting datd---------------')
#         server_recv_data = tcp_client.recv(2048)
#         if server_recv_data:
#             print('client receve data is:',server_recv_data.decode('UTF-8'))
#             #服务器回复数据
#             tcp_client.send('消息已经收到'.encode('UTF-8'))
#         else:
#             tcp_client.close()
#             break
        
# #6 关闭套接字，不再接收心得客户端接入，不影响已有客户端交互
# tcp_server_1_socket.close()


# '''
# 小结：
#     TCP应用程序开发总结
#         1.TCP客户端程序想要和TCP服务端程序进行通信时必须要先建立连接
#         2.TCP客户端程序一般不需要绑定端口号(会自动随机分配），因为客户端是主动发起建立连接的。
#         3.TCP服务端程序必须绑定端口号,否则客户端找不到这个TCP服务端程序。
#         4.执行1isten后的socket套接字是被动套接字,只负责接收新的客户端的连接请求,不能收发消息。
#         5.当TCP客户端程序和TCP服务端程序连接成功后,TCP服务端会会客户端产生一个新的套接字,收发客户
#         端消息使用该套接字。
#         6.TCP服务端关闭accept返回的新套接字意味着和这个客户端已经通信完毕。
#         7.TCP服务端关闭自己的套接字意味着服务端关闭了,新的客户端不能连接服务端，但是之前已经接成功的客
#         户端还能正常通信。
#         8.当客户端的套接字close后,服务器端的recv会解除阻塞,返回的数据长度为；此时，服务端可
#         以通过返回数据的长度来判断客户端是否已经下线，
#         9.反之,如果服务端为客户端创建的的套接字对象lose后,客户端的recv也会解阻塞,返回的数据长
#         度也为0。
# '''


#***************************************************************************************************************************************************************************
# #----------------UDP
# '''流程：
# 1 导入socket模块
# 2 创建socket到套接字
# 3 bind绑定ip和port
# 4 发送数据
# 5 关闭套接字
#   '''
# #1 导入socket模块
# #
# from socket import *

# #2 创建socket到套接字
#     #参数1  地址类型 family： AddressFamily 地址簇
#     #                         socket.AF_INET      ---ipv4
#     #                         socket.AF_INET6     ---ipv6
#     # 参数2   协议类型
#     #                         socket.SOCK_STREAM --TCP
#     #                         socket.SOCK_DGRAM  --UDP                
# udp_socket = socket(AF_INET,SOCK_DGRAM)       
#                     #这里第一个socket是我们导入的模块，第二个socket则是socket中的socket类，整理正常来说第二个socket的首字母一个大写，不然很容易搞混淆
# #3  bind绑定ip和port
# addr = ("",8080)  #这里值=指服务器(ip,port)元组   <------------------------------************这里ip将服务器绑定到 '0.0.0.0' 表示或者也可以写一个空字符串""        服务器将监听所有可用的网络接口上的连接
# udp_socket.bind(addr)          

# #4  发送数据   这里udp发送数据要使用sendto    要说清楚发送到哪里
# data = '好久不见'.encode('UTF-8')
# addr = ("192.168.111.1",8080)
# udp_socket.sendto(data,addr)            #使用样例  udp_socket.sendto(message, (target_ip, target_port))
        
# #5 关闭套接字
# udp_socket.close()

#***************************************************************************************************************************************************************************#----------------UDP
# '''流程：
# 1 导入socket模块
# 2 创建socket到套接字
# 3 bind绑定ip和port
# 4 接收数据
# 5 关闭套接字
#   '''
# #1 导入socket模块
# #
# from socket import *
# import ultis
# #2 创建socket到套接字
#     #参数1  地址类型 family： AddressFamily 地址簇
#     #                         socket.AF_INET      ---ipv4
#     #                         socket.AF_INET6     ---ipv6
#     # 参数2   协议类型
#     #                         socket.SOCK_STREAM --TCP
#     #                         socket.SOCK_DGRAM  --UDP                
# udp_socket = socket(AF_INET,SOCK_DGRAM)       
#                     #这里第一个socket是我们导入的模块，第二个socket则是socket中的socket类，整理正常来说第二个socket的首字母一个大写，不然很容易搞混淆
# #3  bind绑定ip和port
# addr = ("",8080)  #这里值=指服务器(ip,port)元组   <------------------------------************这里ip将服务器绑定到 '0.0.0.0' 表示或者也可以写一个空字符串""        服务器将监听所有可用的网络接口上的连接
# udp_socket.bind(addr)          

# #4  接收数据   这里udp发送数据要使用recvfrom    要说清楚发送到哪里
# print('___开始接收____')
# bytes_arr,addr = udp_socket.recvfrom(1024)
# data = ultis.decode_data(bytes_arr)
# print(data)
    
# #5 关闭套接字
# udp_socket.close()

#***************************************************************************************************************************************************************************#----------------UDP
# '''流程：
# 1 导入socket模块
# 2 创建socket到套接字
# 3 bind绑定ip和port(广播发时不是必选项)
# 4 设置允许发送广播
# 5.发送数据
# 6 关闭套接字
#   '''
# #1 导入socket模块
# #
# from socket import *
# import ultis
# #2 创建socket到套接字
#     #参数1  地址类型 family： AddressFamily 地址簇
#     #                         socket.AF_INET      ---ipv4
#     #                         socket.AF_INET6     ---ipv6
#     # 参数2   协议类型
#     #                         socket.SOCK_STREAM --TCP
#     #                         socket.SOCK_DGRAM  --UDP                
# udp_socket = socket(AF_INET,SOCK_DGRAM)       
#                     #这里第一个socket是我们导入的模块，第二个socket则是socket中的socket类，整理正常来说第二个socket的首字母一个大写，不然很容易搞混淆
# #3  bind绑定ip和port
# addr = ("",8080)  #这里值=指服务器(ip,port)元组   <------------------------------************这里ip将服务器绑定到 '0.0.0.0' 表示或者也可以写一个空字符串""        服务器将监听所有可用的网络接口上的连接
# udp_socket.bind(addr)          

# #4 设置允许发送广播
# '''
# self: socket,   SOL_SOCKET
# level: int,     SO_BROADCAST--广播
# optname: int,   
#     '''
# udp_socket.setsockopt(SOL_SOCKET,SO_BROADCAST,True)
# #5.发送数据   
# print('___开始发送____')

# data = 'imissyou'.encode('UTF-8')
# addr = ("192.168.111.255",6688)        #这里这个ip地址我们要把他弄成广播的，可以上在线网站转换一下     先在命令行中输入ipconfig查看ip  以及掩码位数
# udp_socket.sendto(data,addr)

# print(data)
    
# #6 关闭套接字
# udp_socket.close()




    
    
#**************************************************************************************************************************************************************************
from socket import *
import threading
import ultis

tcp_socket_server = socket(AF_INET,SOCK_STREAM)
addr_bind = ("",8080)   #这里不写，代表绑定所以本机ip地址
tcp_socket_server.bind(addr_bind)
tcp_socket_server.listen(64)

client_id_num = 0   #链接服务器的客户端id

def client_task(client_id,tcp_client,tcp_client_addr):
    try:
        while True:
            recv_data = tcp_client.recv(2048)
            if not recv_data:
                print(f"客户端 {client_id} 断开连接")
                break
            
            data_send = ultis.decode_data(recv_data)
            print(f'{client_id}接收到了信息： {data_send}')
            tcp_client.send(data_send.encode('UTF-8'))
            print(f'{client_id}发送到了信息： {data_send}')
            
    except Exception as e: 
        print(f"客户端 {client_id} 处理出错: {e}")
        
    finally:
        tcp_client.close()
        
        
if __name__ == "__main__":
    try:
        while True:
            tcp_client,tcp_client_addr = tcp_socket_server.accept()       #将接入服务端的客户端的信息通过提取出来（利用元组的自动解包）
            client_id_num += 1
            print(f'{client_id_num} 已经连接') 
            
            
            sub_task = threading.Thread(target=client_task,args=(client_id_num,tcp_client,tcp_client_addr))    
            
            sub_task.daemon = True   # 开启守护线程
            
            sub_task.start()

    except KeyboardInterrupt:
        print("\n服务器正在关闭...")
    finally:
        tcp_socket_server.close()
        
        
        

# 为了防止后面再回来看的时候看不懂，这里请教了gpt老师
