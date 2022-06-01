from Util.ParseConfigFile import ParseConfigFile
from Util.ObjectMap import *
from Config.VarConfig import pageElementLocatorPath


class SearchPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile(pageElementLocatorPath)
        self.searchOption = self.cf.getItemsSection("Search")

    def searchBoxObj(self):
        try:
            locateType, locatorExpression = self.searchOption["Search.searchBox".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def searchInputBoxObj(self):
        try:
            locateType, locatorExpression = self.searchOption["Search.searchInputBox".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def searchBtnObj(self):
        try:
            locateType, locatorExpression = self.searchOption["Search.searchBtn".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def assert_string_in_pagesource(self, assertString):
        # 断言界面源码是否存在某关键字或关键字符串
        try:
            assert assertString in self.driver.page_source, u"%s not found in page source!" % assertString
        except AssertionError as e:
            raise AssertionError(e)
        except Exception as  e:
            raise e

    def backObj(self):
        try:
            locateType, locatorExpression = self.searchOption["Search.back".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def goHomePageObj(self):
        try:
            locateType, locatorExpression = self.searchOption["Search.goHomePage".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e
