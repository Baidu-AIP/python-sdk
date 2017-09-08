# -*- coding: utf-8 -*-

import re
import sys
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote
from .base import Image
from .base import StringIO

class AipImageCensor(AipBase):
    """
        Aip ImageCensor
    """

    __antiPornUrl = 'https://aip.baidubce.com/rest/2.0/antiporn/v1/detect'

    __antiPornGifUrl = 'https://aip.baidubce.com/rest/2.0/antiporn/v1/detect_gif'

    __antiTerrorUrl = 'https://aip.baidubce.com/rest/2.0/antiterror/v1/detect'

    __faceAuditUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/face_audit'
    
    __imageCensorCombUrl = 'https://aip.baidubce.com/api/v1/solution/direct/img_censor'
    
    def antiPorn(self, image):
        """
            antiporn
        """

        data = {}
        data['image'] = image

        return self._request(self.__antiPornUrl, data)

    def _validate(self, url, data):
        """
            validate
        """

        if not isinstance(data, dict):
            return True

        if 'images' in data:
            imageB64s = []

            for image in data['images']:
                img = Image.open(StringIO(image))
                imageB64 = base64.b64encode(image).decode()

                format = img.format.upper()
                width, height = img.size

                # 图片格式检查
                if format not in ['JPEG', 'BMP', 'PNG', 'GIF']:
                    return {
                        'error_code': 'SDK109',
                        'error_msg': 'unsupported image format',
                    }

                # 编码后小于4m
                if len(imageB64) >= 4 * 1024 * 1024:
                    return {
                        'error_code': 'SDK100',
                        'error_msg': 'image size error',
                    }

                imageB64s.append(imageB64)

            data['images'] = ','.join(imageB64s)

        elif 'image' in data:
            img = Image.open(StringIO(data['image']))
            data['image'] = base64.b64encode(data['image'])

            format = img.format.upper()
            width, height = img.size

            # gif
            if url == self.__antiPornGifUrl:
                if format != 'GIF':
                    return {
                        'error_code': 'SDK109',
                        'error_msg': 'unsupported image format',
                    }
                return True

            # 图片格式检查
            if format not in ['JPEG', 'BMP', 'PNG', 'GIF']:
                return {
                    'error_code': 'SDK109',
                    'error_msg': 'unsupported image format',
                }

            # 编码后小于4m
            if len(data['image']) >= 4 * 1024 * 1024:
                return {
                    'error_code': 'SDK100',
                    'error_msg': 'image size error',
                }

        return True

    def antiPornGif(self, image):
        """
            antiporn gif
        """

        data = {}
        data['image'] = image

        return self._request(self.__antiPornGifUrl, data)

    def antiTerror(self, image):
        """
            antiterror
        """

        data = {}
        data['image'] = image

        return self._request(self.__antiTerrorUrl, data)

    def faceAudit(self, images, configId=''):
        """
            faceAudit
        """

        # 非数组则处理为数组
        if not isinstance(images, list):
            images = [images]

        data = {
            'configId': configId
        }

        isUrl = images[0].strip()[0:4] == 'http'
        if not isUrl:
            data['images'] = images
        else:            
            data['imgUrls'] = ','.join([
                quote(url) for url in images
            ])

        return self._request(self.__faceAuditUrl, data)

    def imageCensorComb(self, image, scenes='antiporn', options=None):
        """
            imageCensorComb
        """

        if not isinstance(scenes, list):
            scenes = scenes.split(',')
        
        data = {
            'scenes': scenes,
        }

        isUrl = image.strip()[0:4] == 'http'
        if not isUrl:
            data['image'] = base64.b64encode(image)
        else:
            data['imgUrl'] = image

        data = dict(data, **(options or {}))

        return self._request(self.__imageCensorCombUrl, json.dumps(data), {
            'Content-Type': 'application/json',
        })

