# 仿win10界面的博客后端服务

前端git地址
https://github.com/jinfeng775/my-win10

![image](https://github.com/jinfeng775/my-win10/blob/main/src/assets/introduce/win%E5%B1%95%E7%A4%BA.png)

### 初始化
```
pip3 install flask
pip3 install nb_log
pip3 install pyinstaller
```
## pyinstaller
PyInstaller是一个用于将Python脚本打包成独立可执行文件的工具。它的原理是将Python脚本及其依赖的库、资源文件等打包成一个单独的可执行文件，使得在其他机器上运行时不需要安装Python解释器和相关库，即可直接运行。

https://blog.csdn.net/Dontla/article/details/131474870

详细打包教程
### 打包命令
```
pyinstaller start.spec   
```
打包完毕后需要将文件 `nb_log_config.py` 文件放入打包好的文件下面.dist\start\里面,这是快捷配置日志级别的入口

然后运行`start.exe` 就行了


