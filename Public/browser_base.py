# coding=utf-8
import os
import time
from Public.log import Logger
path=os.getcwd()
mylog = Logger(logger='BasePage').getlog()


class BrowserBase(object):
    """
    主要是把常用的几个Selenium方法封装到BasePage这个类，
    back()
    forward()
    get()
    quit()
    """

    def __init__(self, driver):
        self.driver = driver

    def back(self):

        #浏览器后退按钮

        self.driver.back()

    def forward(self):

        #浏览器前进按钮

        self.driver.forward()

    def open_url(self, url):

        #打开url站点

        self.driver.get(url)

    def quit_browser(self):

        #关闭并停止浏览器服务

        self.driver.quit()

    def take_screenshot(self):
        #截图并保存在根目录下的Screenshots文件夹下
        #file_path = os.getcwd() + '\\Screenshots'
        #file = os.path.join(file_dir, (rq + '.log'))
        #file_path = os.path.join(os.getcwd()) + '/Screenshots/'
        #print(file_path)
        pad = os.getcwd()
        file_dir = pad + '\\Screenshots\\'
        #file = os.path.join(file_dir, (rq + '.log'))
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_dir + rq + '.png'
        mylog.info(screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info("开始截图并保存")

        except Exception as e:
            mylog.error("出现异常", format(e))


