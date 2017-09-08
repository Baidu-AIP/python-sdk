# -*- coding: utf-8 -*-

"""
    KG
"""
from .base import AipBase

class AipKg(AipBase):
    """
        Aip KG
    """

    __getUserTasksUrl = 'https://aip.baidubce.com/rest/2.0/kg/v1/pie/task_query'

    __getTaskInfoUrl = 'https://aip.baidubce.com/rest/2.0/kg/v1/pie/task_info'

    __createTaskUrl = 'https://aip.baidubce.com/rest/2.0/kg/v1/pie/task_create'

    __updateTaskUrl = 'https://aip.baidubce.com/rest/2.0/kg/v1/pie/task_update'

    __startTaskUrl = 'https://aip.baidubce.com/rest/2.0/kg/v1/pie/task_start'

    __getTaskStatusUrl = 'https://aip.baidubce.com/rest/2.0/kg/v1/pie/task_status'


    def getUserTasks(self, options=None):
        """
            getUserTasks
        """

        data = {}

        data = dict(data, **(options or {}))

        return self._request(self.__getUserTasksUrl, data)

    def getTaskInfo(self, taskId):
        """
            getTaskInfo
        """

        data = {}
        data['id'] = taskId

        return self._request(self.__getTaskInfoUrl, data)

    def createTask(
        self,
        name,
        tplStr,
        inputMapping,
        outputFile,
        urlPattern,
        options=None
    ):
        """
            createTask
        """

        data = {}
        data['name'] = name
        data['template_content'] = tplStr
        data['input_mapping_file'] = inputMapping
        data['url_pattern'] = urlPattern
        data['output_file'] = outputFile

        data = dict(data, **(options or {}))

        return self._request(self.__createTaskUrl, data)

    def updateTask(self, taskId, options=None):
        """
            updateTask
        """

        data = {}
        data['id'] = taskId

        data = dict(data, **(options or {}))

        return self._request(self.__updateTaskUrl, data)

    def startTask(self, taskId):
        """
            startTask
        """

        data = {}
        data['id'] = taskId

        return self._request(self.__startTaskUrl, data)

    def getTaskStatus(self, taskId):
        """
            getTaskStatus
        """

        data = {}
        data['id'] = taskId

        return self._request(self.__getTaskStatusUrl, data)
