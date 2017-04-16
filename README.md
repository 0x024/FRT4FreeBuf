## 0x01 环境:
[![](https://img.shields.io/badge/Ubuntu-16.04LTS-brightgreen.svg)]()
[![](https://img.shields.io/badge/Python-2.7.*-brightgreen.svg)]()
[![](https://img.shields.io/badge/OpenCV-3.2.0-brightgreen.svg)]()
[![](https://img.shields.io/badge/Mysql-5.7.*-brightgreen.svg)]()
[![](https://img.shields.io/badge/phpmyadmin-*-brightgreen.svg)]()
[![](https://img.shields.io/badge/ShadowSocks-Linux-brightgreen.svg)]()

```
curl安装：
	sudo apt-get install curl
```

```python
MySQLdb安装：
      sudo apt-get install python-pip     
      sudo apt-get install libmysqlclient-dev
      pip install mysql-python
```
OpenCV 3.2.0——-关于如何安装OpenCV，这里就简单的说一下下，


```
安装依赖包:
      sudo apt-get install build-essential
      sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
      sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev                                   libjasper-dev libdc1394-22-dev
```

```
从github上下载OpenCV最新的源码:
      git clone https://github.com/opencv/opencv.git       #这个是最新的OpenCV 公布在github上的代码
      git clone https://github.com/opencv/opencv_contrib.git #这个里面有一些模块，比如freetype，face，等需要用到
```
官网的教程里面将两个包分开进行编译，但是里面的许多包我们确实用不到，所以，最好的办法，就是将./opencv_contrib/moudles/freetype和face文件夹直接复制到./opencv/moudles/下

``` 
进行安装
	cd ~/opencv
	mkdir release
	cd release
	cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
	make -j4  #这里的-j4代表怎么说好呢，反正越大，编译的速度越快
	sudo make install
```
这里说一下了。在运行cmake的时候，需要下载几个文件，比如
```
ippicv_linux_20151201.tgz，
```
需要挂代理，，关于如何在ubuntu上安装shadowsocks科学上网，我的博客也有写过，


## 0x02 目录树:
![image](https://github.com/0x024/FRT4FreeBuf/blob/master/data/temp/Selection_015.png)


## 0x03 执行:

```
运行前，

	需要将./face/FaceAPI.py中的api_key和api_secret换成你的
	需要在搭建的MYSQL中创建一个FRT数据库，并且事先在FRT中创建一个表，表名和值可任意设置！
	需要将./face/Dbconnect.py中的数据库信息换成自己的
	需要将所有的图片ID设置成12位数字
```


```
python import.py   #将保存在./data/import/目录下的图片特征经分析后，将图片信息导入数据库
```
```
python search.py   #将需要识别的图片放在./data/search/下。运行即可（可放置多张）
```
```
python cam.py   #进行实时人脸识别，可多张脸一起时别
```
