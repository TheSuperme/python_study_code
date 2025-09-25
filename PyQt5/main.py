from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_untitled import Ui_MainWindow
import sys
 
from views.net_assist_widget import Net_assist_widget
from views.serial_assist_widget import Serial_assist_widget

class My_MainWindow(QMainWindow):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()            #aaa

    def init_ui(self):
        w1 = Net_assist_widget(self)
        w2 = Serial_assist_widget(self)
        self.ui.tabWidget.addTab(w1,"网络助手")  #添加标签
        self.ui.tabWidget.addTab(w2,"串口助手")  #添加标签
        
        self.ui.tabWidget.setCurrentIndex(0) #当项目有多个标签时，用于选择一开始的默认显示标签  索引0--标签1  索引1-标签2
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
     
    w = My_MainWindow()
#    w.init_ui()
    w.show()    
    sys.exit(app.exec_())   #退出程序 