# -*- coding: utf-8 -*-
from  Base.base_methon import AmazonTest
import  unittest,time,os
from Public import base_runner

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AmazonTest))
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(basedir, 'test_Report')
    file = os.path.join(file_dir, (now + '.html'))
    re_open = open(file, 'wb')
    runner = base_runner.BSTestRunner(stream=re_open, title='amazon测试报告', description='测试结果')
    runner.run(suite)

