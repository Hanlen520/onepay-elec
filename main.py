#!C:\Python27\python
# -*- coding: utf-8 -*-
#  -*- coding:utf-8 -*-
'''
Created on 2016年7月14日

@author: tc
'''
from cases.testcases import TestCases
import HTMLTestRunner,unittest

testunit=unittest.TestSuite()
#将测试用例加入到测试套件中
testunit.addTest(unittest.makeSuite(TestCases))

#定义报告存放路劲
reportname="E:\\workspace\\onepay-elec\\reports\\report.html"
reportdir="E:\\workspace\\onepay-elec\\reports\\"
curdate=str(date.today())
fp=file(reportname,'wb')

runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'电子交易结算接口测试报告',description=u'用例执行情况：')

#执行测试用例

runner.run(testunit)