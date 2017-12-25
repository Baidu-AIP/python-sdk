
# -*- coding: utf-8 -*-

"""
图像识别
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

class AipOcr(AipBase):

    """
    图像识别
    """

    __generalBasicUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

    __accurateBasicUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'

    __generalUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general'

    __accurateUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate'

    __generalEnhancedUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_enhanced'

    __webImageUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage'

    __idcardUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard'

    __bankcardUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard'

    __drivingLicenseUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/driving_license'

    __vehicleLicenseUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license'

    __licensePlateUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate'

    __businessLicenseUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/business_license'

    __receiptUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/receipt'

    __tableRecognizeUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request'

    __tableResultGetUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result'

    
    def basicGeneral(self, image, options=None):
        """
            通用文字识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__generalBasicUrl, data)
    
    def basicGeneralUrl(self, url, options=None):
        """
            通用文字识别
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__generalBasicUrl, data)
    
    def basicAccurate(self, image, options=None):
        """
            通用文字识别（高精度版）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__accurateBasicUrl, data)
    
    def general(self, image, options=None):
        """
            通用文字识别（含位置信息版）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__generalUrl, data)
    
    def generalUrl(self, url, options=None):
        """
            通用文字识别（含位置信息版）
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__generalUrl, data)
    
    def accurate(self, image, options=None):
        """
            通用文字识别（含位置高精度版）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__accurateUrl, data)
    
    def enhancedGeneral(self, image, options=None):
        """
            通用文字识别（含生僻字版）
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__generalEnhancedUrl, data)
    
    def enhancedGeneralUrl(self, url, options=None):
        """
            通用文字识别（含生僻字版）
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__generalEnhancedUrl, data)
    
    def webImage(self, image, options=None):
        """
            网络图片文字识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__webImageUrl, data)
    
    def webImageUrl(self, url, options=None):
        """
            网络图片文字识别
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__webImageUrl, data)
    
    def idcard(self, image, id_card_side, options=None):
        """
            身份证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['id_card_side'] = id_card_side

        data.update(options)

        return self._request(self.__idcardUrl, data)
    
    def bankcard(self, image, options=None):
        """
            银行卡识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__bankcardUrl, data)
    
    def drivingLicense(self, image, options=None):
        """
            驾驶证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__drivingLicenseUrl, data)
    
    def vehicleLicense(self, image, options=None):
        """
            行驶证识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicleLicenseUrl, data)
    
    def licensePlate(self, image, options=None):
        """
            车牌识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__licensePlateUrl, data)
    
    def businessLicense(self, image, options=None):
        """
            营业执照识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__businessLicenseUrl, data)
    
    def receipt(self, image, options=None):
        """
            通用票据识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__receiptUrl, data)
    
    def tableRecognitionAsync(self, image, options=None):
        """
            表格文字识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__tableRecognizeUrl, data)
    
    def getTableRecognitionResult(self, request_id, options=None):
        """
            表格识别结果
        """
        options = options or {}

        data = {}
        data['request_id'] = request_id

        data.update(options)

        return self._request(self.__tableResultGetUrl, data)
    
    def tableRecognition(self, image, options=None, timeout=10000):
        """
            tableRecognition
        """
        
        result = self.tableRecognitionAsync(image)

        if 'error_code' in result:
            return result
        
        requestId = result['result'][0]['request_id']
        for i in range(int(math.ceil(timeout / 1000.0))):
            result = self.getTableRecognitionResult(requestId, options)
            
            # 完成
            if int(result['result']['ret_code']) == 3: 
                break
            time.sleep(1)

        return result