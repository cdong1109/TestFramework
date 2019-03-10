import os

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 异常图片存放目录
screenPicturesDir = parentDirPath + "/ExceptionPictures/"

# 测试数据文件存放绝对路径
dataFilePath = parentDirPath + "/TestData/126邮箱发送邮件.xlsx"

# 测试数据文件中，测试用例表中部分列对应的数字序号
testCase_testCaseName = 2
testCase_testStepSheetName = 4
testCase_isExecute = 5
testCase_runTime = 6
testCase_testResult = 7

# 用例步骤表中，部分列对应的数字序号
caseStep_caseStepDescription = 2
caseStep_keyWord = 3
caseStep_locationType = 4
caseStep_locatorExpression = 5
caseStep_operatorValue = 6
caseStep_runTime = 7
caseStep_testResult = 8
caseStep_errMsg = 9
caseStep_errPicPath = 10
