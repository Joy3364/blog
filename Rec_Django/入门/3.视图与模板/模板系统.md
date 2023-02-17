## 1. 简介
在使用 template system 时，主要分为三个步骤，
1. You configure an Engine.
2. You compile template code into a Template.
3. You render the template with a Context.  
    
三个步骤的核心是配置引擎，  
引擎的主要配置项是 loader 与 context processors
分别用来**加载模板**与**渲染模板上下文**

开发过程中，django 的 template system 被封装为更高级的api

## 2. 配置 loader

```python
"""
有三个用的 loader
jango.template.loaders.filesystem.Loader
django.template.loaders.app_directories.Loader
django.template.loaders.cached.Loader 
"""
TEMPLATES = [
    {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': [ # 代表开启 filesystem.Loader
               '/home/html/templates/lawrence.com',
               '/home/html/templates/default',
           ],
       'APP_DIRS': True, # 代表开启 app_directories.Loader
    }
]
"""
django.template.loaders.cached.Loader 如果不配置option选项则默认开启，缓存被访问过的模板到内存，也可以指定开启

TEMPLATES = [
    {
       'BACKEND': 'django.template.backends.django.DjangoTemplates',
       'DIRS': ['/dfkvbkj/templates'],
       'OPTIONS': {
           'loaders': [
               ('django.template.loaders.cached.Loader', # 参数1，指定 loader
                  [ # 参数2，把以下参数传给参数1指定的 loader
                   'django.template.loaders.filesystem.Loader',
                   'django.template.loaders.app_directories.Loader',
                   'path.to.custom.Loader',
                  ]
                ),
           ],
       },
    }
]
"""
```
## 3. 自定义 loader
## 4. 内置 context processors
## 5. 自定义 context processors


