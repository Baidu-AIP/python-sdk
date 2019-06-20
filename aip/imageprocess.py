# -*- coding: utf-8 -*-

"""
图像处理
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

class AipImageProcess(AipBase):

    """
    图像处理
    """

    __imageQualityEnhanceUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/image_quality_enhance'

    __dehazeUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/dehaze'

    __contrastEnhanceUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/contrast_enhance'

    
    def imageQualityEnhance(self, image, options=None):
        """
            图像无损放大
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__imageQualityEnhanceUrl, data)
    
    def dehaze(self, image, options=None):
        """
            图像去雾
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__dehazeUrl, data)
    
    def contrastEnhance(self, image, options=None):
        """
            图像对比度增强
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__contrastEnhanceUrl, data)
    