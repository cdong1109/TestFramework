import os

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取页面元素的结对路径
pageElementLocatorPath = parentDirPath + "/Config/PageElementLocator.ini"

# 测试数据文件存放绝对路径
dataFilePath = parentDirPath + "/TestData/Vovi应用商城.xlsx"

# desired_caps配置文件的绝对路径
desiredcapsFilePath = parentDirPath + "/Config/DesiredcapsConfig.ini"

# 需要被执行测试用例的配置文件的绝对路径
loadTestConfigFilePath = parentDirPath + "/Config/LoadTestsConfig.ini"

# TestScripts目录的绝对路径
testScriptsDirPath = parentDirPath + "/TestScripts"

search_searchKeyWord = 1
search_assertKeyWord = 2
search_isExecute = 3
search_runTime = 4
search_testResult = 5

app_assertKeyWord = 1
app_isExecute = 2
app_runTime = 3
app_testResult = 4
