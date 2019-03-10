from PageObjects.AppRankPage import AppRank
import time


class AppRankAction(object):
    @staticmethod
    def appRank(driver, appRankString):
        ar = AppRank(driver)
        ar.goHomePageObj().click()
        time.sleep(3)
        ar.assertAppList(appRankString)
