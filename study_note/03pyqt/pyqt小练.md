



使用Qt-designer 实现的**最终效果如下**

![image-20250922220437870](https://cdn.jsdelivr.net/gh/TheSuperme/picture_bed@main/202509222204976.png)



## 思路

打开我们的**qt-designer**

采用**框架式开发**：

先创建一个**main.py**当做主文件夹，然后在pyqt中创建==QMainWindow==   ，然后再在pyqt中创建一个==QWidget==，添加其他的组件，但是为了规范性，我们不想让main.py里面有一堆东西，然后会冗余，导致看起来太乱了，所以我们新建一个.py文件，在里面

```
 #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
```

然后后面我们之间在main.py里面调用这个类即可。

![image-20250922222227918](https://cdn.jsdelivr.net/gh/TheSuperme/picture_bed@main/202509222222987.png)



## 大致步骤

———————————————————————————大致步骤—————————————————————————————————

![image-20250922220802199](https://cdn.jsdelivr.net/gh/TheSuperme/picture_bed@main/202509222208276.png)



![image-20250922220637538](https://cdn.jsdelivr.net/gh/TheSuperme/picture_bed@main/202509222223192.png)



![image-20250922221217651](https://cdn.jsdelivr.net/gh/TheSuperme/picture_bed@main/202509222212760.png)

设置好后记得打开vscode中去右键对应的.ui文件，然后编译一下，生成对应的.py文件



```py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_untitled import Ui_MainWindow
import sys
 
from net_assist_widget import Net_assist_widget

class My_MainWindow(QMainWindow):   #我们自己创建了一个面向对象，以后就控制我们的面向对象，这个面向对象继承了QWidget
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        w = Net_assist_widget(self)
        self.ui.tabWidget.addTab(w,"网络助手")  #添加标签
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
     
    w = My_MainWindow()
#    w.init_ui()
    w.show()    
    sys.exit(app.exec_())   #退出程序 
```

![image-20250922221529473](https://cdn.jsdelivr.net/gh/TheSuperme/picture_bed@main/202509222215516.png)

这里就是导入我们前面在qt-designer中生成的.py文件中的类  







![image-20250922222312558](https://cdn.jsdelivr.net/gh/TheSuperme/picture_bed@main/202509222223635.png)

![image-20250922222402135](https://cdn.jsdelivr.net/gh/TheSuperme/picture_bed@main/202509222224221.png)



然后编译生成对应的.py文件



因为是第一次上手用，所以难免有好多东西不太懂，所以我们就可以下去自行找一下资料再看看

## 补充

[手把手教你学习PyQT5：打造精美、功能强大的桌面应用程序（更新中。。）-CSDN博客](https://blog.csdn.net/weixin_42475060/article/details/130327901)

可以再看一下这篇博客

