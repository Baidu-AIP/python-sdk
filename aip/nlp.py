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

class AipNlp(AipBase):
    """
        Aip NLP
    """

    __wordsegUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/wordseg'

    __wordposUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/wordpos'

    __wordEmbeddingUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_vec'

    __wordSimEmbeddingUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/word_emb_sim'

    __dnnlmUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn'

    __simnetUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet'

    __commentTagUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag'

    __lexerUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer'

    __sentimentClassifyUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'

    __depParserUrl = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/depparser'


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
    
    def wordseg(self, query, options=None):
        """
            Aip wordseg
        """

        data = {}
        data['query'] = query

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__wordsegUrl, data)

    def wordpos(self, query, options=None):
        """
            Aip wordpos
        """

        data = {}
        data['query'] = query

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__wordposUrl, data)

    def wordEmbedding(self, word, options=None):
        """
            Aip wordEmbedding
        """

        data = {}
        data['word'] = word

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__wordEmbeddingUrl, data)

    def wordSimEmbedding(self, word1, word2, options=None):
        """
            Aip wordSimEmbedding
        """

        data = {}
        data['word_1'] = word1
        data['word_2'] = word2

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__wordSimEmbeddingUrl, data)

    def dnnlm(self, text, options=None):
        """
            Aip dnnlm
        """

        data = {}
        data['text'] = text

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__dnnlmUrl, data)

    def simnet(self, text1, text2, options=None):
        """
            Aip simnet
        """

        data = {}
        data['text_1'] = text1 
        data['text_2'] = text2 

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__simnetUrl, data)

    def commentTag(self, text, options=None):
        """
            Aip commentTag
        """

        data = {}
        data['text'] = text

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__commentTagUrl, data)

    def lexer(self, text):
        """
            Aip lexer
        """

        data = {}
        data['text'] = text

        return self._request(self.__lexerUrl, data)

    def sentimentClassify(self, text, options=None):
        """
            Aip sentimentClassify
        """

        data = {}
        data['text'] = text

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__sentimentClassifyUrl, data)

    def depParser(self, text, options=None):
        """
            Aip depParser
        """

        data = {}
        data['text'] = text

        options = options or {}
        data = dict(data, **options)

        return self._request(self.__depParserUrl, data)