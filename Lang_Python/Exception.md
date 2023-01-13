## 异常捕获结构
```python
try:
    pass #有可能抛出异常的语句
except ExceptionName1,ExceptionName2:
    pass #发生异常时执行
    except ExceptionName3,ExceptionName4:
    pass #发生异常时执行
else:
    pass #不发生异常时执行
finally:
    pass #最后一定会执行
```

## 捕捉异常实例
```python
try:
    pass #有可能抛出异常的语句
except ExceptionName1 as e:
    print(e)
    pass #发生异常时执行
```

## 抛出异常
```python
# 1.抛出带参异常
try:
    a = input("输入一个数：")
    #判断用户输入的是否为数字
    if(not a.isdigit()):
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：",repr(e))
    
# 2.单raise，表示再次抛出异异常
try:
    a = input("输入一个数：")
    if(not a.isdigit()):
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：",repr(e))
    raise
# 3.单raise，表示抛出RuntimeError
try:
    a = input("输入一个数：")
    if(not a.isdigit()):
        raise
except RuntimeError as e:
    print("引发异常：",repr(e))
```

