# 开机通知
开机时，通过电脑摄像头拍摄照片，等待网络连接，通过邮件发送照片并删除所拍摄照片。

README和其他文档如果打开乱码。请使用notepad++等支持utf-8格式的文本编辑器打开。

## 简介
开机通知包括开机照相，等待网络连接，发送邮件后删除本地照片三部分。  
本脚本使用python编写，调用了opencv。

## 使用

### 邮箱设置
本代码中将邮箱bootnotice_test@163.com作为例子，仅仅验证代码可行性。  
其中的密码仅仅是授权码，并非密码。自己实际使用需要完成以下工作。

- 申请一个邮箱，在设置里，开通STMP
- 修改发送邮箱设置
    - 修改boot_notice.py中send_mail函数里的
    ```
    mail_host="smtp.163.com"
    mail_user="bootnotice_test"
    mail_pass="abcde12345"
    mail_postfix="163.com"
    ```
	
- 修改收件箱
    - 修改boot_notice.py中send_mail函数里的mail_to="bootnotice_test@163.com"

### 安装
见windows,ubuntu文件夹内的README.md

## 测试
在163邮箱通过，outlook邮箱未通过。
