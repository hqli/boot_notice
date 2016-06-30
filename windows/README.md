# 开机通知的windows安装
win7下面需要登录才能执行该脚本。

## 安装
- 下载64位python2.7（https://www.python.org/ftp/python/2.7.12/python-2.7.12.amd64.msi）安装到C:\Python27,如果安装到其他路径，需要修改install.bat和unisntall.bat
- 保证联网，管理员权限运行install.bat
    - 需要联网安装python的numpy库，具体可以看install.bat
- 如果安装电脑管家，需要将C:\Program Files\BootNotice文件夹和C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot_notice.vbs文件添加到信任区。
## 卸载
- 管理员权限运行uninstall.bat
- 在开始菜单卸载python2.7
