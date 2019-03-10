from PageObjects.SearchPage import SearchPage
import time


class SearchAction(object):
    @staticmethod
    def search(driver, searchAppName, assertKeyword):
        sa = SearchPage(driver)
        sa.searchBoxObj().click()
        sa.searchInputBoxObj().send_keys(searchAppName)
        sa.searchBtnObj().click()
        time.sleep(3)
        sa.assert_string_in_pagesource(assertKeyword)
        sa.backObj().click()
        sa.goHomePageObj().click()