# '''初识pyqt窗口'''

# from PyQt5.QtWidgets import QApplication,QWidget   #QApplication 是所有PyQt5 GUI应用程序的核心（PyQt5应用程序都必须创建一个且只能创建一个QApplication对象）   QWidget 是PyQt5中所有用户界面对象的基类。
# from PyQt5.QtGui import QIcon   #QIcon 类用于处理图标图像。
# import sys      #sys 模块是Python的标准库之一，提供了对Python解释器和其运行环境的访问。



# #1.创建应用程序
# app = QApplication(sys.argv)

# #2.创建窗口
# w = QWidget()

# #   设置窗口标题
# w.setWindowTitle('This is a demo')
# #   设置窗口尺寸
# w.resize(800,400)
# #   设置窗口的小图标
# w.setWindowIcon(QIcon('c.png'))
# #   设置鼠标放置在窗口时的提示词
# w.setToolTip('这是一个想念提示')

# #3.显示窗口
# w.show()

# #4.等待窗口停止
# sys.exit(app.exec_())

#-----------------------文本控件-----------------------------------
# '''初识pyqt窗口'''
# from PyQt5.QtWidgets import QApplication,QWidget,QLabel   
# from PyQt5.QtGui import QPixmap   
# import sys      #sys 模块是Python的标准库之一，提供了对Python解释器和其运行环境的访问。

# def init_widget(w:QWidget):
#     #设置窗口标题
#     w.setWindowTitle('This is picture show demo')
#     label = QLabel()
#     pixmap = QPixmap('a.png')
#     label.setPixmap(pixmap)
#     #显示到窗口中
#     label.setParent(w)
#     #改变窗口大小
#     w.resize(pixmap.width(),pixmap.height())

# if __name__ == '__main__':      #这是Python里一个常见的写法，意思是“如果这个文件是直接被运行的（而不是被别人当成工具引入的），那么就执行下面的代码”.
#     #1.创建应用程序
#     app = QApplication(sys.argv)

#     #2.创建窗口
#     w = QWidget()

#     init_widget(w)

#     #3.显示窗口
#     w.show()

#     #4.等待窗口停止
#     sys.exit(app.exec_())
    

#-----------------------输入框控件-----------------------------------
# '''初识pyqt窗口'''
# from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QTextEdit
# from PyQt5.QtGui import QPixmap   
# import sys      #sys 模块是Python的标准库之一，提供了对Python解释器和其运行环境的访问。

# def init_widget(w:QWidget):
#     layout = QVBoxLayout()
    
#     edit_user = QLineEdit()
#     edit_user.setPlaceholderText('请输入账号id')
# #    edit_user.setText('nihao') #设置输入框的默认内容
# #    edit_user.setMaxLength(10)  #限制输入长度---设置最大输入长度
#     layout.addWidget(edit_user)
    
#     edit_pwd = QLineEdit()
#     edit_pwd.setPlaceholderText('请输入密码')
#      #这一步是设置内容显示模式，就比如你再输入密码时为了安全应该是看不到的
#     edit_pwd.setEchoMode(QLineEdit.Password)   
#     layout.addWidget(edit_pwd)
    
#     #多行文本输入
#     edit_text = QTextEdit()
#     edit_text.setPlaceholderText('请输入自我介绍')
#     layout.addWidget(edit_text)
#     w.setLayout(layout)


# if __name__ == '__main__':      #这是Python里一个常见的写法，意思是“如果这个文件是直接被运行的（而不是被别人当成工具引入的），那么就执行下面的代码”.
#     #1.创建应用程序
#     app = QApplication(sys.argv)

#     #2.创建窗口
#     w = QWidget()
#     #设置窗口标题
#     w.setWindowTitle('输入框')
    
#     init_widget(w)

#     #3.显示窗口
#     w.show()

#     #4.等待窗口停止
#     sys.exit(app.exec_())

#-----------------------按钮控件（QPushButton)&&&&&-水平布局-----------------------------------
# '''初识pyqt窗口'''
# from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtGui import QPixmap   
# import sys      #sys 模块是Python的标准库之一，提供了对Python解释器和其运行环境的访问。

# def aaa_shi()->None:
#     print('我也喜欢你')

