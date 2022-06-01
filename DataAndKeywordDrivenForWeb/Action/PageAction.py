from selenium import webdriver
from Util.ObjectMap import getElement
from Util.Clipboard import Clipboard
from Util.KeyBoard import KeyboardKeys
from Util.DirAndTime import *
from Util.Wait import WaitUtil
import time

# 定义全局driver变量
driver = None
# 全局的等待类实例对象
waitUtil = None


def open_broswer(broswerName, *arg):
    # 打开浏览器
    global driver, waitUtil
    try:
        if broswerName.lower() == 'ie':
            driver = webdriver.Ie()
        elif broswerName.lower() == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        # driver对象创建成果后，创建等待类实例对象
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e


def visit_url(url, *arg):
    # 访问某个网址
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e


def close_broswer(*arg):
    # 关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e


def sleep(sleepSeconds, *arg):
    # 强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e


def clear(locationType, locatorExpression, *arg):
    # 清除输入框默认内容
    global driver
    try:
        getElement(driver, locationType, locatorExpression).clear()
    except Exception as e:
        raise e


def input_string(locationType, locatorExpression, inputContent):
    # 在页面输入框中输入数据
    global driver
    try:
        getElement(driver, locationType,
                   locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e


def click(locationType, locatorExpression, *arg):
    # 点击页面元素
    global driver
    try:
        getElement(driver, locationType, locatorExpression).click()
    except Exception as e:
        raise e


def assert_string_in_pagesource(assertString, *arg):
    # 断言页面源码是否存在某关键字或关键字符串
    global driver
    try:
        assert assertString in driver.page_source, "{} not found in page source!".format(assertString)
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e


def assert_title(titleStr, *args):
    # 断言页面标题是否存在给定的关键字符串
    global driver
    try:
        assert titleStr in driver.title, "{} not found in title!".format(titleStr)
    except AssertionError as  e:
        raise AssertionError(e)
    except Exception as e:
        raise e


def getTitle(*arg):
    # 获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e


def getPageSource(*arg):
    # 获取页面源码
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e


def switch_to_frame(locationType, frameLocatorExpression, *arg):
    # 切换进入frame
    global driver
    try:
        driver.switch_to.frame(getElement
                               (driver, locationType, frameLocatorExpression))
    except Exception as e:
        raise e


def switch_to_default_content(*arg):
    # 切出frame，回到默认对话框中
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e


def paste_string(pasteString, *arg):
    # 模拟ctrl + v操作
    try:
        Clipboard.setText(pasteString)
        # 等待2秒，防止代码执行的太快，而未成功粘贴内容
        time.sleep(2)
        KeyboardKeys.twoKeys("ctrl", "v")
    except Exception as e:
        raise e


def press_tab_key(*arg):
    # 模拟 tab 键
    try:
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e


def press_enter_key(*arg):
    # 模拟 enter 键
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e


def maximize_broswer():
    # 窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e


def capture_screen(*args):
    # 截取屏幕图片
    global driver
    # 获取当期时间，精确到毫秒
    currTime = getCurrentTime()
    # 拼接异常图片保存的绝对路径及名称
    picNameAndPath = createCurrentDateDir() + "/" + currTime + ".png"
    try:
        # 截取屏幕图片，并保存为本地文件
        driver.get_screenshot_as_file(picNameAndPath)
    except Exception as e:
        raise e
    else:
        return picNameAndPath


def waitPresenceOfElementLocated(locationType, locatorExpression, *arg):
    '''显示等待页面元素出现在DOM中，但并一定可以见，
            存在则返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType, locatorExpression)
    except Exception as e:
        raise e


def waitFrameToBeAvailableAndSwitchToIt(locationType, locatorExpression, *args):
    '''检查frame是否存在，存在则切换进frame控件中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType, locatorExpression)
    except Exception as e:
        raise e


def waitVisibilityOfElementLocated(locationType, locatorExpression, *args):
    '''显示等待页面元素出现在DOM中，并且可见，存在返回该页面元素对象'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType, locatorExpression)
    except Exception as e:
        raise e