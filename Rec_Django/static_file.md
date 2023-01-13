# Django静态文件机制
## 0. 静态文件管理相关问题
1. 模板中的静态文件Url
2. django中的静态文件可以放在哪
3. django如何寻找静态文件
4. django如何部署静态文件
5. django如何处理用户上传的静态文件

## 1. 万物之始 
django中静态文件管理由**django.contrib.staticfiles**应用负责  
该应用需要在**INSTALLED_APPS**中注册  

## 2. 模板中静态文件的URL  
1. 需要django管理的,请按如下方式产生URL
```django
{% load static %}
<link rel="stylesheet" href="{% static 'polls/style.css' %}">
{# 生成的 URL 将以 STATIC_URL 的设置值为前缀 #}
```   
1. 不需要djang管理的请在nginx中配置好

## 3. 静态文件存放与寻找
静态文件寻找由**STATICFILES_FINDERS**指定寻找器进行寻找，常用寻找器有两个，如下
```python
STATICFILES_FINDERS = 
[
    'django.contrib.staticfiles.finders.FileSystemFinder', 
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
# AppDirectoriesFinder 从 app 目录下的 static 目录下寻找
# FileSystemFinder 与 STATICFILES_DIRS 搭配使用，django会在设定的目录下查找static文件，配置如下
STATICFILES_DIRS = [
    "/home/special.polls.com/polls/static",
    "/home/polls.com/polls/static",
    "/opt/webfiles/common",
]
```   
## 4. 部署静态文件
开发环境中  
生产环境中，静态文件一般由 nginx 服务器返回，以下方法可以简单实现
```python
# 设定 STATIC_ROOT
STATIC_ROOT = "/var/www/example.com/static/"
# 运行 collectstatic 命令
python manage.py collectstatic
# 之后所有静态文件会被收集到 STATIC_ROOT 目录下
# 存放结构由 {% static 'polls/style.css' %} 中的部分URL决定，本例中，会将静态文件如下存放
# /var/www/example.com/static/polls/style.css
















