# README in other languages
* [English](./README-EN.md)

# 3aDioStation
使用Python开发的GUI远程安装工具。
是FBI的servefiles的GUI实现。


# 使用方法
使用时需要安装Python 3，如果你还没有安装过，请到[这里](https://www.python.org)下载并安装。

确保3DS和电脑连接到同一个局域网之下。

启动FBI，选择Remote Install（远程安装），屏幕上会显示你的3DS的IP。

运行threadiostation目录下的gui.py。

点击浏览选择要安装的文件，**支持的格式为.cia, .tik, .cetk, .3dsx**。

在3DS IP的输入框内填入3DS的IP。

点击启动按钮启动服务器。

FBI会提示是否从该服务器接受URL，选择是。

然后就开始安装叻:)

安装完成后点击停止关闭服务器或者直接退出也行。

# 关于本地化
软件的文本不多，使用了非常简单的方式进行本地化，在加载时从json文件中读取本地化文本加载为字典并显示在对应组件上。
如果你希望帮助翻译成其他语言，请参阅internationalization文件夹中的json文件格式进行翻译并提交请求。
