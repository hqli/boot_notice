:: set python install path
set python_path=C:\Python27
:: set the software install path
set bootnotice_path="C:\Program Files\BootNotice"

:: delete the software install folder
rd /s /q  %bootnotice_path%

:: clean python27 path
wmic ENVIRONMENT where "name='BPython27' and username='<system>'" set VariableValue="" 

:: delete the software's boot
set id=%USERNAME%
del "C:\Users\%id%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot_notice.vbs"