# def init_widget(w:QWidget):
#     layout = QHBoxLayout()   #创建水平排列的布局        水平--Horizontial    垂直--Vertical
    
#     btn1 = QPushButton()
#     btn1.setText('我喜欢你')
#     btn1.clicked.connect(aaa_shi)  #绑定一个槽函数（我感觉就是嵌入式中的回调函数），当事件发生时执行槽函数
#     layout.addWidget(btn1)
    
#     btn2 = QPushButton('你好')      #这个方式我感觉比btn1那里的好用
#     layout.addWidget(btn2)
    
#     w.setLayout(layout)


# if __name__ == '__main__':      #这是Python里一个常见的写法，意思是“如果这个文件是直接被运行的（而不是被别人当成工具引入的），那么就执行下面的代码”.
#     #1.创建应用程序
#     app = QApplication(sys.argv)

#     #2.创建窗口
#     w = QWidget()
#     #设置窗口标题
#     w.setWindowTitle('输入框')
    
#     init_widget(w)

#     #3.显示窗口
#     w.show()

#     #4.等待窗口停止
#     sys.exit(app.exec_())
    
    
#-----------------------表单布局-----------------------------------
# '''初识pyqt窗口'''
# from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QFormLayout,QLineEdit
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtGui import QPixmap   
# import sys      #sys 模块是Python的标准库之一，提供了对Python解释器和其运行环境的访问。

# def aaa_shi()->None:
#     print('我也喜欢你')

# def init_widget(w:QWidget):
#     layout = QFormLayout(w)  #这里把 w 添加进去就等价于w.setLayout(layout)
    
#     user_id = QLineEdit()
#     user_pwd = QLineEdit()
#     user_pwd.setEchoMode(QLineEdit.Password)
#     user_phone = QLineEdit()
    
#     btn1 = QPushButton('提交')
#     btn1.clicked.connect(aaa_shi)
    
#     layout.addRow('用户名: ',user_id)
#     layout.addRow('密码  : ',user_pwd)
#     layout.addRow('手机号: ',user_phone)
#     layout.addRow(btn1)
    
# if __name__ == '__main__':      #这是Python里一个常见的写法，意思是“如果这个文件是直接被运行的（而不是被别人当成工具引入的），那么就执行下面的代码”.
#     #1.创建应用程序
#     app = QApplication(sys.argv)

#     #2.创建窗口
#     w = QWidget()
#     #设置窗口标题
#     w.setWindowTitle('输入框')
    
#     init_widget(w)

#     #3.显示窗口
#     w.show()

#     #4.等待窗口停止
#     sys.exit(app.exec_())
    

#-----------------------嵌套布局-----------------------------------
# '''初识pyqt窗口'''
# from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QFormLayout,QLineEdit
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtGui import QPixmap   
# import sys      #sys 模块是Python的标准库之一，提供了对Python解释器和其运行环境的访问。


# def aaa_shi()->None:
#     print('我也喜欢你')

# def init_widget(w:QWidget):
#     root_layout = QHBoxLayout(w)  #这里把 w 添加进去就等价于w.setLayout(layout)
    
#     col1 = QVBoxLayout()
#     col1.addWidget(QPushButton('one'))
    
#     col2 = QVBoxLayout()
#     col2.addWidget(QPushButton('one'))
#     col2.addWidget(QPushButton('two'))
    
#     col3 = QVBoxLayout()
#     col3.addWidget(QPushButton('one'))
#     col3.addWidget(QPushButton('two'))
#     col3.addWidget(QPushButton('three'))
    
#     col4 = QVBoxLayout()
#     col4.addWidget(QPushButton('one'))
#     col4.addWidget(QPushButton('two'))
#     col4.addWidget(QPushButton('three'))
#     col4.addWidget(QPushButton('four'))
    
#     root_layout.addLayout(col1)
#     root_layout.addLayout(col2)
#     root_layout.addLayout(col3)
#     root_layout.addLayout(col4)
    
    
# if __name__ == '__main__':      #这是Python里一个常见的写法，意思是“如果这个文件是直接被运行的（而不是被别人当成工具引入的），那么就执行下面的代码”.
#     #1.创建应用程序
#     app = QApplication(sys.argv)

