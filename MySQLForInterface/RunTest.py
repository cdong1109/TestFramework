import time
from Util.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from Action.CreatScriptFile import createScrpt
from Config.VarConfig import baseDir

if __name__ == "__main__":
    # 生成测试脚本
    createScrpt()
    # 执行测试用例
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 指定测试用例为当前文件夹下的 script 目录
    test_dir = baseDir + '/Scripts'
    testsuit = defaultTestLoader.discover(test_dir, pattern='*.py')
    filename = baseDir + '/Report/' + now + '_result.html'
    fp = open(filename, 'w', encoding="utf-8")
    runner = HTMLTestRunner(stream=fp, title='接口自动化测试', description='接口自动化测试结果报告')
    runner.run(testsuit)
    fp.close()
