from selenium import webdriver
from Action.AddContactAction import AddContactAction
from Action.LoginAction import LoginAction
from Util.ParseExcel import ParseExcel
from Config.VarConfig import *
from Util.Log import logger
import time, traceback


def createContacts():
    try:
        excelObj = ParseExcel()
        excelObj.loadWorkBook(dataFilePath)
        userSheet = excelObj.getSheetByName("126账号")
        isExecute = excelObj.getColumn(userSheet, account_isExecute)
        userNameCols = excelObj.getColumn(userSheet, account_userName)
        for idx, i in enumerate(isExecute[1:]):
            if i.value == 'y':
                userRow = excelObj.getRow(userSheet, idx + 2)
                userName = userRow[account_userName - 1].value
                passWord = str(userRow[account_passWord - 1].value)
                contactSheetName = userRow[account_dataSourceSheetName - 1].value

                driver = webdriver.Chrome()
                driver.maximize_window()
                driver.get("https://mail.126.com/")
                LoginAction.login(driver, userName, passWord)

                #断言前停顿3秒，防止页面跳转太快，断言失败
                time.sleep(3)
                try:
                    assert "收 信" in driver.page_source
                except Exception as e:
                    logger.error("用户“{}”登录后，断言页面关键字“退出”失败\n异常信息：{}".format(userName, traceback.format_exc()))
                else:
                    logger.info("用户“{}”登录后,断言页面关键字“退出”成功".format(userName))

                contactSheet = excelObj.getSheetByName(contactSheetName)
                isExecuteAddContact = excelObj.getColumn(contactSheet, contacts_isExecute)

                contactNum = 0
                successAddContactNum = 0
                coutactPersonNameCols = excelObj.getColumn(contactSheet, contacts_contactPersonName)
                for id, j in enumerate(isExecuteAddContact[1:]):
                    if j.value == 'y':
                        contactNum += 1
                        contactRow = excelObj.getRow(contactSheet, id + 2)
                        coutactPersonName = coutactPersonNameCols[id + 1].value
                        coutactPersonEmail = contactRow[contacts_contactPersonEmail - 1].value
                        isStar = contactRow[contacts_isStar - 1].value
                        countactPersonPhone = str(contactRow[contacts_contactPersonPhone - 1].value)
                        countactPersonComment = contactRow[contacts_contactPersonComment - 1].value
                        assertKeyWords = contactRow[contacts_assertKeyWords - 1].value

                        logger.info("**********开始添加联系人“%s”**********" % coutactPersonName)
                        AddContactAction.addContact(driver, coutactPersonName, coutactPersonEmail, isStar,
                                                    countactPersonPhone, countactPersonComment)
                        time.sleep(3)
                        try:
                            assert assertKeyWords in driver.page_source
                        except Exception as e:
                            excelObj.writeCell(contactSheet, "faild", rowNo=id + 2, colsNo=contacts_testResult,
                                               style="red")
                            excelObj.writeCellCurrentTime(contactSheet, rowNo=id + 2, colsNo=contacts_runTime,
                                                          style="red")
                            logger.error("添加联系人“{}”失败\n异常信息：{}".format(coutactPersonName, traceback.format_exc()))
                        else:
                            successAddContactNum += 1
                            excelObj.writeCell(contactSheet, "pass", rowNo=id + 2, colsNo=contacts_testResult,
                                               style="green")
                            excelObj.writeCellCurrentTime(contactSheet, rowNo=id + 2, colsNo=contacts_runTime,
                                                          style="green")
                            logger.info("添加联系人“{}”成功".format(coutactPersonName))
                    else:
                        excelObj.writeCell(contactSheet, "", rowNo=id + 2, colsNo=contacts_runTime)
                        excelObj.writeCell(contactSheet, "", rowNo=id + 2, colsNo=contacts_testResult)
                        logger.info("联系人“{}”被忽略执行".format(coutactPersonNameCols[idx + 1].value))
                driver.quit()
                if contactNum == successAddContactNum:
                    excelObj.writeCell(userSheet, "Pass", rowNo=idx + 2, colsNo=account_testResult, style="green")
                else:
                    excelObj.writeCell(userSheet, "Faild", rowNo=idx + 2, colsNo=account_testResult, style="red")
            else:
                excelObj.writeCell(userSheet, "", rowNo=idx + 2, colsNo=account_testResult)
                logger.info("账号“{}”被忽略执行".format(userNameCols[idx + 1].value))
    except Exception as e:
        logger.error("数据驱动框架主程序发生异常\n异常信息:{}".format(traceback.format_exc()))
