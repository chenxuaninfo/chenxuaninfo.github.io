#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import uuid

# 第三方 SMTP 服务
mail_host="smtp.aliyun.com"  #设置服务器
mail_user="medicalrobot@aliyun.com"    #用户名
mail_pass=""   #口令 

sender = 'medicalrobot@aliyun.com'
receivers = ['mrrobotxin@dingtalk.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText(str(uuid.uuid1()), 'plain', 'utf-8')
message['From'] = Header('medicalrobot@aliyun.com', 'utf-8')
message['To'] =  Header('mrrobotxin@dingtalk.com', 'utf-8')
 
subject = str('medicalrobot@aliyun.com')
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功"+str(uuid.uuid1()))
except smtplib.SMTPException:
    print("Error: 无法发送邮件"+str(uuid.uuid1()))