import requests
import json


class HttpClient(object):
    def __init__(self):
        pass

    def __post(self, url, data=None, json=None, **kwargs):
        response = requests.post(url=url, data=data, json=json, **kwargs)
        return response

    def __get(self, url, params=None, **kwargs):
        response = requests.get(url=url, params=params, **kwargs)
        return response

    def request(self, requestMethod, requestUrl, paramType, requestData=None, headers=None, cookies=None):
        if requestMethod.lower() == "post":
            try:
                if paramType.lower() == "form":
                    response = self.__post(requestUrl, data=json.dumps(requestData), headers=None, cookies=None)
                    return response
                elif paramType.lower() == "json":
                    response = self.__post(requestUrl, json=requestData, headers=None, cookies=None)
                    return response
            except Exception as e:
                raise e
        elif requestMethod.lower() == "get":
            try:
                if paramType.lower() == "params":
                    response = self.__get(requestUrl, params=requestData, headers=None, cookies=None)
                    return response
                elif paramType.lower() == "url":
                    response = self.__get(requestUrl + str(requestData), headers=None, cookies=None)
                    return response
            except Exception as e:
                raise e