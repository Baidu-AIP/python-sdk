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

class AipFace(AipBase):
    """
        Aip Face
    """

    __detectUrl = 'https://aip.baidubce.com/rest/2.0/face/v1/detect'

    __matchUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/match'

    __addUserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/add'

    __updateUserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/update'

    __deleteUserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/delete'

    __verifyUserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/verify'

    __identifyUserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/identify'

    __getUserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/get'

    __getGroupListUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/getlist'

    __getGroupUsersUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/getusers'

    __addGroupUserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/adduser'

    __deleteGroupUserUrl = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/group/deleteuser'


    def detect(self, image, options=None):
        """
            face attributes detect
        """

        options = options or {}
        data = {}
        data['image'] = image

        data = dict(data, **options)

        return self._request(self.__detectUrl, data)

    def __getEncodeImages(self, images):
        """
            encode image array
        """

        if isinstance(images, bytes):
            return base64.b64encode(images)

        result = []
        
        for image in images:
            if image:
                result.append(base64.b64encode(image).decode())        

        return result

    def match(self, images, options=None):
        """
            match
        """

        options = options or {}
        data = {}
        data['images'] = images

        data = dict(data, **options)

        return self._request(self.__matchUrl, data)

    def _validate(self, url, data):
        """
            validate
        """

        # user_info参数 不超过256B
        if 'user_info' in data:
            userInfo = str(data['user_info'])
            if len(userInfo) > 256:
                return {
                    'error_code': 'SDK103',
                    'error_msg': 'user_info size error',
                }

        # group_id参数 组成为字母/数字/下划线，且不超过48B
        if 'group_id' in data:

            if isinstance(data['group_id'], list):
                groupIds = data['group_id']
            else:
                groupIds = [
                    data['group_id'],
                ]

            for groupId in groupIds:
                groupId = str(groupId)
                if not re.match(r'^\w+$', groupId):
                    return {
                        'error_code': 'SDK104',
                        'error_msg': 'group_id format error',
                    }
                if len(groupId) > 48:
                    return {
                        'error_code': 'SDK105',
                        'error_msg': 'group_id size error',
                    }

            data['group_id'] = ','.join(groupIds)

        # uid参数 组成为字母/数字/下划线，且不超过128B
        if 'uid' in data:
            uid = str(data['uid'])
            if not re.match(r'^\w+$', uid):
                return {
                    'error_code': 'SDK106',
                    'error_msg': 'uid format error',
                }
            if len(uid) > 128:
                return {
                    'error_code': 'SDK107',
                    'error_msg': 'uid size error',
                }

        if 'image' in data:
            data['image'] = self.__getEncodeImages(data['image'])
            
            # 编码后小于2m
            if not data['image'] or len(data['image']) >= 10 * 1024 * 1024:
                return {
                    'error_code': 'SDK100',
                    'error_msg': 'image size error',
                }
        elif 'images' in data:
            images = self.__getEncodeImages(data['images'])
            data['images'] = ','.join(images)

            # 人脸比对 编码后小于20m 其他 10m
            maxlen = (20 if url == self.__matchUrl else 10) * 1024 * 1024
            maxcount = (2 if url == self.__matchUrl else 1) 
            if len(images) < maxcount or len(data['images']) >= maxlen:
                return {
                    'error_code': 'SDK100',
                    'error_msg': 'image size error',
                }

        return True

    def addUser(self, uid, userInfo, groupId, image, options=None):
        """
            addUser
        """

        options = options or {}
        data = {}
        data['uid'] = str(uid)
        data['user_info'] = str(userInfo)
        data['group_id'] = groupId
        data['image'] = image

        data = dict(data, **options)

        return self._request(self.__addUserUrl, data)

    def updateUser(self, uid, userInfo, groupId, image, options=None):
        """
            updateUser
        """

        options = options or {}
        data = {}
        data['uid'] = uid
        data['user_info'] = userInfo
        data['group_id'] = groupId
        data['image'] = image

        data = dict(data, **options)

        return self._request(self.__updateUserUrl, data)

    def deleteUser(self, uid, options=None):
        """
            deleteUser
        """

        options = options or {}
        data = {}
        data['uid'] = uid

        data = dict(data, **options)

        return self._request(self.__deleteUserUrl, data)

    def verifyUser(self, uid, groupId, image, options=None):
        """
            verifyUser
        """

        options = options or {}
        data = {}
        data['uid'] = uid
        data['image'] = image
        data['group_id'] = groupId
        
        data = dict(data, **options)

        return self._request(self.__verifyUserUrl, data)

    def identifyUser(self, groupId, image, options=None):
        """
            identifyUser
        """

        options = options or {}
        data = {}
        data['group_id'] = groupId
        data['image'] = image

        data = dict(data, **options)

        return self._request(self.__identifyUserUrl, data)

    def getUser(self, uid, options=None):
        """
            getUser
        """

        options = options or {}
        data = {}
        data['uid'] = uid

        data = dict(data, **options)

        return self._request(self.__getUserUrl, data)

    def getGroupList(self, options=None):
        """
            getGroupList
        """

        options = options or {}
        data = {}

        data = dict(data, **options)

        return self._request(self.__getGroupListUrl, data)

    def getGroupUsers(self, groupId, options=None):
        """
            getGroupUsers
        """

        options = options or {}
        data = {}
        data['group_id'] = groupId

        data = dict(data, **options)

        return self._request(self.__getGroupUsersUrl, data)

    def addGroupUser(self, srcGroupId, dstGroupId, uid):
        """
            addGroupUser
        """

        data = {}
        data['uid'] = uid
        data['group_id'] = dstGroupId
        data['src_group_id'] = srcGroupId

        return self._request(self.__addGroupUserUrl, data)

    def deleteGroupUser(self, groupId, uid):
        """
            deleteGroupUser
        """

        data = {}
        data['uid'] = uid
        data['group_id'] = groupId

        return self._request(self.__deleteGroupUserUrl, data)

