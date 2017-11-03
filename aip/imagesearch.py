
# -*- coding: utf-8 -*-

"""
图像搜索
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
from .base import StringIO

class AipImageSearch(AipBase):
    """
    图像搜索
    """

    __sameHqAddUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/same_hq/add'

    __sameHqSearchUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/same_hq/search'

    __sameHqDeleteUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/same_hq/delete'

    __similarAddUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/add'

    __similarSearchUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/search'

    __similarDeleteUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/delete'

    
    def sameHqAdd(self, image, options=None):
        """
            相同图检索—入库
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__sameHqAddUrl, data)
    
    def sameHqSearch(self, image, options=None):
        """
            相同图检索—检索
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__sameHqSearchUrl, data)
    
    def sameHqDeleteByImage(self, image, options=None):
        """
            相同图检索—删除
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__sameHqDeleteUrl, data)
    
    def sameHqDeleteBySign(self, cont_sign, options=None):
        """
            相同图检索—删除
        """
        options = options or {}

        data = {}
        data['cont_sign'] = cont_sign

        data = dict(data, **options)

        return self._request(self.__sameHqDeleteUrl, data)
    
    def similarAdd(self, image, options=None):
        """
            相似图检索—入库
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__similarAddUrl, data)
    
    def similarSearch(self, image, options=None):
        """
            相似图检索—检索
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__similarSearchUrl, data)
    
    def similarDeleteByImage(self, image, options=None):
        """
            相似图检索—删除
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__similarDeleteUrl, data)
    
    def similarDeleteBySign(self, cont_sign, options=None):
        """
            相似图检索—删除
        """
        options = options or {}

        data = {}
        data['cont_sign'] = cont_sign

        data = dict(data, **options)

        return self._request(self.__similarDeleteUrl, data)
    