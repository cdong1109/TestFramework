import os

# 数据源表中存放接口的数据表名
ApiSheetName = "API"
# 框架根目录所在绝对路径
baseDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据文件所在绝对路径
dataFilePath = baseDirPath + "/TestData/inter_test_data.xlsx"

# 测试接口对应的列名
API_name = 2
API_protocol = 3
API_requestUrl = 4
API_requestMothod = 5
API_paramsType = 6
API_testCaseSheetName = 7
API_isExecute = 8
API_runTime = 9
API_total = 10
API_passNum = 11
API_ignoreNum = 12
API_failNum = 13
API_errorNum = 14

# 测试用例对应的数据列名
TestCase_requestHeaders = 1
TestCase_headersEncrypt = 2
TestCase_requestData = 3
TestCase_dependData = 4
TestCase_bodyEncrypt = 5
TestCase_responseData = 6
TestCase_responseDecrypt = 7
TestCase_dependDataStore = 8
TestCase_checkPoint = 9
TestCase_isExecute = 10
TestCase_status = 11
TestCase_runTime = 12
TestCase_errorMsg = 13

# 存储请求参数中的依赖数据
RequestData = {}
# 存储响应数据中的依赖数据
ResponseData = {}
