# 1.普通Python连接数据库
```
import pymysql
```
# 2.django的orm框架
```python
# 依赖于 mysqlclient，可能需要独立安装
# 只能创建表，不能创建库

# 2.1 在setting中配置

# 新增列

# 增
MODEL_NAME.objects.create(keylist)

# 查 得到列表类型的数据 QuerySet
MODEL_NAME.objects.filter(条件语句)
MODEL_NAME.objects.all(keylist)

# 删
MODEL_NAME.objects.filter(条件语句).delete()

# 改
MODEL_NAME.objects.filter(条件语句).update(keylist)

# 外键
to
tofield
级联删除models.CASCADE

# form
class MyForm(forms.Form):
    name = forms.charFeild(widght=forms.input)

{% for feild in myform % }
    {{field.lable}}:{{field}}
    {% endfor %}

# modelform
class MyForm(models.ModelForm):
    name = forms.charFeild(widght=forms.input)
    class Meta:
        model = 已经定义的其他Model
        fields = [要显示的字段名（可以来自model也可以来自自己）]
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control"}) #前端添加样式属性
        }

# 循环添加样式

def __init__(self,*args,**kwargs):
    super.__init__(*args,**kwargs)
    for name,field in self.fields.item():
        field.widget.attrs = {"class":"form-control"}

# 数据验证
if req.method == 'get':
    form_obj = MyForm(data=req.GET)
    if form_obj.is_valid():
        form.cleaned_data
        form_obj.save()
    else:
        print(form.errors)
    # 前端显示信息
    {{field.errors.0}}

# 长度限制
name = forms.charFeild(min_lenth=10,widght=forms.input)
# 正则表达式
name = forms.charFeild(validators='',widght=forms.input)

zh-hans
