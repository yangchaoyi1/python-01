#!/usr/bin/env python3
#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1767257599@qq.com'
pwd = 'ycfqnnvhlmuvbaea'
#pwd = 'qwe123!@#'
receivers = ['1767257599@qq.com']

message = MIMEText('Python 邮件发送测试……','plain','utf-8')
message['from'] = Header("邮件测试",'utf-8')
message['To'] = Header("测试",'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com",465)
    smtpObj.login(sender,pwd)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print("Error:无法发送邮件.Case:%s"%e)
