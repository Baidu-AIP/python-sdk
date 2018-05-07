
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

    __detectUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'

    __searchUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/search'

    __userAddUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add'

    __userUpdateUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/update'

    __faceDeleteUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/delete'

    __userGetUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/get'

    __faceGetlistUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist'

    __groupGetusersUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getusers'

    __userCopyUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/copy'

    __userDeleteUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/delete'

    __groupAddUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/add'

    __groupDeleteUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/delete'

    __groupGetlistUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/group/getlist'

    __personVerifyUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/person/verify'

    __faceverifyUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/faceverify'

    __videoSessioncodeUrl = 'https://aip.baidubce.com/rest/2.0/face/v1/faceliveness/sessioncode'

    __videoFacelivenessUrl = 'https://aip.baidubce.com/rest/2.0/face/v1/faceliveness/verify'

    
    def detect(self, image, image_type, options=None):
        """
            人脸检测
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type

        data.update(options)

        return self._request(self.__detectUrl, data)
    
    def search(self, image, image_type, options=None):
        """
            人脸搜索
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type

        data.update(options)

        return self._request(self.__searchUrl, data)
    
    def addUser(self, image, image_type, group_id, user_id, options=None):
        """
            人脸注册
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id'] = group_id
        data['user_id'] = user_id

        data.update(options)

        return self._request(self.__userAddUrl, data)
    
    def updateUser(self, image, image_type, group_id, user_id, options=None):
        """
            人脸更新
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['group_id'] = group_id
        data['user_id'] = user_id

        data.update(options)

        return self._request(self.__userUpdateUrl, data)
    
    def faceDelete(self, user_id, group_id, face_token, options=None):
        """
            人脸删除
        """
        options = options or {}

        data = {}
        data['user_id'] = user_id
        data['group_id'] = group_id
        data['face_token'] = face_token

        data.update(options)

        return self._request(self.__faceDeleteUrl, data)
    
    def getUser(self, user_id, group_id, options=None):
        """
            用户信息查询
        """
        options = options or {}

        data = {}
        data['user_id'] = user_id
        data['group_id'] = group_id

        data.update(options)

        return self._request(self.__userGetUrl, data)
    
    def faceGetlist(self, user_id, group_id, options=None):
        """
            获取用户人脸列表
        """
        options = options or {}

        data = {}
        data['user_id'] = user_id
        data['group_id'] = group_id

        data.update(options)

        return self._request(self.__faceGetlistUrl, data)
    
    def getGroupUsers(self, group_id, options=None):
        """
            获取用户列表
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id

        data.update(options)

        return self._request(self.__groupGetusersUrl, data)
    
    def userCopy(self, user_id, options=None):
        """
            复制用户
        """
        options = options or {}

        data = {}
        data['user_id'] = user_id

        data.update(options)

        return self._request(self.__userCopyUrl, data)
    
    def deleteUser(self, group_id, user_id, options=None):
        """
            删除用户
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id
        data['user_id'] = user_id

        data.update(options)

        return self._request(self.__userDeleteUrl, data)
    
    def groupAdd(self, group_id, options=None):
        """
            创建用户组
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id

        data.update(options)

        return self._request(self.__groupAddUrl, data)
    
    def groupDelete(self, group_id, options=None):
        """
            删除用户组
        """
        options = options or {}

        data = {}
        data['group_id'] = group_id

        data.update(options)

        return self._request(self.__groupDeleteUrl, data)
    
    def getGroupList(self, options=None):
        """
            组列表查询
        """
        options = options or {}

        data = {}

        data.update(options)

        return self._request(self.__groupGetlistUrl, data)
    
    def personVerify(self, image, image_type, id_card_number, name, options=None):
        """
            身份验证
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type
        data['id_card_number'] = id_card_number
        data['name'] = name

        data.update(options)

        return self._request(self.__personVerifyUrl, data)
    
    def faceverify(self, image, image_type, options=None):
        """
            在线活体检测
        """
        options = options or {}

        data = {}
        data['image'] = image
        data['image_type'] = image_type

        data.update(options)

        return self._request(self.__faceverifyUrl, data)
    
    def videoSessioncode(self, options=None):
        """
            语音校验码接口
        """
        options = options or {}

        data = {}

        data.update(options)

        return self._request(self.__videoSessioncodeUrl, data)
    
    def videoFaceliveness(self, session_id, video_base64, options=None):
        """
            视频活体检测接口
        """
        options = options or {}

        data = {}
        data['session_id'] = session_id
        data['video_base64'] = video_base64

        data.update(options)

        return self._request(self.__videoFacelivenessUrl, data)
    

    __matchUrl = 'https://aip.baidubce.com/rest/2.0/face/v3/match'

    def match(self, images):
        """
            人脸比对
        """

        return self._request(self.__matchUrl, json.dumps(images), {
            'Content-Type': 'application/json',
        })