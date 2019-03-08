# coding=utf-8
import time
import unittest
from selenium import webdriver
from Public.log import Logger
from Public.browser_base import BrowserBase

mylogger = Logger(logger='amazon测试日志').getlog()

class AmazonTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        mylogger.info("打开浏览器" )
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)


    def tearDown(self):
        self.driver.quit()

    def test_amazon(self):
        browserbase = BrowserBase(self.driver)
        browserbase.open_url("https://www.amazon.cn/")
        mylogger.info("打开amazon网站")
        self.driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys("软件测试")
        #print(self.driver.title)
        mylogger.info("输入关键字 软件测试" )

        self.driver.find_element_by_xpath("//*[@value='搜索']").click()
        #print(self.driver.current_window_handle)
        #print(self.driver.title)
        mylogger.info("搜索 软件测试" )

        # js = 'document.getElementsByName("tj_trnews")[0].target="_blank"'
        # self.driver.execute_script(js)

        self.driver.find_element_by_xpath("//*[@data-attribute='软件测试(原书第2版)']").click()
        mylogger.info("点击 软件测试(原书第2版)" )

        handles = self.driver.window_handles
        #print(handles)

        self.driver.switch_to.window(handles[1])
        #print(self.driver.current_window_handle)
        #print(self.driver.title)

        self.driver.find_element_by_xpath("//*[@id='add-to-cart-button']").click()
        #print('11111')
        #print(self.driver.title)
        mylogger.info("加入购物车")
        time.sleep(1)

        try:
            assert '商品已加入购物车' in self.driver.page_source, "页面源码中不存在该关键字！"
            #print('Test pass.')
            a = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div/div/div[1]/span/span[2]").text
            mylogger.info("页面包含关键词 商品已加入购物车")
            assert '￥ 28.20' in a, "价格不对！"
            mylogger.info("商品价格验证")
            #browserbase.take_screenshot()
            print('-----Test pass.-----')
        except Exception as e:
            browserbase.take_screenshot()
            mylogger.info("ERROR:%s" % e)
            print('Test fail.')

        browserbase.quit_browser()


