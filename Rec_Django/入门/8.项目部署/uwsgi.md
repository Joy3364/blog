## install uwsgi
1. install uwsgi in python3.8, it has conflicts between python3.9 and uwsgi  
2. pip/conda install uwsgi

## uwsgi cmd
1. uwsgi --ini your_config_file.ini
2. after that, you will get a *.pid file: uwsgi --reload/stop *.pid

## how to set uwsgi

```python  
# uwsgi使用配置文件启动，配置如下
[uwsgi]
#项目目录
chdir=/home/loner/work_rf/web_app/myblog/
#指定项目application
module=myblog.wsgi:application
#指定sock的文件路径（nginx使用）
socket=uwsgi/uwsgi.sock
# 进程个数（processess一样效果）
workers=2
#指定启动时的pid文件路径
pidfile=uwsgi/uwsgi.pid
#指定ip及端口（配置nginx就不需要单独启动uwsgi需要填写）
#http=172.16.0.4:8001
#指定静态文件（配置nginx不需要，单独启动uwsgi加载静态文件）
#static-map=/static=/var/www/orange_web/static
#启动uwsgi的用户名和用户组
uid=root
gid=root
#启用主进程
master=true
# 启用线程
enable-threads=true
#自动移除unix Socket和pid文件当服务停止的时候
vacuum=true
#设置日志目录
daemonize=uwsgi/uwsgi.log
#不记录信息日志，只记录错误以及uwsgi内部消息
disable-logging=true
# 序列化接受的内容，如果可能的话
thunder-lock=true
```
