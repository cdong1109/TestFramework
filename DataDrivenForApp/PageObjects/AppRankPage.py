from Util.ParseConfigFile import ParseConfigFile
from Util.ObjectMap import *
from Config.VarConfig import pageElementLocatorPath


class AppRank(object):
    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile(pageElementLocatorPath)
        self.loginOption = self.cf.getItemsSection("APPRank")

    def goHomePageObj(self):
        try:
            locateType, locatorExpression = self.loginOption["APPRank.goHomePage".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def assertAppList(self, assertString):
        try:
            assertStringList = assertString.split(",")
            locateType, locatorExpression = self.loginOption["APPRank.assertKeywordList".lower()].split(">")
            elements = getElements(self.driver, locateType, locatorExpression)
            for element in elements[:3]:
                assert element.text in assertStringList
        except AssertionError as e:
            raise AssertionError(e)
        except Exception as e:
            raise e
