from Util.ParseExcel import ParseExcel
from Util.Log import logger
from Util.GetDesiredcaps import getDesiredcaps
from Config.VarConfig import *
from Action.SearchAppAction import SearchAction
from appium import webdriver
import traceback, time


def searchApp():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', getDesiredcaps())
    try:
        excelObj = ParseExcel()
        excelObj.loadWorkBook(dataFilePath)
        searchSheet = excelObj.getSheetByName("搜索")
        isExecute = excelObj.getColumn(searchSheet, search_isExecute)
        searchKeyWordCols = excelObj.getColumn(searchSheet, search_searchKeyWord)

        for idx, i in enumerate(isExecute[1:]):
            searchKeyWord = searchKeyWordCols[idx + 1].value
            logger.info("----------搜索APP“{}”开始执行".format(searchKeyWord))
            if i.value == 'y':
                searchRow = excelObj.getRow(searchSheet, idx + 2)
                assertKeyWord = searchRow[search_assertKeyWord - 1].value
                try:
                    SearchAction.search(driver, searchKeyWord, assertKeyWord)
                except Exception as e:
                    excelObj.writeCellCurrentTime(searchSheet, rowNo=idx + 2, colsNo=search_runTime, style="red")
                    excelObj.writeCell(searchSheet, "Faild", rowNo=idx + 2, colsNo=search_testResult, style="red")
                    logger.error("搜索APP“{}”失败\n异常信息：{}".format(searchKeyWord, traceback.format_exc()))
                else:
                    excelObj.writeCellCurrentTime(searchSheet, rowNo=idx + 2, colsNo=search_runTime, style="green")
                    excelObj.writeCell(searchSheet, "Pass", rowNo=idx + 2, colsNo=search_testResult, style="green")
                    logger.info("搜索APP“{}”成功".format(searchKeyWord))
            else:
                excelObj.writeCell(searchSheet, "", rowNo=idx + 2, colsNo=search_runTime, )
                excelObj.writeCell(searchSheet, "", rowNo=idx + 2, colsNo=search_testResult)
                logger.info("搜索APP“{}”的用例被忽略执行".format(searchKeyWord))
    except Exception as e:
        logger.error("数据驱动框架主程序发生异常\n异常信息:{}" % (traceback.format_exc()))
    finally:
        driver.quit()
