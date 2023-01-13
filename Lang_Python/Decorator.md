## 1. 装饰器的实质
装饰器可以是函数，  
也可以是类，  
**装饰器** 接受一个 **函数** 作为 **参数**，  
**装饰器** 以该函数为核心，**构建**一个**新函数**，也是其**子函数**，  
**最后**把**子函数**返回给旧函数。 
具体查看 [菜鸟教程](https://www.runoob.com/w3cnote/python-func-decorators.html)

## 2. 函数型装饰器

### 2.1 装饰器与函数
```python

def a_decorator(arg_func):
 
    def wrapTheFunction( *arg,**kwarg ):
        print("before arg_func()")
        return arg_func( *arg,**kwarg )

    return wrapTheFunction #  return a sub_function
```
### 2.2 实质使用
```python
def a_function():
    print("I am a_func()")

a_function()
#outputs: "I am a_func()"
 
a_function = a_decorator(a_function)
#
 
a_function()
#outputs:before arg_func()
#        I am a_func()
#        after arg_func()
```
### 2.2 快捷使用
```python
@a_decorator
def a_function():
    print("I am a_func()")

```
### 2.3 带参的装饰器及其使用
```python
# 其实质是一个返回装饰器的函数
def a_decorator_factory(arg1 = "jack"):

    def a_decorator(arg_func): 
    
        def wrapTheFunction( *arg,**kwarg ):
            print("hello ",arg1)
            print("before arg_func()")
            return arg_func( *arg,**kwarg ) 

        return wrapTheFunction #  return a sub_function
    
    return a_decorator # return a decorator

# 使用方法
@a_decorator_factory(arg1 = "Marry")
def a_function():
    print("I am a_func()")
```
## 3. 类型装饰器
### 3.1 原理
__call__类方法使得对象成为一个函数
### 3.2 构造
```python
from functools import wraps
 
class logit():
    def __init__(self, logfile='out.log'):
        self.logfile = logfile
 
    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function
 
    def notify(self):
        # logit只打日志，不做别的
        pass
```
### 3.3 使用
```python
# a = logit() #创建一个对象
# a() 等同于 __call__(),a 等同于 __call__
#

@logit() #logit()返回一个匿名对象，
def myfunc1():
    print("myfunc1")

myfunc1()
```


