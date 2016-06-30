#!/usr/bin/env python
# -*- coding: utf-8 -*-
#导入smtplib和MIMEText
import smtplib
from email.MIMEText import MIMEText
import email.MIMEMultipart 
import email.MIMEBase  
import socket
import time
import os
import cv2
import platform


def wait_network():
    sysstr = platform.system()
    while(1):
        if(sysstr =="Windows"):
            net = os.system('ping www.baidu.com')
        elif(sysstr == "Linux"):
            net = os.system('ping www.baidu.com -c 2')
        else:
            print ("unknown System")
            break
        if net:
            time.sleep(30)
        else:
            break

def capture():
    cap = cv2.VideoCapture(0)
    time.sleep(0.25)
    cap.read()
    time.sleep(0.25)
    (ret, im) = cap.read()
    home = os.path.expanduser('~')
    sysstr = platform.system()
    if(sysstr =="Windows"):
        home+='\\'
    elif(sysstr == "Linux"):
        home+='/'
    else:
        print ("unknown System")
        exit()
    img_name = home+'boot_' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.jpg'

    cv2.imwrite(img_name, im)
    cap.release()
    return img_name


def send_mail(to_list, sub, contents, att):
    #设置服务器，用户名、口令以及邮箱的后缀
    mail_host="smtp.163.com"
    mail_user="bootnotice_test"
    mail_pass="abcde12345"
    mail_postfix="163.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    
    # 构造MIMEMultipart对象做为根容器  
    main_msg = email.MIMEMultipart.MIMEMultipart()  
      
    # 构造MIMEText对象做为邮件显示内容并附加到根容器  
    text_msg = email.MIMEText.MIMEText(contents)  
    main_msg.attach(text_msg)  
      
    # 构造MIMEBase对象做为文件附件内容并附加到根容器  
    contype = 'application/octet-stream'  
    maintype, subtype = contype.split('/', 1)  
    ## 读入文件内容并格式化  
    data = open(att, 'rb')  
    file_msg = email.MIMEBase.MIMEBase(maintype, subtype)  
    file_msg.set_payload(data.read( ))  
    data.close( )  
    email.Encoders.encode_base64(file_msg)  
      
    ## 设置附件头  
    basename = os.path.basename(att)  
    file_msg.add_header('Content-Disposition',  
     'attachment', filename = basename)  
    main_msg.attach(file_msg) 
      
    # 设置根容器属性  
    main_msg['From'] = me
    main_msg['To'] = to_list
    main_msg['Subject'] = sub
    main_msg['Date'] = email.Utils.formatdate( )  
      
    # 得到格式化后的完整文本  
    fullText = main_msg.as_string()
    
    # print fullText
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        # s.ehlo()
        # s.starttls()
        # s.ehlo()
        s.login(mail_user,mail_pass)
        # print 'login'
        s.sendmail(me, to_list, fullText)
        s.close()
        # print '1'
        return True
    except Exception, e:
        # print '2'
        print str(e)
        return False

if __name__ == '__main__':
    mail_to="bootnotice_test@163.com"
    sub = "Boot Notice"
    hostname = socket.gethostname()
    now =  time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    contents = hostname+" Up\n"+now
	
    att = capture()
    wait_network()
    
    if not send_mail(mail_to, sub, contents, att):
        print "boost notice send faild"
        exit()

	# delete att
    sysstr = platform.system()
    if(sysstr =="Windows"):
        os.system('del '+att)
    elif(sysstr == "Linux"):
        os.system('rm '+att)
    else:
        print ("unknown System")
