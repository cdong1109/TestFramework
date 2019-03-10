from Config.VarConfig import RequestData, ResponseData


def getDependData(sourceData, dependData):
    # sourceData字典中存在key值"request"时，在全局变量RequestData中取出满足规则的数据，保存在sourceData，供接口请求使用
    # sourceData字典中存在key值"response"时，在全局变量ResponseData中取出满足规则的数据，保存在sourceData，供接口请求使用
    try:
        if isinstance(sourceData, dict) and isinstance(dependData, dict):
            if "request" in dependData:
                for k, v in dependData["request"].items():
                    testCaseSheetName, caseId = v.split("->")
                    if testCaseSheetName in RequestData:
                        if caseId in RequestData[testCaseSheetName]:
                            if k in RequestData[testCaseSheetName][caseId]:
                                sourceData[k] = RequestData[testCaseSheetName][caseId][k]
                            else:
                                sourceData[k] = ""
                        else:
                            sourceData[k] = ""
                    else:
                        sourceData[k] = ""
                return sourceData
            elif "response" in dependData:
                for k, v in dependData["response"].items():
                    testCaseSheetName, caseId = v.split("->")
                    if testCaseSheetName in ResponseData:
                        if caseId in ResponseData[testCaseSheetName]:
                            if k in ResponseData[testCaseSheetName][caseId]:
                                sourceData[k] = ResponseData[testCaseSheetName][caseId][k]
                            else:
                                sourceData[k] = ""
                        else:
                            sourceData[k] = ""
                    else:
                        sourceData[k] = ""
                return sourceData
    except Exception as e:
        raise e