#     #2.创建窗口
#     w = QWidget()
#     #设置窗口标题
#     w.setWindowTitle('输入框')
    
#     init_widget(w)

#     #3.显示窗口
#     w.show()

#     #4.等待窗口停止
#     sys.exit(app.exec_())
    
    
           
#-----------------------对话框布局-----------------------------------
# '''初识pyqt窗口'''
# from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QFormLayout
# from PyQt5.QtWidgets import QPushButton,QLineEdit,QMessageBox
# from PyQt5.QtGui import QPixmap   
# import sys      #sys 模块是Python的标准库之一，提供了对Python解释器和其运行环境的访问。


# def aaa_shi()->None:
#     print('我也喜欢你')
# #    QMessageBox.information(w,'提示','删除成功')        
#     result = QMessageBox.question(w,'提示','确定要删除吗',
#     QMessageBox.Yes | QMessageBox.No,
#     defaultButton = QMessageBox.No
#                                 )
    
#     if result == QMessageBox.Yes:
#         print('删除成功')
#     else:
#         print('取消完成')
        
# def init_widget(w:QWidget):
#     layout = QVBoxLayout(w)
#     btn = QPushButton('删除')  #这里把 w 添加进去就等价于w.setLayout(layout)
#     btn.clicked.connect(aaa_shi)
#     layout.addWidget(btn)
    
    
    
# if __name__ == '__main__':      #这是Python里一个常见的写法，意思是“如果这个文件是直接被运行的（而不是被别人当成工具引入的），那么就执行下面的代码”.
#     #1.创建应用程序
#     app = QApplication(sys.argv)

#     #2.创建窗口
#     w = QWidget()
#     #设置窗口标题
#     w.setWindowTitle('输入框')
    
#     init_widget(w)

#     #3.显示窗口
#     w.show()

#     #4.等待窗口停止
#     sys.exit(app.exec_())
    
    
           
#----------------------小练习----------------------------             
'''初识pyqt窗口'''
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QFormLayout,QLineEdit
from PyQt5.QtWidgets import QPushButton,QRadioButton,QCheckBox
from PyQt5.QtGui import QPixmap   
import sys      #sys 模块是Python的标准库之一，提供了对Python解释器和其运行环境的访问。


def aaa_shi()->None:
    print('我也喜欢你')

def init_widget(w:QWidget):
    root_layout = QVBoxLayout(w)  #这里把 w 添加进去就等价于w.setLayout(layout)
    
    form_layout = QFormLayout()
    
    user_id = QLineEdit()
    form_layout.addRow('用户名:', user_id)

    user_pwd = QLineEdit()
    form_layout.addRow('密码:', user_pwd)
    
    col3 = QHBoxLayout()
    user_gender_1 = QRadioButton('男')
    user_gender_2 = QRadioButton('女')
    col3.addWidget(user_gender_1)
    col3.addWidget(user_gender_2)
    form_layout.addRow('性别',col3)
    
    hobby_layout = QHBoxLayout()
    btn1 = QCheckBox('抽烟')
    btn2 = QCheckBox('喝酒')
    btn3 = QCheckBox('烫头')
    hobby_layout.addWidget(btn1)
    hobby_layout.addWidget(btn2)
    hobby_layout.addWidget(btn3)
    form_layout.addRow('爱好',hobby_layout)
    
    user_motto = QLineEdit()
    form_layout.addRow('个性签名',user_motto)
    
    wife = QLineEdit()
    form_layout.addRow('择偶标准',wife)
    
     # 提交按钮
    submit_button = QPushButton('确认注册')
    
    root_layout.addLayout(form_layout)
    root_layout.addWidget(submit_button)
    
if __name__ == '__main__':      #这是Python里一个常见的写法，意思是“如果这个文件是直接被运行的（而不是被别人当成工具引入的），那么就执行下面的代码”.
    #1.创建应用程序
    app = QApplication(sys.argv)

    #2.创建窗口
    w = QWidget()
    #设置窗口标题
    w.setWindowTitle('输入框')
    
    init_widget(w)

    #3.显示窗口
    w.show()

    #4.等待窗口停止
    sys.exit(app.exec_())