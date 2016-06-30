:: 设置python安装路径 
set python_path=C:\Python27
:: 设置开机通知脚本的安装路径
set bootnotice_path="C:\Program Files\BootNotice"

:: 创建开机通知脚本的安装文件夹
mkdir %bootnotice_path%

:: 将python可执行文件添加到Path中
wmic ENVIRONMENT create name="BPython27",username="<system>",VariableValue="%python_path%"

wmic ENVIRONMENT where "name='path' and username='<system>'" set VariableValue="%path%;%BPython27%" 

:: 将opencv支持添加到python的库
copy cv2.pyd %bootnotice_path%

:: 复制开机通知脚本到指定的安装路径
copy boot_notice.py %bootnotice_path%

copy boot_notice.bat %bootnotice_path%
:: 增加开机启动项
set id=%USERNAME%
copy boot_notice.vbs "C:\Users\%id%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"

:: 安装numpy，需要联网
%python_path%\Scripts\pip.exe install numpy