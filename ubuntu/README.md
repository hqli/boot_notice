# 开机通知的ubuntu安装

## 安装python以及opencv

需要联网
```
apt-get install python python-dev
apt-get install python-opencv
```

## 开机自启动
```
chmod +x boot_notice.py
cp boot_notice.py /usr/local/bin/
```
编辑/etc/rc.local，添加`python /usr/local/bin/boot_notice.py`
