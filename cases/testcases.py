#!C:\Python27\python
# -*- coding: utf-8 -*-
'''
Created on 2016年7月15日

@author: tc
'''
import unittest,sys
from actions.actions import Actions

class TestCases(unittest.TestCase):


    def setUp(self):
        self.actions=Actions()
        SQL="update account_fund set balance='10000',frozen_amount='0',daily_balance='0',daily_frozen_amount='0' where account_id='105372'"
        self.actions.conn(SQL)

    def tearDown(self):
        pass

    def test_001(self):
        u"""账户资金增加"""
        response=self.actions.sendRequest("dilipay.account.add.balance")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)

    def test_002(self):
        u"""自助圈提-创建圈提记录"""
        response=self.actions.sendRequest("dilipay.trade.create.unload")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_003(self):
        u"""圈提"""
        response=self.actions.sendRequest("dilipay.trade.create.withdraw")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_004(self):
        u"""创建圈存记录"""
        response=self.actions.sendRequest("dilipay.trade.create.predeposit")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_005(self):
        u"""资金账户注册"""
        #电话号码重复
        response=self.actions.sendRequest("dilipay.account.info.register")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_006(self):
        u"""现金充值交易支付"""
        response=self.actions.sendRequest("dilipay.trade.pay")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_007(self):
        u"""现金充值交易创建"""
        response=self.actions.sendRequest("dilipay.trade.create.deposit")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_008(self):
        u"""现金提现"""
        response=self.actions.sendRequest("dilipay.trade.withdraw.cash")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_009(self):
        u"""统一账号身份认证"""
        response=self.actions.sendRequest("dilipay.account.secured.auth")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_010(self):
        u"""自动圈提确认"""
        response=self.actions.sendRequest("dilipay.account.balance.unload")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_011(self):
        u"""创建圈提记录"""
        response=self.actions.sendRequest("dilipay.trade.create.unload")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_012(self):
        u"""获取账户信息"""
        response=self.actions.sendRequest("dilipay.account.info.get")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_013(self):
        u"""获取账户可用余额"""
        response=self.actions.sendRequest("dilipay.account.balance.get")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_014(self):
        u"""解冻账号"""
        response=self.actions.sendRequest("dilipay.account.status.unfreeze")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_015(self):
        u"""冻结账号资金"""
        response=self.actions.sendRequest("dilipay.account.fund.freeze")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_016(self):
        u"""解冻账号资金"""
        response=self.actions.sendRequest("dilipay.account.fund.unfreeze")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_017(self):
        u"""账号冻结资金明细查询"""
        response=self.actions.sendRequest("dilipay.account.fund.freeze.list")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_018(self):
        u"""清除支付密码错误次数"""
        response=self.actions.sendRequest("dilipay.password.limit.clear")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_019(self):
        u"""批量解冻账号资金"""
        response=self.actions.sendRequest("dilipay.account.fund.unfreeze.batch")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        
    def test_020(self):
        u"""创建及时到账交易"""
        response=self.actions.sendRequest("dilipay.trade.create.direct")
        flag=self.actions.verifyResult(response)
        self.assertEqual(True, flag, u'接口测试失败:'+sys._getframe().f_code.co_name)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'qtest.qtestName']
    unittest.main()