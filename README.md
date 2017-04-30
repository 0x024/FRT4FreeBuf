## 0x00 预览：
![image](https://github.com/0x024/FRT4FreeBuf/blob/master/data/temp/exp.png)
## 0x01 环境:


- 最新环境配置请到我的博客查看

- [www.0x024.com](http://www.0x024.com) 

- 星期日, 30. 四月 2017 09:28下午 


## 0x02 目录树:
![image](https://github.com/0x024/FRT4FreeBuf/blob/master/data/temp/tree.png)


## 0x03 执行:

```
运行前，

	需要将./face/FaceAPI.py中的api_key和api_secret换成你的
	(为了便于您测试,我以将我的key放在里面，为了防止多人使用outer_id冲突，希望您后期换成自己的)
	需要将./face/FaceAPI.py中的outer_id设置成自己喜欢的标识
	需要在搭建的MYSQL中创建一个FRT(要求排列顺序规则为：utf8_general_ci)数据库，并且事先在FRT
	中创建一个表，表名和值可任意设置！
	需要将./face/Dbconnect.py中的数据库信息换成自己的
	需要将所有的图片ID设置成12位数字
	如果需要重新导入或者识别同一张照片，需要在.data/log/*.log 删除对应log即可
```


```
python import.py   #将保存在./data/import/目录下的图片特征经分析后，将图片信息导入数据库，只可单人照片，且要求图片清晰度较高
```
```
python search.py   #将需要识别的图片放在./data/search/下。完成后保存在本目录下，（可放置多张）
```
```
python cam.py   #进行实时人脸识别，可多张脸一起时别
```
