from Config.VarConfig import *
from Util.Log import logger
import os


def getTestFunNames():
    # 获取TestScripts目录下脚本中的函数名
    # 函数名规则自行定义：此框架中.py文件名和该文件中的函数名一致，如AppRank.py文件中的用例函数名为appRank
    allTestFunsList = []
    testScriptsPath = testScriptsDirPath
    files = os.listdir(testScriptsPath)
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            file = os.path.splitext(file)[0]
            allTestFunsList.append(file[0].lower() + file[1:])
    return allTestFunsList


def parseLoadTestConfig():
    # 获取配置文件中执行的用例的函数名
    # 规则自行定义
    allTestFunsList = getTestFunNames()
    testCaseFunList = []
    executeTestCaseFuns = []
    with open(loadTestConfigFilePath,encoding="utf-8") as fp:
        lines = fp.readlines()
        for line in lines:
            if line.strip() and (not line.strip().startswith("#")):
                if line.strip() == "*":
                    testCaseFunList += allTestFunsList
                    break
                else:
                    testCaseFunList.append(line.strip())
    testCaseFunList = list(set(testCaseFunList))
    if "*" in testCaseFunList:
        return allTestFunsList
    else:
        for fun in testCaseFunList:
            if fun in allTestFunsList:
                executeTestCaseFuns.append(fun)
            else:
                logger.error("需要执行的用例函数名“{}”配置错误".format(fun))
        return executeTestCaseFuns
