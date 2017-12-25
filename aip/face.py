
# -*- coding: utf-8 -*-

"""
人脸识别
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

class AipFace(AipBase):

    """
    人脸识别
    """

    __detectUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/detect'

    __matchUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/match'

    __identifyUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/identify'

    __verifyUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/verify'

    __userAddUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/add'

    __userUpdateUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/update'

    __userDeleteUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/delete'

    __userGetUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/get'

    __groupGetlistUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/getlist'

    __groupGetusersUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/getusers'

    __groupAdduserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/adduser'

    __groupDeleteuserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/deleteuser'

    
    def detect(self, image, options=None):
        """
            人脸检测
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__detectUrl, data)
    
    def match(self, images, options=None):
        """
            人脸比对
        """
        options = options or {}

        data = {}
        data['images'] = ','.join([
            base64.b64encode(image).decode() for image in images
        ])

        data.update(options)

        return self._request(self.__matchUrl, data)
    
    def identifyUser(self, group_id, image, options=None):
        """
            人脸识别
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__identifyUrl, data)
    
    def verifyUser(self, uid, group_id, image, options=None):
        """
            人脸认证
        """
        options = options or {}

        data = {}
        data['uid'] = uid
        data['group_id'] = group_id
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__verifyUrl, data)
    
    def addUser(self, uid, user_info, group_id, image, options=None):
        """
            人脸注册
        """
        options = options or {}

        data = {}
        data['uid'] = uid
        data['user_info'] = user_info
        data['group_id'] = group_id
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__userAddUrl, data)
    
    def updateUser(self, uid, user_info, group_id, image, options=None):
        """
            人脸更新
        """
        options = options or {}

        data = {}
        data['uid'] = uid
        data['user_info'] = user_info
        data['group_id'] = group_id
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__userUpdateUrl, data)
    
    def deleteUser(self, uid, options=None):
        """
            人脸删除
        """
        options = options or {}

        data = {}
        data['uid'] = uid

        data.update(options)

        return self._request(self.__userDeleteUrl, data)
    
    def getUser(self, uid, options=None):
        """
            用户信息查询
        """
        options = options or {}

        data = {}
        data['uid'] = uid

        data.update(options)

        return self._request(self.__userGetUrl, data)
    
    def getGroupList(self, options=None):
        """
            组列表查询
        """
        options = options or {}

        data = {}

        data.update(options)

        return self._request(self.__groupGetlistUrl, data)
    
    def getGroupUsers(self, group_id, options=None):
        """
            组内用户列表查询
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id

        data.update(options)

        return self._request(self.__groupGetusersUrl, data)
    
    def addGroupUser(self, src_group_id, group_id, uid, options=None):
        """
            组间复制用户
        """
        options = options or {}

        data = {}
        data['src_group_id'] = src_group_id
        data['group_id'] = group_id
        data['uid'] = uid

        data.update(options)

        return self._request(self.__groupAdduserUrl, data)
    
    def deleteGroupUser(self, group_id, uid, options=None):
        """
            组内删除用户
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id
        data['uid'] = uid

        data.update(options)

        return self._request(self.__groupDeleteuserUrl, data)
    
