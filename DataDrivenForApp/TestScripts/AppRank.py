from Util.ParseExcel import ParseExcel
from Util.Log import logger
from Util.GetDesiredcaps import getDesiredcaps
from Config.VarConfig import *
from Action.AppRankAction import AppRankAction
from appium import webdriver
import traceback, time


def appRank():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', getDesiredcaps())
    try:
        excelObj = ParseExcel()
        excelObj.loadWorkBook(dataFilePath)
        appRankSheet = excelObj.getSheetByName("应用")
        isExecute = excelObj.getColumn(appRankSheet, app_isExecute)
        appRankStringCols = excelObj.getColumn(appRankSheet, app_assertKeyWord)

        for idx, i in enumerate(isExecute[1:]):
            appRankString = appRankStringCols[idx + 1].value
            logger.info("----------应用排行“{}”开始执行".format(appRankString))
            if i.value == 'y':
                try:
                    AppRankAction.appRank(driver, appRankString)
                except Exception as e:
                    excelObj.writeCellCurrentTime(appRankSheet, rowNo=idx + 2, colsNo=app_runTime, style="red")
                    excelObj.writeCell(appRankSheet, "Faild", rowNo=idx + 2, colsNo=app_testResult, style="red")
                    logger.error(
                        "在“应用”模块，断言排列前三的APP“{}”失败\n异常信息：{}".format(appRankString, traceback.format_exc()))
                else:
                    excelObj.writeCellCurrentTime(appRankSheet, rowNo=idx + 2, colsNo=app_runTime, style="green")
                    excelObj.writeCell(appRankSheet, "Pass", rowNo=idx + 2, colsNo=app_testResult, style="green")
                    logger.info("在“应用”模块，断言排列前三的APP“{}”成功".format(appRankString))
            else:
                excelObj.writeCell(appRankSheet, "", rowNo=idx + 2, colsNo=app_runTime, )
                excelObj.writeCell(appRankSheet, "", rowNo=idx + 2, colsNo=app_testResult)
                logger.info("排列前三的用例“{}”被忽略执行".format(appRankString))
    except Exception as e:
        logger.error("数据驱动框架主程序发生异常\n异常信息:{}".format(traceback.format_exc()))
    finally:
        driver.quit()
