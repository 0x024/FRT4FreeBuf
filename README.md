目录树。。。

![image](https://github.com/0x024/FRT/blob/master/data/temp/Selection_002.png)

环境搭建
Ubuntu16.04LTS—–其实其他的版本也可.
python2.7—-本人使用的是python2.7，
MySQLdb ——-python下的Mysql包
Mysql数据库----可以直接百度‘ubuntu搭建lamp环境’进行安装即可
```java  
sudo apt-get install python-pip
sudo apt-get install libmysqlclient-dev
pip install mysql-python
```
OpenCV 3.2.0——-关于如何安装OpenCV，这里就简单的说一下下，
安装的依赖包:
```java  
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```
从github上下载OpenCV最新的源码:
```java  
git clone https://github.com/opencv/opencv.git       #这个是最新的OpenCV 公布在github上的代码
git clone https://github.com/opencv/opencv_contrib.git #这个里面有一些模块，比如freetype，face，等需要用到
```
官网的教程里面将两个包分开进行编译，但是里面的许多包我们确实用不到，所以，最好的办法，就是将./opencv_contrib/moudles/freetype和face文件直接复制到./opencv/moudles/下

```java  
cd ~/opencv
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j4  #这里的-j4代表怎么说好呢，反正越大，编译的速度越快
sudo make install
```
这里说一下了。在运行cmake的时候，需要下载几个文件，比如
```java  
ippicv_linux_20151201.tgz，
```
需要挂代理，，关于如何在ubuntu上安装shadowsocks科学上网，我的博客也有写过，
