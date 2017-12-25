
# -*- coding: utf-8 -*-

"""
自然语言处理
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

class AipNlp(AipBase):

    """
    自然语言处理
    """

    __lexerUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer'

    __lexerCustomUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer_custom'

    __depParserUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/depparser'

    __wordEmbeddingUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_vec'

    __dnnlmCnUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn'

    __wordSimEmbeddingUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_sim'

    __simnetUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet'

    __commentTagUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag'

    __sentimentClassifyUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'

    def _proccessResult(self, content):
        """
            formate result
        """
        
        if sys.version_info.major == 2:
            return json.loads(content.decode('gbk', 'ignore').encode('utf8')) or {}
        else:
            return json.loads(str(content, 'gbk')) or {}

    def _proccessRequest(self, url, params, data, headers):
        """
            _proccessRequest
        """

        if sys.version_info.major == 2:
            return json.dumps(data, ensure_ascii=False).decode('utf8').encode('gbk')
        else:
            return json.dumps(data, ensure_ascii=False).encode('gbk')
    
    def lexer(self, text, options=None):
        """
            词法分析
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__lexerUrl, data)
    
    def lexerCustom(self, text, options=None):
        """
            词法分析（定制版）
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__lexerCustomUrl, data)
    
    def depParser(self, text, options=None):
        """
            依存句法分析
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__depParserUrl, data)
    
    def wordEmbedding(self, word, options=None):
        """
            词向量表示
        """
        options = options or {}

        data = {}
        data['word'] = word

        data.update(options)

        return self._request(self.__wordEmbeddingUrl, data)
    
    def dnnlm(self, text, options=None):
        """
            DNN语言模型
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__dnnlmCnUrl, data)
    
    def wordSimEmbedding(self, word_1, word_2, options=None):
        """
            词义相似度
        """
        options = options or {}

        data = {}
        data['word_1'] = word_1
        data['word_2'] = word_2

        data.update(options)

        return self._request(self.__wordSimEmbeddingUrl, data)
    
    def simnet(self, text_1, text_2, options=None):
        """
            短文本相似度
        """
        options = options or {}

        data = {}
        data['text_1'] = text_1
        data['text_2'] = text_2

        data.update(options)

        return self._request(self.__simnetUrl, data)
    
    def commentTag(self, text, options=None):
        """
            评论观点抽取
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__commentTagUrl, data)
    
    def sentimentClassify(self, text, options=None):
        """
            情感倾向分析
        """
        options = options or {}

        data = {}
        data['text'] = text

        data.update(options)

        return self._request(self.__sentimentClassifyUrl, data)
    