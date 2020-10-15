# 安装(Installation) Python SDK

## 目录结构(Directory Structure)
```
    ├── aip                   // SDK目录 (SDK Table of contents)
    │   ├── __init__.py       // 导出类 (Export class)
    │   ├── base.py           // aip基类 (aip base class) 
    │   ├── speech.py         // 语音 (Voice)
    │   ├── face.py           // 人脸 (human face)
    │   ├── ocr.py            // OCR
    │   ├── nlp.py            // NLP
    │   ├── kg.py             // 知识图谱 (Knowledge Graph)
    │   ├── imagecensor.py    // 图像审核 (Image Review)
    │   ├── imageclassify.py  // 图像识别 (Image Identification)
    │   └── imagesearch.py    // 图像搜索 (Image Search)
    └── setup.py              //setuptools安装 (setup tools installation)
```

**支持 Python版本(Version)：2.7.+ ,3.+**

**安装步骤如下：**
**The installation steps are as follows：**

1. ``` pip install git+https://github.com/Baidu-AIP/python-sdk.git@master ```

2. ``` from aip import 对应服务 ```即可


# 使用文档 (Use Documentation)

参考[官方网站](http://ai.baidu.com/docs#/Begin/top)
Reference: [Official website] (http://ai.baidu.com/docs#/Begin/top)
