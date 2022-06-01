from Config.VarConfig import RequestData, ResponseData

def dataStore(needStoreData, testCaseSheeName, taseCaseId, requestSource={}, responseSource={}):
    # needStoreData字典中存在key值"request"时，requestSource数据按照自定义的存储规则保存在全部变量RequestData中
    # needStoreData字典中存在key值"response"时，responseSource数据按照自定义的存储规则保存在全部变量responseSource中
    try:
        if isinstance(requestSource, dict) and isinstance(responseSource, dict):
            if "request" in needStoreData:
                for i in needStoreData["request"]:
                    if i in requestSource:
                        if testCaseSheeName in RequestData:
                            if str(taseCaseId) in RequestData[testCaseSheeName]:
                                RequestData[testCaseSheeName][str(taseCaseId)][i] = requestSource[i]
                            else:
                                RequestData[testCaseSheeName][str(taseCaseId)] = {i: requestSource[i]}
                        else:
                            RequestData[testCaseSheeName] = {str(taseCaseId): {i: requestSource[i]}}
            if "response" in needStoreData:
                for i in needStoreData["response"]:
                    if i in responseSource:
                        if testCaseSheeName in ResponseData:
                            if str(taseCaseId) in ResponseData[testCaseSheeName]:
                                ResponseData[testCaseSheeName][str(taseCaseId)][i] = responseSource[i]
                            else:
                                ResponseData[testCaseSheeName][str(taseCaseId)] = {i: responseSource[i]}
                        else:
                            ResponseData[testCaseSheeName] = {str(taseCaseId): {i: responseSource[i]}}
    except Exception as e:
        raise e