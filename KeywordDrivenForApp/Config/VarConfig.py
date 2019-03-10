import os

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 异常图片存放目录
screenPicturesDir = parentDirPath + "/ExceptionPictures/"

# 测试数据文件存放绝对路径
dataFilePath = parentDirPath + "/TestData/Vovi应用商城.xlsx"

# Dedired_caps配置文件存放的绝对路径
desiredcapsFilePath = parentDirPath + "/Config/DesiredcapsConfig.ini"

# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName = 1
testCase_testStepSheetName = 3
testCase_isExecute = 4
testCase_runTime = 5
testCase_testResult = 6

# 用例步骤表中，部分列对应的数字序号
caseStep_caseStepDescription = 1
caseStep_keyWord = 2
caseStep_locationType = 3
caseStep_locatorExpression = 4
caseStep_operatorValue = 5
caseStep_runTime = 6
caseStep_testResult = 7
caseStep_errMsg = 8
caseStep_errPicPath = 9
