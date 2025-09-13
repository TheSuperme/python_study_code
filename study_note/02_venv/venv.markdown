

## 建议去看看一些大佬写的笔记

[Python中的venv虚拟环境详解_python虚拟环境venv-CSDN博客](https://blog.csdn.net/weixin_42998312/article/details/143863224)

[Python的虚拟环境(venv)是什么？-CSDN博客](https://blog.csdn.net/luanxiyuan/article/details/99711330)

[创建和使用 Python 虚拟环境（使用Python自带的venv模块）_python创建venv-CSDN博客](https://blog.csdn.net/peanutwang/article/details/144555317)

[Python虚拟环境使用教程（以虚拟环境管理工具venv为例）（virtualenv、venv、pyenv、virtualenvwrapper、conda不同管理工具对比）-CSDN博客](https://blog.csdn.net/Dontla/article/details/132019176)



Python虚拟环境（venv）是一个非常重要的工具，让我详细给你讲解一下。

## 什么是虚拟环境？

虚拟环境是一个**独立的Python运行环境**，它包含：

- 独立的Python解释器副本
- 独立的包安装目录
- 独立的环境变量设置

简单理解：就像给每个项目创建一个**独立的Python世界**。

## 为什么需要虚拟环境？

### 问题场景：

```
全局环境问题：
项目A需要 requests==2.25.1
项目B需要 requests==2.28.0
如果都装在全局，就会冲突！
```

### 解决方案：

```
项目A虚拟环境：requests==2.25.1
项目B虚拟环境：requests==2.28.0
全局环境：保持干净
```

## 基本使用方法

### 1. 创建虚拟环境

```
# 创建名为myproject的虚拟环境
python -m venv myproject

# 或者指定Python版本（如果有多个版本）
python3.9 -m venv myproject
```

### 2. 激活虚拟环境

```
# Windows
myproject\Scripts\activate

# macOS/Linux
source myproject/bin/activate

# 激活成功后，命令行前面会显示环境名：
(myproject) C:\Users\YourName>
```

### 3. 在虚拟环境中工作

```
# 现在安装的包只会装在这个虚拟环境中
pip install requests
pip install flask
pip list  # 只显示当前环境的包
```

### 4. 退出虚拟环境

```
deactivate
# 命令行前的(myproject)会消失
```

## 实际项目流程示例

### 新项目开发：

```
# 1. 创建项目目录
mkdir my_tcp_server
cd my_tcp_server

# 2. 创建虚拟环境
python -m venv venv

# 3. 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. 安装需要的包
pip install socket
pip install threading

# 5. 开发代码
# 创建你的Python文件...

# 6. 保存依赖列表
pip freeze > requirements.txt
```

### 项目协作：

```
# 其他人拿到你的项目后：
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活环境
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 现在环境和你的完全一样！
```

## 目录结构详解

创建虚拟环境后的目录结构：

```
myproject/
├── Scripts/          # Windows下的可执行文件
│   ├── activate      # 激活脚本
│   ├── python.exe    # Python解释器副本
│   └── pip.exe       # pip工具
├── Lib/              # 包安装目录
│   └── site-packages/# 第三方包存放位置
└── pyvenv.cfg        # 配置文件
```

## 常用命令总结

```
# 创建环境
python -m venv 环境名

# 激活环境
# Windows: 环境名\Scripts\activate
# macOS/Linux: source 环境名/bin/activate

# 退出环境
deactivate

# 查看当前环境包
pip list

# 导出依赖
pip freeze > requirements.txt

# 安装依赖
pip install -r requirements.txt

# 删除虚拟环境（直接删除文件夹即可）
rm -rf 环境名
```

## 最佳实践建议

### 1. 项目结构：

```
my_project/
├── venv/             # 虚拟环境（通常加入.gitignore）
├── src/              # 源代码
├── requirements.txt  # 依赖列表
├── README.md
└── .gitignore
```

### 2. .gitignore设置：

```
# 不要把虚拟环境上传到git
venv/
env/
.env
```

### 3. requirements.txt管理：

```
# 只导出项目真正需要的包，不包括开发工具
pip freeze > requirements.txt

# 或者手动维护requirements.txt
echo "requests==2.28.0" > requirements.txt
echo "flask==2.2.0" >> requirements.txt
```
