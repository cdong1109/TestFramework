from Action.PageAction import *
from Util.ParseExcel import ParseExcel
from Config.VarConfig import *
from Util.Log import logger
from TestScripts.WriteResult import writeResult
import traceback


def send_126Mail():
    try:
        excelObj = ParseExcel()
        excelObj.loadWorkBook(dataFilePath)
        caseSheet = excelObj.getSheetByName("测试用例")
        caseNameCols = excelObj.getColumn(caseSheet, testCase_testCaseName)
        isExecuteCaseCols = excelObj.getColumn(caseSheet, testCase_isExecute)
        # 记录需要执行的用例个数
        requiredCaseNum = 0
        # 记录执行成功的用例个数
        successfulCaseNum = 0

        for idx, i in enumerate(isExecuteCaseCols[1:]):
            # 测试用例sheet中第一行为标题，无须执行
            if i.value == "y":
                requiredCaseNum += 1
                caseRow = excelObj.getRow(caseSheet, idx + 2)
                caseName = caseNameCols[idx + 1].value
                stepSheetName = caseRow[testCase_testStepSheetName - 1].value
                # print CaseName,StepSheetName
                # 根据用例的sheet名获取用例的sheet对象
                stepSheet = excelObj.getSheetByName(stepSheetName)
                # 记录用例步骤的个数
                stepNum = excelObj.getRowsNumber(stepSheet)
                # 记录用例步骤执行成功的个数
                successfulStepNum = 0

                logger.info("----------" + caseName)
                for j in range(2, stepNum + 1):
                    # 用例步骤中的第一行为标题，无须执行
                    stepRow = excelObj.getRow(stepSheet, j)
                    # 获取用例步骤中描述
                    StepDescription = stepRow[caseStep_caseStepDescription - 1].value
                    # 获取函数名
                    keyWord = stepRow[caseStep_keyWord - 1].value
                    # 获取操作元素的定位方式
                    locationType = stepRow[caseStep_locationType - 1].value
                    # 获取操作元素定位方式的表达式
                    locatorExpression = stepRow[caseStep_locatorExpression - 1].value
                    # 获取函数中的参数
                    operatorValue = stepRow[caseStep_operatorValue - 1].value
                    # 数值类数据从excel取出后为数字，转换为字符串，方便拼接
                    if isinstance(operatorValue, int):
                        operatorValue = str(operatorValue)
                    if keyWord and locationType and locatorExpression and operatorValue:
                        step = keyWord + "('{}','{}','{}')".format(locationType, locatorExpression, operatorValue)
                    elif keyWord and locationType and locatorExpression:
                        step = keyWord + "('{}','{}')".format(locationType, locatorExpression)
                    elif keyWord and operatorValue:
                        step = keyWord + "('{}')".format(operatorValue)
                    else:
                        step = keyWord + "()"
                    try:
                        # 用例步骤执行执行成功，写入执行结果和日志
                        eval(step)
                        successfulStepNum += 1
                        writeResult(excelObj, stepSheet, "Pass", j, "caseStep")
                        logger.info("执行步骤“{}”成功".format(StepDescription))
                    except Exception as e:
                        # 用例步骤执行执行成功
                        errPicPath = capture_screen()
                        errMsg = traceback.format_exc()
                        writeResult(excelObj, stepSheet, "Faild", j, "caseStep", errMsg="errMsg", errPicPath=errPicPath)
                        logger.error("执行步骤“{}”失败\n异常信息：{}".format(StepDescription, traceback.format_exc()))
                if successfulStepNum == stepNum - 1:
                    successfulCaseNum += 1
                    writeResult(excelObj, caseSheet, "Pass", idx + 2, "testCase")
                else:
                    writeResult(excelObj, caseSheet, "Faild", idx + 2, "testCase")
            else:
                writeResult(excelObj, caseSheet, "", idx + 2, "testCase")
                logger.info("用例“{}”被设置为忽略执行".format(caseNameCols[idx + 1].value))
        logger.error("共{}条用例，{}条需要被执行，本次执行通过{}条".format(len(isExecuteCaseCols) - 1, requiredCaseNum, successfulCaseNum))
    except Exception as e:
        logger.info("关键字驱动框架主程序发生异常\n异常信息:{}".format(traceback.format_exc()))