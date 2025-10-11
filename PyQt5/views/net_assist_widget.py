from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
import socket
import threading 

import tool.ultis as ultis 
from ui.Ui_net_assist_widget import Ui_Net_assist_widget


class Net_assist_widget(QWidget):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget

    # 1. ***** 定义信号 *****
    # 定义一个带字符串参数的信号，用于从子线程发送接收到的数据到主线程
    signal_recv_data = pyqtSignal(str)
     # 定义一个信号，用于更新连接状态（如按钮文字、IP和端口号等）
    # 参数: (是否连接成功:bool, 本地IP:str, 本地端口:int)
    signal_update_status  = pyqtSignal(bool,str,int)
    
    
    def __init__(self,parent=None):
        super().__init__()
        self.ui = Ui_Net_assist_widget()
        self.tcp_client = None  # 将tcp_client提升为类的属性，方便在其他方法中访问
        self.tcp_serve = None
        self.connected_client_sockets = [] # 新增：用于存储所有连接的客户端套接字列表
        self.server_running = False  # 🔧 新增：控制服务器循环的标志位
        self.is_connected = False # 添加一个连接状态的标志
        self.ui.setupUi(self)
        self.init_ui()
    #tcp_client 的线程函数    
    def thread_run_tcp_client(self,target_ip,target_port):
        self.tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #创建一个tcp的socket对象
        try:
            target_addr = (target_ip,int(target_port))
            self.tcp_client.connect(target_addr)   #绑定ip和端口
            print('服务器连接成功')
        except Exception as e:
            print(f"连接服务器失败: {e}")
            # 发射信号通知主线程连接失败
            self.signal_update_status.emit(False, "", 0)
            return # 连接失败，线程直接退出
        
         # 连接成功,更新一下状态位
        self.is_connected = True
        sockkname = self.tcp_client.getsockname()  #获取本地分配的ip和端口号
        print("sockkname: ",sockkname)
        (local_ip,local_port) = sockkname
        print(f"local ip{local_ip},local port{local_port}")
        #发射信号通知主线程连接成功
        self.signal_update_status.emit(True,local_ip,local_port)
        
        #现在开始循环接收数据：
        while self.is_connected:
            try:
                # 等待接收数据，这里会阻塞直到收到数据或连接断开
                recv_byte_data = self.tcp_client.recv(2048)
                # 如果接收到的数据为空，说明服务器主动断开了连接
                if not recv_byte_data:
                    print("服务器断开了连接")
                    break # 退出接收循环
               
                send_str_data = ultis.decode_data(recv_byte_data)
                print('str_data: ',send_str_data)
                # 3. ***** 发射信号，而不是直接操作UI *****
                # 发射信号，将接收到的数据字符串发送出去
                self.signal_recv_data.emit(send_str_data)
            
            except Exception as e:
                # 发生异常，很可能是连接被重置
                print(f"接收数据异常: {e}")
                break # 退出接收循环
        
        # 循环结束，意味着连接已断开
        # 修改这里，在关闭之前检查self.tcp_client是否为None
        if self.tcp_client: #
            self.tcp_client.close() #
        self.is_connected = False
        print("连接已关闭")
        # 再次发射信号，通知主线程更新UI为“未连接”状态
        self.signal_update_status.emit(False, "", 0)
     
    def hand_new_client(self,client_socket,client_addr): 
        try:  
            while self.server_running:  # 🔧 修改：检查服务器运行状态
                #5 recv/send接收发送数据
                print('-------------waiting datd---------------')
                server_recv_data_byte = client_socket.recv(2048)   #等待客户端发送数据
                if not server_recv_data_byte:  # 🔧 新增：检查空数据
                    print(f"客户端 {client_addr} 断开连接")
                    break
                
                server_recv_data = ultis.decode_data(server_recv_data_byte)
                if server_recv_data:
                    print('client receve data is:',server_recv_data)
                    #服务器回复数据
                    client_socket.send('消息已经收到'.encode('UTF-8'))
                    self.signal_recv_data.emit("recv:" + server_recv_data)
        except Exception as e:
            print(e)
        finally:
            # 确保客户端套接字在处理结束后关闭
            if client_socket:
                print(f"关闭客户端 {client_addr} 连接")
                try:
                    client_socket.shutdown(socket.SHUT_RDWR) # 尝试优雅关闭
                except OSError:
                    pass # 如果客户端已经关闭，shutdown会报错
                client_socket.close()
                # 从列表中移除已断开的客户端套接字
                if client_socket in self.connected_client_sockets:
                    self.connected_client_sockets.remove(client_socket)
    #tcp_serve 的线程函数 
    def thread_run_tcp_serve(self,serve_ip,serve_port):
        self.tcp_serve = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #创建一个tcp的socket对象
        self.tcp_serve.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        addr = (serve_ip,int(serve_port))
        self.tcp_serve.bind(addr)
        self.tcp_serve.listen(64)   #变为被动模式
         # 连接成功,更新一下状态位
        self.is_connected = True
        self.server_running = True  # 🔧 新增：标记服务器开始运行
        self.connected_client_sockets.clear() # 启动服务器时清空客户端列表
        self.signal_update_status.emit(True, "", 0)
        # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
        # tcp_client_socket用来为这个客户端服务
        # self.tcp_serve就可以省下来专门等待其他新客户端的链接 
        # 🔧 关键修改2：设置超时，避免accept永久阻塞
        self.tcp_serve.settimeout(1.0)
        try: 
            while self.server_running:  # 🔧 修改：使用标志位控制循环
                try: 
                    client_socket,client_addr = self.tcp_serve.accept()       #将接入服务端的客户端的信息通过提取出来（利用元组的自动解包）
                    print('有新的客户端接入：',client_addr)
                    # 将客户端套接字添加到列表中
                    self.connected_client_sockets.append(client_socket)
                    # 针对这个客户端启动一个线程来处理其数据
                    thread = threading.Thread(target= self.hand_new_client,args=(client_socket,client_addr))
                    thread.daemon = True
                    thread.start()
                except socket.timeout:  # 🔧 新增：处理超时，继续循环
                    continue
                except Exception as e:
                    if self.server_running:  # 只在服务器运行时打印错误
                        print(f"Accept异常: {e}")
                        self.signal_update_status.emit(False, "", 0)
                    break
        except Exception as e:
            print(e)
        finally:
             # ✅ 修复：简化关闭逻辑，只保留一份
            print("开始清理服务器资源...")
            
            # 关闭所有客户端连接
            for sock in list(self.connected_client_sockets):
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                except:
                    pass
                try:
                    sock.close()
                except:
                    pass
            self.connected_client_sockets.clear()
            
            # 关闭服务器socket
            if self.tcp_serve:
                try:
                    self.tcp_serve.close()
                except:
                    pass
                self.tcp_serve = None
            
            self.is_connected = False
            self.server_running = False
            print("TCP服务器已完全关闭")
            self.signal_update_status.emit(False, "", 0)
            
    #当设置模式为tcp client时执行的函数
    def handle_client_connect(self):
        if self.is_connected:       #如果之前已经连接，那么当再次点击就是断开连接
            self.is_connected = False  # 🔧 先设置标志位
            if self.tcp_client:     #如果客户端存在，那么就关闭
                try:
                    self.tcp_client.shutdown(socket.SHUT_RDWR)
                    self.tcp_client.close()
                    self.tcp_client = None # 确保在关闭后设置为None
                    self.signal_update_status.emit(False, "", 0)
                except Exception as e:
                    print(f"关闭socket时出错: {e}")
            return
        #如果执行到这里，说明此时还没有连接，那么我们就开始连接  
        target_ip = self.ui.edit_target_ip.text()
        target_port = self.ui.edit_target_port.text()
        print(f'链接服务器{target_ip}:{target_port}')

        if target_ip == '' or target_port == '':
            print("请输入ip和端口号")
            return
        
        thread_1 = threading.Thread(target= self.thread_run_tcp_client,args=(target_ip,target_port)) 
        thread_1.daemon = True #开启线程守护
        thread_1.start()
    
    #当设置模式为tcp serve时执行的函数
    def handle_server_run(self):
        if self.is_connected:       #如果之前已经连接，那么当再次点击就是断开连接
            self.server_running = False  # 🔧 关键修改3：设置标志位，停止accept循环
            self.is_connected = False
            if self.tcp_serve:     #如果客户端存在，那么就关闭
                try:
                    self.tcp_serve.close()  # 直接关闭，不调用shutdown
                    self.tcp_serve = None # 确保在关闭后设置为None
                    self.signal_update_status.emit(False, "", 0)
                except Exception as e:
                    print(f"关闭socket时出错: {e}")
                # 关闭所有客户端连接
            for sock in list(self.connected_client_sockets):
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                except:
                    pass
            self.connected_client_sockets.clear()
            self.signal_update_status.emit(False, "", 0)
            return
        
        server_ip = self.ui.edit_target_ip.text()
        server_port = self.ui.edit_target_port.text()
        print("开启服务器")
        if server_port == '':
            print("请输入端口号")
            return
        thread_2 = threading.Thread(target= self.thread_run_tcp_serve,args=(server_ip,server_port)) 
        thread_2.daemon = True #开启线程守护
        thread_2.start()
        
    #连接服务器按钮       
    def on_comnnect_clicked(self):
        if self.is_connected:       # If already connected, disconnect first
            self.is_connected = False
            if self.tcp_client:
                try:
                    self.tcp_client.shutdown(socket.SHUT_RDWR)
                    self.tcp_client.close()
                except Exception as e:
                    print(f"Error shutting down client socket: {e}")
                finally:
                    self.tcp_client = None
                    
            elif self.tcp_serve:
                # 🔧 关键修改5：服务器关闭逻辑
                self.server_running = False
                try:
                    self.tcp_serve.close()
                except Exception as e:
                    print(f"Error shutting down server socket: {e}")
                finally:
                    self.tcp_serve = None
        # 关闭所有客户端连接
            for sock in list(self.connected_client_sockets):
                try:
                    sock.shutdown(socket.SHUT_RDWR)
                    sock.close()
                except:
                    pass
            self.connected_client_sockets.clear()
        
            self.signal_update_status.emit(False, "", 0)
            return
        current_index = self.ui.cb_mode.currentIndex()
        if current_index == 0:
            print("当前的设置模式为:TCP客户端")
            self.handle_client_connect()
        elif current_index == 1:
            print("当前的设置模式为:TCP服务器")
            self.handle_server_run()
        else:   
            print("当前的设置模式为:UDP")
            
        
    def on_send_clicked(self):
        # 先判断当前模式
        current_index = self.ui.cb_mode.currentIndex()
        user_input_text = self.ui.edit_send_data.toPlainText()
        if user_input_text == '':
            return # 没有要发送的数据

        if current_index == 0: # TCP客户端模式
            if not self.is_connected or not self.tcp_client:
                print("请先链接服务器")
                return
            try:
                print(f"tcp client发送了: {user_input_text}")
                self.tcp_client.send(user_input_text.encode("UTF-8"))
                self.signal_recv_data.emit("send:" + user_input_text)
            except Exception as e:
                print(f"客户端发送数据失败: {e}")
                # 可以在此处考虑断开连接并更新UI
                self.is_connected = False
                if self.tcp_client:
                    self.tcp_client.close()
                    self.tcp_client = None
                self.signal_update_status.emit(False, "", 0)

        elif current_index == 1: # TCP服务器模式
            if not self.is_connected or not self.tcp_serve: # 检查服务器是否在监听
                print("服务器未开启或未在监听")
                return

            if not self.connected_client_sockets:
                print("没有客户端连接，无法发送数据")
                return

            print(f"tcp server向所有客户端发送了: {user_input_text}")
            # 遍历所有连接的客户端，逐一发送数据
            for client_sock in list(self.connected_client_sockets): # 使用list()创建副本，以防止在循环中修改列表
                try:
                    client_sock.send(user_input_text.encode("UTF-8"))
                    self.signal_recv_data.emit(f"send to {client_sock.getpeername()}:" + user_input_text)
                except Exception as e:
                    print(f"向客户端 {client_sock.getpeername()} 发送数据失败: {e}")
                    # 如果发送失败，说明客户端可能已经断开，将其从列表中移除
                    if client_sock in self.connected_client_sockets:
                        self.connected_client_sockets.remove(client_sock)
                    try:
                        client_sock.close()
                    except Exception:
                        pass # 忽略关闭错误

        else: # UDP模式 (此处省略，根据您的UDP实现来添加)
            print("当前的设置模式为:UDP, 发送逻辑待实现")        
    #更改设置模式是触发        
    def on_mode_change(self):
        self.is_connected = False
        current_index = self.ui.cb_mode.currentIndex()
        if current_index == 0:
            print("当前的设置模式为:TCP客户端")
            self.ui.label_ip.setText("服务器ip:")
            self.ui.label_port.setText("服务器端口号:")
            self.ui.edit_target_ip.setText("127.0.0.1")
            self.ui.edit_target_port.setText("8080")
            self.ui.label_local_ip.show()
            self.ui.cb_local_ip.show()
            self.ui.label_local_port.show()
            self.ui.edit_local_port.show()
            self.ui.label_3.hide()
            self.ui.comboBox.hide()

        elif current_index == 1:
            print("当前的设置模式为:TCP服务器")
            self.ui.label_ip.setText("本地ip:")
            self.ui.label_port.setText("本地端口号:")
            self.ui.edit_target_ip.setText("192.168.74.1")
            self.ui.edit_target_port.setText("8080")
            self.ui.label_local_ip.hide()
            self.ui.cb_local_ip.hide()
            self.ui.label_local_port.hide()
            self.ui.edit_local_port.hide()
            self.ui.label_3.show()
            self.ui.comboBox.show()
        else:   
            print("当前的设置模式为:UDP")
    # 4. ***** 创建槽函数 *****
    """
    这个是槽函数，在主线程中被调用，用于安全地更新UIsocket.timeout
    """
    def append_received_data(self, text):
        # 使用 append 而不是 setText，这样可以保留历史记录
        # 获取当前时间
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("当前时间:", current_time)
        real_text = f"[{current_time}]:{text}"
        self.ui.edit_recv_data.append(real_text)
        # 可以添加自动滚动到底部的功能
        self.ui.edit_recv_data.ensureCursorVisible()
    """
        这个是槽函数，用于根据连接状态更新UI
    """    
    def update_connection_status(self, is_connected, local_ip, local_port):
        if is_connected:
            self.ui.btn_connect.setText("断开连接(已连接)")
            cb_local_ip_index = self.ui.cb_local_ip.findText(local_ip)  #获取当前组件cb_local_ip选择的ip的索引
            if cb_local_ip_index != -1:   #确保获取的索引值有效
                self.ui.cb_local_ip.setCurrentIndex(cb_local_ip_index)     #设置为当前的本地ip
            self.ui.edit_local_port.setText(str(local_port))        #设置当前组件edit_local_port的数据
        else:
            self.ui.btn_connect.setText("连接网络")
            self.ui.edit_local_port.clear() # 清空本地端口显示
            
            
    def init_ui(self):
        self.ui.btn_connect.clicked.connect(self.on_comnnect_clicked)       #绑定（链接按钮）的相关回调函数
        self.ui.btn_send.clicked.connect(self.on_send_clicked)              #绑定（发送）的相关回调函数
        self.ui.cb_mode.currentIndexChanged.connect(self.on_mode_change)    #更改TCP设置模式或者UDP    当设置模式的索引值变化时执行函数on_mode_change
        self.on_mode_change()
         # 5. ***** 连接信号和槽 *****
        self.signal_recv_data.connect(self.append_received_data)
        self.signal_update_status.connect(self.update_connection_status)
        
        for ip in ultis.get_local_ip():                     #这两行可以等价于：  local_ips = ultis.get_local_ip():
            self.ui.cb_local_ip.addItem(ip)                 #                  self.ui.cb_local_ip.addItems(local_ips)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Net_assist_widget()
    
    w.show() 
     
    sys.exit(app.exec_())   #退出程序 
    