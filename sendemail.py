# -*- coding: utf-8 -*-

import subprocess,smtplib,email,os
from email.mime.text import MIMEText
from email.header import Header

def sendmail(fromaddress,toaddress,password,theme,context):
        msg = MIMEText(context,'plain','utf-8')
            msg['to'] = toaddress
                msg['from'] = fromaddress
                    msg['subject'] = theme
                        try:
                                    server = smtplib.SMTP_SSL("smtp.qq.com")
                                            server.connect('smtp.qq.com')
                                                    server.login(fromaddress,password)
                                                            server.sendmail(fromaddress, toaddress, msg.as_string())
                                                                    server.quit()
                                                                        except:
                                                                                    print('-----邮件发送失败-----')

                                                                                    if __name__ == "__main__":
                                                                                            while True:
                                                                                                        print("-----欢迎使用-----")
                                                                                                                ask = input("是否开始发送邮件请输入 y 或者 n ：")
                                                                                                                        if ask == 'y':
                                                                                                                                        print("-----开始发送邮件-----")
                                                                                                                                                    fromaddress = input("发送人地址：")
                                                                                                                                                                toaddress = input("收件人地址：")
                                                                                                                                                                            password = input("请输入授权码或者密码：")
                                                                                                                                                                                        theme = input("请输入主题：")
                                                                                                                                                                                                    context = input("请输入邮件正文内容：")
                                                                                                                                                                                                                send = input("是否确认发送请输入 y 或者 n ：")
                                                                                                                                                                                                                            if send == 'y':
                                                                                                                                                                                                                                                sendmail(fromaddress,toaddress,password,theme,context)
                                                                                                                                                                                                                                                            goout = input("是否退出请输入 y 或者 n ：")
                                                                                                                                                                                                                                                                        if goout == 'y':
                                                                                                                                                                                                                                                                                            break            
                                                                                                                                                                                                                                                                                            print("-----感谢使用-----")
