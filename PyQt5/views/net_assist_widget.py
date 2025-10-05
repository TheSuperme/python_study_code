from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
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
        self.is_connected = False # 添加一个连接状态的标志
        self.ui.setupUi(self)
        self.init_ui()
        
    def thread_run_func(self,target_ip,target_port):
        
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
                #如果执行到这里则说明
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
        self.tcp_client.close()
        self.is_connected = False
        print("连接已关闭")
        # 再次发射信号，通知主线程更新UI为“未连接”状态
        self.signal_update_status.emit(False, "", 0)
          
            
    def on_comnnect_clicked(self):
        if self.is_connected:       #如果之前已经连接，那么当再次点击就是断开连接
            self.is_connected = False
            if self.tcp_client:     #如果客户端存在，那么就关闭
                try:
                    self.tcp_client.shutdown(socket.SHUT_RDWR)
                    self.tcp_client.close()
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
        
        thread_1 = threading.Thread(target= self.thread_run_func,args=(target_ip,target_port)) 
        thread_1.daemon = True #开启线程守护
        thread_1.start()
        
    # 4. ***** 创建槽函数 *****
    """
    这个是槽函数，在主线程中被调用，用于安全地更新UI
    """
    def append_received_data(self, text):
         # 使用 append 而不是 setText，这样可以保留历史记录
        self.ui.edit_recv_data.append(text)
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
            self.ui.btn_connect.setText("连接服务器")
            self.ui.edit_local_port.clear() # 清空本地端口显示
            
            
    def init_ui(self):
        self.ui.btn_connect.clicked.connect(self.on_comnnect_clicked)
        self.ui.edit_target_ip.setText("127.0.0.1")
        self.ui.edit_target_port.setText("8080")
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