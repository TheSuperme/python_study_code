# from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
# import sys

# class My_Widget(QWidget):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
#     def __init__(self,title):
#         super().__init__()
#         self.setWindowTitle(title)
#         self.resize(459, 325)
        
#     def on_btn_click(self):
#         print('abcabc')  
        
#     def init_ui(self):
#         btn = QPushButton('点我',self)
#         btn.clicked.connect(self.on_btn_click)
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
    
#     w = My_Widget('这里是窗口标题')
#     w.init_ui()
#     w.show()    
    
#     sys.exit(app.exec_())   #退出程序 

#-----------------------------Qwidget-----------------

# from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
# import sys

# from Ui.Ui_my_widget import Ui_Form

# class My_Widget(QWidget):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#         self.init_ui()
        
#     def on_btn_click(self):
#         print('abcabc')  
        
#     def init_ui(self):
#         pass
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
    
#     w = My_Widget()
#     w.init_ui()
#     w.show()    
#     sys.exit(app.exec_())   #退出程序 
    
    
    
#------------------------QMainWindow--------

# from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
# import sys

# from Ui.Ui_my_mainwindow import Ui_MyMainWindow

# class My_MainWindow(QMainWindow):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MyMainWindow()
#         self.ui.setupUi(self)
#         self.init_ui()
        
#     def on_btn_click(self):
#         print('abcabc')  
        
#     def init_ui(self):
#         pass
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
    
#     w = My_MainWindow()
#     w.init_ui()
#     w.show()    
#     sys.exit(app.exec_())   #退出程序 
    
    
    
    
#------------------------导入主题--------   详情参见    https://github.com/UN-GCPDS/qt-material

# from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
# import sys
# from Ui.Ui_my_mainwindow import Ui_MyMainWindow

# from qt_material import apply_stylesheet

# class My_MainWindow(QMainWindow):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MyMainWindow()
#         self.ui.setupUi(self)
#         self.init_ui()
        
#     def on_btn_click(self):
#         print('abcabc')  
        
#     def init_ui(self):
#         pass
        
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
    
#     # setup stylesheet
#     apply_stylesheet(app, theme='light_amber.xml')
    
#     w = My_MainWindow()
#     w.init_ui()
#     w.show()    
#     sys.exit(app.exec_())   #退出程序 
    


