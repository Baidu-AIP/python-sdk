# 安装Python SDK

## 目录结构
```
    ├── aip                   // SDK目录
    │   ├── __init__.py       // 导出类
    │   ├── base.py           // aip基类
    │   ├── speech.py         // 语音
    │   ├── face.py           // 人脸
    │   ├── ocr.py            // OCR
    │   ├── nlp.py            // NLP
    │   ├── kg.py             // 知识图谱
    │   ├── imagecensor.py    // 图像审核
    │   └── imageclassify.py  // 图像识别
    └── setup.py              //setuptools安装
```

**支持 Python版本：2.7.+ ,3.+**

**安装步骤如下：**

1. ``` pip install git+https://github.com/Baidu-AIP/python-sdk.git@master ```

2. ``` from aip import 对应服务 ```即可


# 使用文档

参考[官方网站](http://ai.baidu.com/docs#/Begin/top)
