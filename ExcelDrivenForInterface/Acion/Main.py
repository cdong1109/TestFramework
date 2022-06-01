from Util.HttpClient import HttpClient
from Util.ParseExcel import ParseExcel
from Config.VarConfig import *
from Util.Log import logger
from Acion.BodyEncrypt import bodyEncryptOper
from Acion.CheckResult import checkResult
from Acion.WriteResult import writeResult
from Acion.DataStore import dataStore
from Acion.GetDependData import getDependData
import json
import traceback


def sendRequest():
    try:
        excelObj = ParseExcel()
        excelObj.loadWorkBook(dataFilePath)
        apiSheet = excelObj.getSheetByName(ApiSheetName)

        apiNameCols = excelObj.getColumn(apiSheet, API_name)
        apiIsExecuteCols = excelObj.getColumn(apiSheet, API_isExecute)
        for idx, i in enumerate(apiIsExecuteCols[1:]):
            apiName = apiNameCols[idx + 1].value
            if i.value == "y":
                case_total = 0
                case_passNum = 0
                case_ignoreNum = 0
                case_failNum = 0
                case_errorNum = 0
                apiRow = excelObj.getRow(apiSheet, idx + 2)
                requestUrl = apiRow[API_requestUrl - 1].value
                requestMothod = apiRow[API_requestMothod - 1].value
                paramsType = apiRow[API_paramsType - 1].value
                testCaseSheetName = apiRow[API_testCaseSheetName - 1].value

                logger.info("----------" + apiName)
                testCaseSheet = excelObj.getSheetByName(testCaseSheetName)
                testCaseIsExecuteCols = excelObj.getColumn(testCaseSheet, TestCase_isExecute)
                for id, j in enumerate(testCaseIsExecuteCols[1:]):
                    case_total += 1
                    try:
                        if j.value == "y":
                            testCaseRow = excelObj.getRow(testCaseSheet, id + 2)
                            requestHeaders = testCaseRow[TestCase_requestHeaders - 1].value
                            headersEncrypt = testCaseRow[TestCase_headersEncrypt - 1].value
                            requestData = testCaseRow[TestCase_requestData - 1].value
                            dependData = testCaseRow[TestCase_dependData - 1].value
                            bodyEncrypt = testCaseRow[TestCase_bodyEncrypt - 1].value
                            responseData = testCaseRow[TestCase_responseData - 1].value
                            responseDecrypt = testCaseRow[TestCase_responseDecrypt - 1].value
                            dependDataStore = testCaseRow[TestCase_dependDataStore - 1].value
                            checkPoint = testCaseRow[TestCase_checkPoint - 1].value

                            # 当请求参数中不是数值时，处理成字典
                            if not isinstance(requestData, int):
                                requestData = eval(requestData)
                            # 处理请求参数中的依赖数据
                            if requestData and dependData:
                                requestData = getDependData(requestData, eval(dependData))
                            # 处理请求参数中的加密数据
                            if requestData and bodyEncrypt:
                                requestData = bodyEncryptOper(requestData, eval(bodyEncrypt))

                            httpC = HttpClient()
                            response = httpC.request(requestMothod, requestUrl, paramsType, requestData=requestData)
                            # 接口响应结果写入用例工作表
                            excelObj.writeCell(testCaseSheet, response.text, rowNo=id + 2, colsNo=TestCase_responseData)
                            # 当接口响应成功时，验证检查点是否满足
                            if response.status_code == 200 and checkPoint:
                                # 获取检查点错误信息
                                errData = checkResult(response, eval(checkPoint))
                                if errData:
                                    # 接口执行失败，执行的错误结果写入到测试用例工作表
                                    case_failNum += 1
                                    writeResult(excelObj, testCaseSheet, "Faild", id + 2, "testcase",
                                                testCaseErrMsg=str(errData))
                                    logger.info("接口“{}”的第“{}”条用例执行失败".format(apiName, id + 1))

                                else:
                                    # 接口执行成功，执行的正确结果写入到测试用例工作表
                                    case_passNum += 1
                                    writeResult(excelObj, testCaseSheet, "Pass", id + 2, "testcase")
                                    logger.info(u"接口“{}”的第“{}”条用例执行成功".format(apiName, id + 1))
                                    # 当接口执行成功时，保存依赖数据到全局变量RequestData、ResponseData，供后面的接口使用
                                    if dependDataStore:
                                        dataStore(eval(dependDataStore), testCaseSheetName, id + 2,
                                                  requestSource=requestData, responseSource=response.json())
                            elif response.status_code != 200:
                                # 接口响应失败，执行失败的接口写入到测试用例工作表
                                case_errorNum += 1
                                writeResult(excelObj, testCaseSheet, "Error", id + 2, "testcase",
                                            testCaseErrMsg="接口响应异常！")
                                logger.info(
                                    "接口“{}”的第“{}”条用例执行过程出错\n错误信息：{}".format(apiName, id + 1, traceback.format_exc()))
                        else:
                            # 清空忽略执行的测试用例工作表数据
                            case_ignoreNum += 1
                            writeResult(excelObj, testCaseSheet, "", id + 2, "testcase")
                            logger.info("接口“{}”的第“{}”条用例被设置为忽略执行".format(apiName, id + 1))
                    except Exception as e:
                        # 接口请求中，发生异常情况，将错误结果写入测试用例工作表
                        case_errorNum += 1
                        writeResult(excelObj, testCaseSheet, "Error", id + 2, "testcase",
                                    testCaseErrMsg=traceback.format_exc())
                        logger.info(
                            "接口请求发生异常情况，接口“{}”的第“{}”条用例执行过程出错\n错误信息：{}".format(apiName, id + 1, traceback.format_exc()))

                if case_errorNum or case_failNum:
                    # 存在异常错误或者失败测试用例时，表示接口api执行错误，将相关的统计数据写入到接口api的工作表中
                    writeResult(excelObj, apiSheet, "Faild", idx + 2, "api",
                                apiResult=[case_total, case_passNum, case_ignoreNum, case_failNum, case_errorNum])
                else:
                    writeResult(excelObj, apiSheet, "Pass", idx + 2, "api",
                                apiResult=[case_total, case_passNum, case_ignoreNum, case_failNum, case_errorNum])
            else:
                # 清空忽略执行api工作表的数据
                writeResult(excelObj, apiSheet, "", idx + 2, "api")
                logger.info("接口“{}”被设置为忽略执行".format(apiName))

    except Exception as e:
        logger.info("接口框架主程序发生异常\n异常信息:{}".format(traceback.format_exc()))
