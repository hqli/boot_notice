:: 设置python安装路径 
set python_path=C:\Python27
:: 设置开机通知脚本的安装路径
set bootnotice_path="C:\Program Files\BootNotice"

:: 删除开机通知脚本
rd /s /q  %bootnotice_path%

:: 将python27的环境变量清空
wmic ENVIRONMENT where "name='BPython27' and username='<system>'" set VariableValue="" 

:: 删除开机启动项
set id=%USERNAME%
del "C:\Users\%id%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot_notice.vbs"