                              
├── data
│   ├── cascades                            用来存放haar分类器
│   │   └── haarcascade_frontalface_alt.xml
│   ├── face_import                         存放需要导入数据库的图片
│   │   ├── 100000000001.普京.png
│   │   ├── 100000000002.克林顿.png
│   │   ├── 100000000003.小布什.png
│   │   └── 100000000004.比尔盖茨.png
│   ├── font                                显示中文的字体文件
│   │   └── simhei.ttf  
│   ├── img_search                          存放需要搜索人面部信息的图片
│   │   ├── Selection_001
│   │   │   └── Selection_001.png
│   │   └── Selection_001.png
│   ├── log                                 存放各种log文件
│   └── temp
├── face                                    face包
│   ├── DBConnect.py
│   ├── FaceAPI.py
│   └── __init__.py
├── img_face.py                             对图片里的人进行识别
├── cam_face.py                             摄像头进行人脸识别
└── import.py                               图片信息导入数据库

