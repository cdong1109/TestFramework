import json
import re


def checkResult(response, checkPoint):
    # 对接口返回结果进行验证
    # 当验证检查点错误时，返回错误数据
    try:
        if isinstance(checkPoint, str):
            # 检查点是字符串，直接与相应结果进行比较
            errData = ""
            if checkPoint not in response.text:
                errData = response.text
            return errData
        elif isinstance(checkPoint, dict):
            # 检查点是字典格式，兼容正则、字符串、布尔类型的比较
            errData = {}
            responseJson = response.json()
            for k, v in checkPoint.items():
                if k in responseJson:
                    if isinstance(v, dict):
                        # 匹配正规表达式时，str(responseJson[k])兼容字符串或者数据
                        if not re.match(v["value"], str(responseJson[k])):
                            errData[k] = responseJson[k]
                    else:
                        if isinstance(v, bool):
                            if bool(v) != responseJson[k]:
                                errData[k] = responseJson[k]
                        elif isinstance(v, str):
                            if not responseJson[k] == v:
                                errData[k] = responseJson[k]
                else:
                    errData[k] = ""
            return errData
    except Exception as e:
        raise e