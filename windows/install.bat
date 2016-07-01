:: set python install folder
set python_path=C:\Python27
:: set this software install folder
set bootnotice_path="C:\Program Files\BootNotice"

:: create this software install folder
mkdir %bootnotice_path%

:: add python script to Path
wmic ENVIRONMENT create name="BPython27",username="<system>",VariableValue="%python_path%"

wmic ENVIRONMENT where "name='path' and username='<system>'" set VariableValue="%path%;%BPython27%" 

:: copy opencv to this software install folder
copy cv2.pyd %bootnotice_path%

:: copy boot_notice.py and boot_notice.bat to install folder
copy boot_notice.py %bootnotice_path%

copy boot_notice.bat %bootnotice_path%
:: set the software start with boot
set id=%USERNAME%
copy boot_notice.vbs "C:\Users\%id%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"

:: install numpy need Internet
%python_path%\Scripts\pip.exe install numpy