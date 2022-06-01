from Util.ParseExcel import ParseExcel
from Config.VarConfig import *
import traceback

def writeResult(excelObj,sheet,testResult,rowNo,colNo,testCaseErrMsg=None,apiResult=None):
    #用例执行结束后，向excel中写入执行结果信息
    #testCaseErrMsg写入测试工作表执行失败的信息
    #apiResult写入接口工作表中的用例统计数据，列表中依次传入API_total、API_passNum、API_ignoreNum、API_failNum、API_errorNum

    #通过测试结果信息，判断成功为绿色，失败为红色
    colorDict={"pass":"green","faild":"red","error":"red","":None}

    #通过colNo=“api”写入接口接口工作表，colNo=“testcase”写入测试用例工作表
    try:
        if colNo.lower()=="api":
            if testResult=="":
                #接口工作表中，忽略执行的接口行清空执行结果
                excelObj.writeCell(sheet, testResult, rowNo=rowNo, colsNo=API_runTime,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, testResult, rowNo=rowNo, colsNo=API_total,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, testResult, rowNo=rowNo, colsNo=API_passNum,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, testResult, rowNo=rowNo, colsNo=API_ignoreNum,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, testResult, rowNo=rowNo, colsNo=API_failNum,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, testResult, rowNo=rowNo, colsNo=API_errorNum,style=colorDict[testResult.lower()])
            else:
                excelObj.writeCellCurrentTime(sheet, rowNo=rowNo, colsNo=API_runTime,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, apiResult[0], rowNo=rowNo, colsNo=API_total,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, apiResult[1], rowNo=rowNo, colsNo=API_passNum,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, apiResult[2], rowNo=rowNo, colsNo=API_ignoreNum,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, apiResult[3], rowNo=rowNo, colsNo=API_failNum,style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, apiResult[4], rowNo=rowNo, colsNo=API_errorNum,style=colorDict[testResult.lower()])
        if colNo.lower() == "testcase":
            if testResult == "":
                #测试用例工作表中，忽略执行的测试用例行清空执行结果
                excelObj.writeCell(sheet,"", rowNo=rowNo, colsNo=TestCase_status, style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet,"", rowNo=rowNo, colsNo=TestCase_runTime, style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet,"", rowNo=rowNo, colsNo=TestCase_errorMsg, style=colorDict[testResult.lower()])
            else:
                excelObj.writeCellCurrentTime(sheet, rowNo=rowNo, colsNo=TestCase_runTime, style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, testResult, rowNo=rowNo, colsNo=TestCase_status, style=colorDict[testResult.lower()])
                excelObj.writeCell(sheet, testCaseErrMsg, rowNo=rowNo, colsNo=TestCase_errorMsg,style=colorDict[testResult.lower()])
    except Exception as e:
        print ("写入excel出错\n错误信息:{}：".format(traceback.format_exc()))