from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_serial_assist_widget import Ui_Serial_assist_widget
import sys



class Serial_assist_widget(QWidget):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
    def __init__(self,parent=None):
        super().__init__()
        self.ui = Ui_Serial_assist_widget()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        pass
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = Serial_assist_widget()
    w.init_ui()
    w.show()    
    sys.exit(app.exec_())   #退出程序 