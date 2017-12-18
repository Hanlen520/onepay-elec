#  -*- coding:utf-8 -*-
'''
Created on 2016年7月14日

@author: tc
'''
import requests
import xml.dom.minidom
import json,MySQLdb,random,time,re
from datetime import date
from collections import OrderedDict #确保字典安初始顺序遍历


class Actions():

    def __init__(self):
        self.cfgfile="E:\\workspace\\onepay-elec\\config\\interfaceConfig-esc.xml"
        self.dependfile="E:\\workspace\\onepay-elec\\config\\interfaceConfig-sql-esc.xml"
        
    def sendRequest(self,servicename):
        #检查是否有依赖
        dependServiceName=self.checkDepend(servicename)
        if dependServiceName =="":
            pass
        else:
            self.sendRequest(dependServiceName)
        
        (method,url,body,headers)=self.packageData(servicename)
        #修改数据
        if dependServiceName =="":
            pass
        else:
            self.modifyBody(servicename,body)
        #修改现金充值交易创建dilipay.trade.create.deposit接口外部订单号
        if servicename=="dilipay.trade.create.deposit" or servicename=="dilipay.trade.create.direct":
            self.modifyOutTradeNum(body)
        #格式化数据
        jbody = json.dumps(body)
        headers=eval(headers)
        #开始发送
        try:
            if method=="post":
                response=requests.post(url,jbody,headers=headers)
                
                return response
            else:
                response=requests.get(url,jbody,headers=headers)
                
                return response
        except Exception,error:
            print error
            
    def verifyResult(self,response):
        content=response.text
        regex='"response":{"isSuccess":"T"'
        flag=False
        if re.search(regex,content) and response.status_code==200:
            flag=True
        else:
            print content,response.status_code
        
        return flag
       
    def packageData(self,servicename):
        dom=xml.dom.minidom.parse(self.cfgfile)
        root=dom.documentElement
        Scheme=root.getElementsByTagName("Scheme")[0].childNodes[0].data
        method=root.getElementsByTagName("method")[0].childNodes[0].data
        url=root.getElementsByTagName("url")[0].childNodes[0].data
        partnerId=root.getElementsByTagName("partnerId")[0].childNodes[0].data
        headers=root.getElementsByTagName("header")[0].childNodes[0].data
        url=Scheme+"://"+url+"&partnerId="+partnerId+"&service="+servicename
        interfaces=root.getElementsByTagName("interface")
        body={}
        for interface in interfaces:
            if interface.getAttribute("service")==servicename:
                for node in interface.childNodes:
                    if node.nodeType == node.ELEMENT_NODE:
                        body[node.nodeName] = node.childNodes[0].nodeValue
                        
        return method,url,body,headers
    
    def checkDepend(self,servicename):
        dom=xml.dom.minidom.parse(self.cfgfile)
        root=dom.documentElement
        interfaces=root.getElementsByTagName("interface")
        for interface in interfaces:
            if interface.getAttribute("service")==servicename:
                dependServiceName=interface.getAttribute("depend")
                
        return dependServiceName
    
    def modifyBody(self,servicename,body):
        #修改body内容
        l_depend_dict=self.getDependInfo(servicename)
        sql=l_depend_dict['sql']
        curdate=str(date.today())
        sql=sql+' where gmt_create > "'+ curdate + '" ORDER BY gmt_create desc LIMIT 1'
        data=self.conn(sql)
        #数据库中的值赋给l_depend_dict
        i=0
        for key in l_depend_dict.keys():
            if key != 'sql':
                if re.search('^\[',l_depend_dict[key]):
                    #json元素为列表
                    l_depend_dict[key]=eval(str('['+str(data[i])+']'))
                    i=i+1
                else:
                    l_depend_dict[key]=data[i] 
                    i=i+1
        #l_depend_dict中的值赋给body
        for key1 in l_depend_dict.keys():
            if key1 !='sql':
                for key2 in body.keys():
                    if key1 == key2:
                        body[key2]=l_depend_dict[key1]
        
    def getDependInfo(self,servicename):
        #获取依赖信息
        dom=xml.dom.minidom.parse(self.dependfile)
        root=dom.documentElement
        interfaces=root.getElementsByTagName("interface")
        l_depend_dict=OrderedDict()
        for interface in interfaces:
            if interface.getAttribute("service")==servicename:
                for node in interface.childNodes:
                    if node.nodeType == node.ELEMENT_NODE:
                        l_depend_dict[node.nodeName] = node.childNodes[0].nodeValue
       
        return l_depend_dict
    
    def modifyOutTradeNum(self,body):
        l_time=time.localtime()
        timeStr=time.strftime("%Y%m%d%H%M%S", l_time)
        num=random.randint(1,10000)
        num=str(num).zfill(5)
        l_outTradeNum=str(timeStr)+str(num)
        body['outTradeNo']=l_outTradeNum
    
    def conn(self,sql):
        try:
            conndb=MySQLdb.Connect(host='ip', user='用户名', passwd='密码', db='实例名',port=端口号)
            cur=conndb.cursor()
            #cur.select_db('实例名')
            print sql
            cur.execute(sql)
            result=cur.fetchone()
            conndb.commit()
            cur.close
            conndb.close
            return result
        except MySQLdb.Error,e:
            print (e.args[0], e.args[1])