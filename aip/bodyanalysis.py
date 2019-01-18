# -*- coding: utf-8 -*-

"""
人体分析
"""

import re
import sys
import math
import time
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote

class AipBodyAnalysis(AipBase):

    """
    人体分析
    """

    __bodyAnalysisUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis'

    __bodyAttrUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr'

    __bodyNumUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_num'

    __gestureUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture'

    __bodySegUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg'

    
    def bodyAnalysis(self, image, options=None):
        """
            人体关键点识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bodyAnalysisUrl, data)
    
    def bodyAttr(self, image, options=None):
        """
            人体属性识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bodyAttrUrl, data)
    
    def bodyNum(self, image, options=None):
        """
            人流量统计
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bodyNumUrl, data)
    
    def gesture(self, image, options=None):
        """
            手势识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__gestureUrl, data)
    
    def bodySeg(self, image, options=None):
        """
            人像分割
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bodySegUrl, data)
    