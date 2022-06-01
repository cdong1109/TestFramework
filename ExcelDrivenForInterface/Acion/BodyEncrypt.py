from Util.EncryptMD5 import encryptMD5


def bodyEncryptOper(sourceData, encryptData):
    # 对请求参数进行MD5加密处理
    try:
        if isinstance(sourceData, dict) and isinstance(encryptData, dict):
            for k, v in encryptData.items():
                for i in v:
                    if i.lower() == "md5" and k in sourceData:
                        sourceData[k] = encryptMD5(sourceData[k])
            return sourceData
    except Exception as e:
        raise e