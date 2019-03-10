import os

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取页面元素的结对路径
pageElementLocatorPath = parentDirPath + "/Config/PageElementLocator.ini"

# 测试数据文件存放绝对路径
dataFilePath = parentDirPath + "/TestData/126邮箱联系人.xlsx"

account_userName = 2
account_passWord = 3
account_dataSourceSheetName = 4
account_isExecute = 5
account_testResult = 6

contacts_contactPersonName = 2
contacts_contactPersonEmail = 3
contacts_isStar = 4
contacts_contactPersonPhone = 5
contacts_contactPersonComment = 6
contacts_assertKeyWords = 7
contacts_isExecute = 8
contacts_runTime = 9
contacts_testResult = 10