## the major step for django  
1. start a project (django-admin startproject your_pro_name)
2. enter main project dir  
2. create an app (python manage.py startapp your_app_name)
3. register your app in setting.py ()
4. create a view.py in app dir and write view function (require a request as parama)
5. modify urls.py for your app ()
6. create a model sub class in your_app.models.py which should inherit from models.Model
7. register your_model in admin.py
8. python manage.py makemigrations and migrate  

## the set for static files  
1. set static files in dev environment  
    1.1 set ' STATIC_URL = ? ' in settings.py   
    1.2 set ' STATIC_ROOT = ? ' in settings.py  
    1.3 append 'static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)' in urls.py # it has different effects when it is writed in your_pro.urls and your_app.urls 
  
2. set static files in produce environment  
    2.1 set  'STATICFILES_DIRS = ['?','?',] in settings.py  
    2.2 set  'STATIC_ROOT = ? ' in settings.py  
    2.3 python manage.py collectstatic # after this, all static files will be collected to STATIC_ROOT  
    2.4 config nginx







