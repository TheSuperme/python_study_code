from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import socket
import threading 

import tool.ultis as ultis 
from ui.Ui_net_assist_widget import Ui_Net_assist_widget


class Net_assist_widget(QWidget):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
    def __init__(self,parent=None):
        super().__init__()
        self.ui = Ui_Net_assist_widget()
        self.ui.setupUi(self)
        self.init_ui()
        
    def thread_run_func(self,target_ip,target_port):
            tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #创建一个tcp的socket对象
            try: 
                target_addr = (target_ip,int(target_port))
                tcp_client.connect(target_addr)   #绑定ip和端口
                print('服务器连接成功')
                sockkname = tcp_client.getsockname()  #获取本地分配的ip和端口号
                print("sockkname: ",sockkname)
                (local_ip,local_port) = sockkname
                print(f"local ip{local_ip},local port{local_port}")
                self.ui.btn_connect.setText("断开连接(已连接)")
                cb_local_ip_index = self.ui.cb_local_ip.findText(local_ip)  #获取当前组件cb_local_ip选择的ip的索引
                self.ui.cb_local_ip.setCurrentIndex(cb_local_ip_index)     #设置为当前的本地ip
                self.ui.edit_local_port.setText(str(local_port))        #设置当前组件edit_local_port的数据
                
                recv_byte_data = tcp_client.recv(2048)
                send_str_data = ultis.decode_data(recv_byte_data)
                self.ui.edit_recv_data.setText(send_str_data)
                print('str_data: ',send_str_data)
                print('-------------------------')
            except Exception as e:
                print(e)
            
            finally:
                tcp_client.close()    
            
    def on_comnnect_clicked(self):
        target_ip = self.ui.edit_target_ip.text()
        target_port = self.ui.edit_target_port.text()
        print(f'链接服务器{target_ip}:{target_port}')

        if target_ip == ' ' or target_port == ' ':
            print("请输入ip和端口号")
            return
       
        thread_1 = threading.Thread(target= self.thread_run_func,args=(target_ip,target_port)) 
        thread_1.daemon = True #开启线程守护
        thread_1.start()
        
        
        
    def init_ui(self):
        self.ui.btn_connect.clicked.connect(self.on_comnnect_clicked)
        self.ui.edit_target_ip.setText("127.0.0.1")
        self.ui.edit_target_port.setText("8080")
        for ip in ultis.get_local_ip():                     #这两行可以等价于：  local_ips = ultis.get_local_ip():
            self.ui.cb_local_ip.addItem(ip)                 #                  self.ui.cb_local_ip.addItems(local_ips)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Net_assist_widget()
    w.init_ui()
    
    w.show()    
    sys.exit(app.exec_())   #退出程序 